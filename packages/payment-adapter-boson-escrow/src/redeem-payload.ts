// Offline validation of a buyer's pre-signed Boson exchange meta-transaction
// (redeem OR pre-redeem cancel).
//
// The deferred-redeem policy stores the buyer's signed redeem at submit time and
// broadcasts it later, when the merchant fulfills. The pre-redeem refund path
// relays a buyer-signed cancel at dispatch time. In both cases the payload is
// paired with an `exchange_id` that is data, not proof — unless we check it. This
// module makes it proof.
//
// What the buyer actually signs (read from @bosonprotocol/core-sdk
// `makeExchangeMetaTxSigner`, the producer of these payloads):
//
//   MetaTxExchange {
//     nonce, from, contractAddress, functionName,
//     exchangeDetails: MetaTxExchangeDetails { exchangeId }
//   }
//   functionSignature = bosonExchangeHandlerIface
//                         .encodeFunctionData("<fn>", [exchangeId])
//
// redeemVoucher and cancelVoucher share the SAME MetaTxExchange struct family, so
// the same decode + recover logic validates both (only the expected function name
// differs). The exchange id is covered by the signature TWICE: once in the signed
// `exchangeDetails` struct and once inside the ABI-encoded calldata. That is what
// makes the payload self-binding: it can only ever act on the one exchange it was
// signed for, whatever id it is filed under locally. Pairing a payload with someone
// else's exchange id therefore cannot redirect funds — the on-chain call acts on
// the signed id.
//
// WHAT THIS DOES NOT PROVE (verified empirically against the SDK, not assumed):
// the signer check below confirms the payload recovers to its OWN `from`, i.e.
// that it is internally consistent and not forged or corrupt. It does NOT prove
// `from` is the exchange's real buyer — anyone can sign a well-formed payload
// naming THEIR OWN address for SOMEONE ELSE'S exchange id, and it passes every
// check here. Such a payload is useless on-chain (the Diamond rejects a
// redeem/cancel from a non-holder), but for the deferred-redeem STORE path it
// DISPLACES the real one. Establishing that the submitter owns/administers the
// exchange is therefore the CALLER's job and is not optional; this module is the
// integrity layer (is this a well-formed redeem/cancel for this exchange at all?),
// not the authorization layer. (The refund op adds `assertExchangeBinding` on top,
// binding the exchange to the calling merchant before relay.)
//
// Every check here is offline (no RPC): decode, compare, recover.

import { metaTransactionExchangeTypedData } from "@bosonprotocol/x402-core/eip712";
import { decodeSignedPayload } from "@bosonprotocol/x402-evm/codec";
import {
  type Abi,
  type Address,
  decodeFunctionData,
  type Hex,
  parseAbi,
  recoverTypedDataAddress,
  toHex,
} from "viem";

/** The Boson function a deferred redeem must call. Verbatim from core-sdk's
 *  `signMetaTxRedeemVoucher` → `makeExchangeMetaTxSigner("redeemVoucher(uint256)")`.
 *  A payload naming any other function is not a redeem: `cancelVoucher(uint256)`
 *  shares the MetaTxExchange struct and would otherwise validate, then CANCEL the
 *  exchange instead of releasing it to the merchant. */
export const BOSON_REDEEM_FUNCTION_NAME = "redeemVoucher(uint256)";

/** The Boson function a buyer-signed pre-redeem CANCEL must call. Verbatim from
 *  core-sdk's `signMetaTxCancelVoucher` → `makeExchangeMetaTxSigner("cancelVoucher(uint256)")`.
 *  Same MetaTxExchange struct family as redeem; only the function name differs. */
export const BOSON_CANCEL_FUNCTION_NAME = "cancelVoucher(uint256)";

/** The buyer-signed dispute functions. All three are `makeExchangeMetaTxSigner`
 *  actions (verbatim from core-sdk's `signMetaTxRaiseDispute` /
 *  `signMetaTxRetractDispute` / `signMetaTxEscalateDispute`), i.e. the SAME
 *  MetaTxExchange struct family as redeem/cancel, over the dispute-handler iface —
 *  only the function name (and its `(uint256 exchangeId)` selector) differ. The
 *  mutual `resolveDispute` is deliberately absent: it carries a counterparty
 *  signature in a different struct and is not a buyer-only exchange meta-tx. */
export const BOSON_RAISE_DISPUTE_FUNCTION_NAME = "raiseDispute(uint256)";
export const BOSON_RETRACT_DISPUTE_FUNCTION_NAME = "retractDispute(uint256)";
export const BOSON_ESCALATE_DISPUTE_FUNCTION_NAME = "escalateDispute(uint256)";

/** The mutual resolveDispute. Unlike every buyer-only action above it takes THREE args
 *  (exchangeId, buyerPercentBasisPoints, and the seller's counterparty signature) and
 *  its outer meta-tx is signed over `MetaTxDisputeResolution`, a different struct family,
 *  so it needs its own validator. Verbatim from core-sdk's `signMetaTxResolveDispute`. */
export const BOSON_RESOLVE_DISPUTE_FUNCTION_NAME = "resolveDispute(uint256,uint256,bytes)";

/** The Boson function a SELLER-signed pre-redeem REVOKE must call. The merchant's
 *  side of a pre-redeem refund: the seller cancels a committed exchange before
 *  fulfillment and the escrowed USDC returns to the buyer in full.
 *
 *  Two things differ from every other action in this module, and both matter.
 *  It is signed by the seller ASSISTANT, not the buyer, so `from` is the assistant
 *  address rather than the voucher holder. And it is signed over the GENERIC
 *  `MetaTransaction` struct rather than `MetaTxExchange`, because core-sdk has no
 *  `makeExchangeMetaTxSigner` entry for it (x402-client refuses to sign revoke at
 *  all: it is seller-only and throws). Hence `recoverOver: "generic"` below. */
export const BOSON_REVOKE_FUNCTION_NAME = "revokeVoucher(uint256)";

const REDEEM_ABI = parseAbi(["function redeemVoucher(uint256 _exchangeId)"]);
const REVOKE_ABI = parseAbi(["function revokeVoucher(uint256 _exchangeId)"]);
const CANCEL_ABI = parseAbi(["function cancelVoucher(uint256 _exchangeId)"]);
const RAISE_DISPUTE_ABI = parseAbi(["function raiseDispute(uint256 _exchangeId)"]);
const RETRACT_DISPUTE_ABI = parseAbi(["function retractDispute(uint256 _exchangeId)"]);
const ESCALATE_DISPUTE_ABI = parseAbi(["function escalateDispute(uint256 _exchangeId)"]);
const RESOLVE_DISPUTE_ABI = parseAbi([
  "function resolveDispute(uint256 _exchangeId, uint256 _buyerPercentBasisPoints, bytes _signature)",
]);

/** Why a payload was refused. Each is a hard refusal: none of these can arise from
 *  a well-formed redeem/cancel the buyer actually signed for this exchange. */
export type RedeemPayloadRejection =
  /** Not a decodable ABI-encoded BosonMetaTx tuple. */
  | "payload_undecodable"
  /** Decodes, but calls something other than redeemVoucher (e.g. cancelVoucher). */
  | "not_a_redeem"
  /** Decodes, but calls something other than cancelVoucher (e.g. redeemVoucher). */
  | "not_a_cancel"
  /** Decodes, but calls something other than revokeVoucher. Notably a cancelVoucher
   *  smuggled in as a revoke: same refund outcome on-chain, but it would let a
   *  BUYER-signed payload ride the seller path and skip the assistant-address gate. */
  | "not_a_revoke"
  /** Decodes, but calls something other than the requested dispute action (raise/
   *  retract/escalate), e.g. a cancelVoucher smuggled in as a dispute. */
  | "not_a_dispute"
  /** Decodes, but calls something other than resolveDispute. */
  | "not_a_resolve"
  /** A resolveDispute whose buyerPercentBasisPoints is not the server-derived split;
   *  the buyer may not choose the percentage. */
  | "buyer_percent_mismatch"
  /** The calldata is not a well-formed <fn>(uint256) call. */
  | "calldata_unreadable"
  /** The signed exchange id is not the exchange this payload was filed against. */
  | "exchange_id_mismatch"
  /** The signature does not recover to the meta-tx's own `from`: forged or corrupt. */
  | "signature_mismatch"
  /** The escrow Diamond passed in is not an address, so the typed-data domain
   *  cannot be rebuilt and nothing can be verified. A host misconfiguration, not a
   *  bad submission: refuse rather than store bytes we were unable to check. */
  | "verifying_contract_invalid";

export interface RedeemPayloadValidation {
  readonly ok: boolean;
  readonly reason?: RedeemPayloadRejection;
  readonly message?: string;
  /** The buyer EOA the payload is signed by, on success. */
  readonly signer?: Address;
}

export interface ValidateRedeemPayloadArgs {
  /** The wire-format signed payload: ABI-encoded BosonMetaTx tuple. */
  readonly signedPayload: string;
  /** The exchange this payload is being stored against (decimal string). */
  readonly exchangeId: string;
  /** EVM chain the exchange lives on (Base mainnet = 8453). */
  readonly chainId: number;
  /** The Boson escrow Diamond: the EIP-712 verifyingContract. Accepted as a plain
   *  string (hosts carry it as config, e.g. the Terminal's `cfg.boson.escrow`) and
   *  shape-checked here, so callers need not pre-narrow it. */
  readonly verifyingContract: string;
}

/** Cancel uses the identical args shape as redeem. */
export type ValidateCancelPayloadArgs = ValidateRedeemPayloadArgs;

const ADDRESS_RE = /^0x[0-9a-fA-F]{40}$/;

/** The function-specific bits that distinguish a redeem payload from a cancel
 *  payload — everything else in the validation is identical. */
interface ExchangeActionSpec {
  readonly functionName: string;
  readonly abi: Abi;
  /** The rejection reason emitted when the payload calls a DIFFERENT function. */
  readonly wrongFunctionReason: RedeemPayloadRejection;
  /** Which EIP-712 struct the signature was taken over, because Boson uses two.
   *
   *  "exchange" (default) is `MetaTxExchange`, carrying `exchangeDetails.exchangeId`.
   *  Every BUYER action (redeem, cancel, raise/retract/escalate) is signed this way,
   *  via core-sdk's `makeExchangeMetaTxSigner`.
   *
   *  "generic" is the plain `MetaTransaction` struct (nonce, from, contractAddress,
   *  functionName, functionSignature), which is what core-sdk's `signMetaTx` produces
   *  for actions outside that family. The SELLER's `revokeVoucher` is one of them.
   *
   *  Picking the wrong one recovers a different address and rejects every legitimate
   *  payload, which is the trap the note above the recovery step warns about. */
  readonly recoverOver?: "exchange" | "generic";
}

/** Shared core: validate that `signedPayload` is a buyer-signed MetaTxExchange for
 *  EXACTLY `exchangeId` that calls `spec.functionName`. Redeem and cancel differ
 *  only by `spec`.
 *
 *  Fails CLOSED: any decode error, mismatch, or unexpected shape is a refusal, and
 *  a refusal can never break a legitimate payload (a real one signed for this
 *  exchange passes every check). Never throws; a thrown decode error is mapped to a
 *  rejection so a malformed submission is a 4xx, not a 500. */
async function validateExchangeMetaTxPayload(
  args: ValidateRedeemPayloadArgs,
  spec: ExchangeActionSpec,
): Promise<RedeemPayloadValidation> {
  if (!ADDRESS_RE.test(args.verifyingContract)) {
    return {
      ok: false,
      reason: "verifying_contract_invalid",
      message: `verifyingContract "${args.verifyingContract}" is not an EVM address.`,
    };
  }

  let metaTx: ReturnType<typeof decodeSignedPayload>;
  try {
    metaTx = decodeSignedPayload(args.signedPayload as Hex);
  } catch (e) {
    return {
      ok: false,
      reason: "payload_undecodable",
      message: `signed_payload is not a decodable BosonMetaTx tuple: ${
        e instanceof Error ? e.message : String(e)
      }`,
    };
  }

  if (metaTx.functionName !== spec.functionName) {
    return {
      ok: false,
      reason: spec.wrongFunctionReason,
      message: `signed_payload calls "${metaTx.functionName}", not "${spec.functionName}".`,
    };
  }

  // The exchange id inside the ABI-encoded calldata: what the Diamond will
  // actually act on when this is broadcast.
  let calldataExchangeId: bigint;
  try {
    // The codec's BosonMetaTx surfaces its hex fields as plain `string` under the
    // Terminal's Deno resolution; they are codec-produced hex, so narrowing here is
    // safe and decodeFunctionData validates the bytes regardless.
    const decoded = decodeFunctionData({
      abi: spec.abi,
      data: metaTx.functionSignature as Hex,
    });
    const arg0 = decoded.args?.[0];
    if (typeof arg0 !== "bigint") throw new Error("first arg is not a uint256 exchange id");
    calldataExchangeId = arg0;
  } catch (e) {
    return {
      ok: false,
      reason: "calldata_unreadable",
      message: `signed_payload functionSignature is not a ${spec.functionName} call: ${
        e instanceof Error ? e.message : String(e)
      }`,
    };
  }

  let claimed: bigint;
  try {
    claimed = BigInt(args.exchangeId);
  } catch {
    return {
      ok: false,
      reason: "exchange_id_mismatch",
      message: `exchange_id "${args.exchangeId}" is not a numeric exchange id.`,
    };
  }
  if (calldataExchangeId !== claimed) {
    return {
      ok: false,
      reason: "exchange_id_mismatch",
      message: `signed_payload targets exchange ${calldataExchangeId}, not ${claimed}.`,
    };
  }

  // Recover the signer over the EXCHANGE typed-data (primary type MetaTxExchange,
  // carrying exchangeDetails.exchangeId). NOTE: the SDK's own
  // `recoverMetaTransactionSigner` builds the GENERIC `MetaTransaction` typed-data
  // instead, which is a different struct — using it here would recover a wrong
  // address and reject every legitimate payload.
  let recovered: Address;
  try {
    const typedData =
      spec.recoverOver === "generic"
        ? // The plain MetaTransaction struct, verbatim from core-sdk's `signMetaTx`.
          // Boson's domain here is non-standard in two ways that both matter: there is
          // NO `chainId` field, and the chain is carried in `salt` as a 32-byte value.
          // `contractAddress` is the Diamond, the same address as `verifyingContract`.
          {
            domain: {
              name: "Boson Protocol",
              version: "V2",
              verifyingContract: args.verifyingContract as Address,
              salt: toHex(args.chainId, { size: 32 }),
            },
            types: {
              MetaTransaction: [
                { name: "nonce", type: "uint256" },
                { name: "from", type: "address" },
                { name: "contractAddress", type: "address" },
                { name: "functionName", type: "string" },
                { name: "functionSignature", type: "bytes" },
              ],
            },
            primaryType: "MetaTransaction",
            message: {
              nonce: BigInt(metaTx.nonce),
              from: metaTx.from as Address,
              contractAddress: args.verifyingContract as Address,
              functionName: spec.functionName,
              functionSignature: metaTx.functionSignature as Hex,
            },
          }
        : await metaTransactionExchangeTypedData({
            chainId: args.chainId,
            verifyingContract: args.verifyingContract as Address,
            nonce: BigInt(metaTx.nonce),
            from: metaTx.from as Address,
            functionName: spec.functionName,
            exchangeId: claimed,
          });
    recovered = await recoverTypedDataAddress({
      // The builder returns a deliberately-loose typed-data shape (Boson's
      // EIP712Domain field set is non-standard); viem accepts it structurally.
      domain: typedData.domain,
      types: typedData.types,
      primaryType: typedData.primaryType,
      message: typedData.message,
      signature: { r: metaTx.sig.r, s: metaTx.sig.s, v: BigInt(metaTx.sig.v) },
      // deno-lint-ignore no-explicit-any
    } as any);
  } catch (e) {
    return {
      ok: false,
      reason: "signature_mismatch",
      message: `signed_payload signature could not be recovered: ${
        e instanceof Error ? e.message : String(e)
      }`,
    };
  }

  if (recovered.toLowerCase() !== metaTx.from.toLowerCase()) {
    return {
      ok: false,
      reason: "signature_mismatch",
      message: "signed_payload signature does not match its own `from` address.",
    };
  }

  return { ok: true, signer: recovered };
}

/** Validate that `signedPayload` is a buyer-signed REDEEM for EXACTLY `exchangeId`. */
export function validateRedeemPayload(
  args: ValidateRedeemPayloadArgs,
): Promise<RedeemPayloadValidation> {
  return validateExchangeMetaTxPayload(args, {
    functionName: BOSON_REDEEM_FUNCTION_NAME,
    abi: REDEEM_ABI,
    wrongFunctionReason: "not_a_redeem",
  });
}

/** Validate that `signedPayload` is a buyer-signed pre-redeem CANCEL for EXACTLY
 *  `exchangeId`. Self-binding over the exchange id, same as redeem; the refund op
 *  layers `assertExchangeBinding` on top to bind the exchange to the merchant. */
export function validateCancelPayload(
  args: ValidateCancelPayloadArgs,
): Promise<RedeemPayloadValidation> {
  return validateExchangeMetaTxPayload(args, {
    functionName: BOSON_CANCEL_FUNCTION_NAME,
    abi: CANCEL_ABI,
    wrongFunctionReason: "not_a_cancel",
  });
}

/** Validate that `signedPayload` is a SELLER-signed pre-redeem REVOKE for EXACTLY
 *  `exchangeId`. Self-binding over the exchange id like cancel, so the payload can
 *  only ever act on the exchange it was signed for.
 *
 *  This is the integrity layer only, and the gap it leaves is bigger here than for
 *  the buyer actions. It proves the payload is a well-formed revoke that recovers to
 *  its own `from`; it does NOT prove `from` is the offer's seller assistant. Anyone
 *  can sign a well-formed revoke naming their own address, and the Diamond would
 *  refuse it on-chain, but Facet must not relay it in the first place. The CALLER is
 *  therefore required to check the recovered signer against
 *  `getSeller(sellerId).assistant` before relaying, exactly as the proven
 *  scripts/agent-demos/mainnet-revoke.ts harness does. */
export function validateRevokePayload(
  args: ValidateCancelPayloadArgs,
): Promise<RedeemPayloadValidation> {
  return validateExchangeMetaTxPayload(args, {
    functionName: BOSON_REVOKE_FUNCTION_NAME,
    abi: REVOKE_ABI,
    wrongFunctionReason: "not_a_revoke",
    recoverOver: "generic",
  });
}

/** The buyer-only dispute meta-tx actions that share the MetaTxExchange struct
 *  family. `resolve` is excluded on purpose (different, counterparty-signed
 *  struct — see the function-name constants above). */
export type DisputeMetaTxAction = "raise" | "retract" | "escalate";

const DISPUTE_SPECS: Record<DisputeMetaTxAction, ExchangeActionSpec> = {
  raise: {
    functionName: BOSON_RAISE_DISPUTE_FUNCTION_NAME,
    abi: RAISE_DISPUTE_ABI,
    wrongFunctionReason: "not_a_dispute",
  },
  retract: {
    functionName: BOSON_RETRACT_DISPUTE_FUNCTION_NAME,
    abi: RETRACT_DISPUTE_ABI,
    wrongFunctionReason: "not_a_dispute",
  },
  escalate: {
    functionName: BOSON_ESCALATE_DISPUTE_FUNCTION_NAME,
    abi: ESCALATE_DISPUTE_ABI,
    wrongFunctionReason: "not_a_dispute",
  },
};

/** Dispute uses the identical args shape as redeem/cancel, plus the specific
 *  buyer action the payload must match. */
export type ValidateDisputePayloadArgs = ValidateRedeemPayloadArgs & {
  readonly action: DisputeMetaTxAction;
};

/** Validate that `signedPayload` is a buyer-signed dispute (raise/retract/escalate,
 *  per `args.action`) for EXACTLY `args.exchangeId`. Self-binding over the exchange
 *  id, same as redeem/cancel: it makes the site-bound exchange the Terminal
 *  authorized the one the facilitator will actually act on (the SDK relays the
 *  payload's OWN embedded exchange id, so without this the two can differ). The
 *  dispute op layers the on-chain buyer-signature gate on top; `resolve` is not a
 *  buyer-only action and is validated elsewhere. */
export function validateDisputePayload(
  args: ValidateDisputePayloadArgs,
): Promise<RedeemPayloadValidation> {
  return validateExchangeMetaTxPayload(args, DISPUTE_SPECS[args.action]);
}

/** The Boson `MetaTxDisputeResolution` struct set, verbatim from core-sdk's
 *  `signMetaTxResolveDispute`. The buyer signs the OUTER struct, whose nested
 *  `disputeResolutionDetails` carries the exchange id, the split, AND the seller's
 *  counterparty signature, so the buyer's signature covers all three at once: a buyer
 *  cannot alter the percentage or swap the seller sig without invalidating their own. */
const META_TX_DISPUTE_RESOLUTION_TYPES = {
  MetaTxDisputeResolution: [
    { name: "nonce", type: "uint256" },
    { name: "from", type: "address" },
    { name: "contractAddress", type: "address" },
    { name: "functionName", type: "string" },
    { name: "disputeResolutionDetails", type: "MetaTxDisputeResolutionDetails" },
  ],
  MetaTxDisputeResolutionDetails: [
    { name: "exchangeId", type: "uint256" },
    { name: "buyerPercentBasisPoints", type: "uint256" },
    { name: "signature", type: "bytes" },
  ],
} as const;

export type ValidateResolvePayloadArgs = ValidateRedeemPayloadArgs & {
  /** The SERVER-derived buyer share, in basis points. The payload's own
   *  buyerPercentBasisPoints MUST equal this: the buyer never chooses the split. */
  readonly buyerPercentBps: number;
  /** The exact seller Resolution signature Facet offered for this ticket, if known.
   *  When provided, the payload's embedded seller sig must match it byte for byte, so a
   *  buyer cannot pair a stale or different offer with this exchange. */
  readonly expectedSellerSignature?: string;
};

/** Validate that `signedPayload` is a buyer-signed `resolveDispute` for EXACTLY
 *  `args.exchangeId` at EXACTLY `args.buyerPercentBps`, carrying the seller's
 *  counterparty signature.
 *
 *  resolve is NOT a buyer-only exchange action: its outer meta-tx is
 *  `MetaTxDisputeResolution` (not `MetaTxExchange`) and its calldata is
 *  `resolveDispute(uint256,uint256,bytes)` (not `<fn>(uint256)`), so it cannot reuse
 *  `validateExchangeMetaTxPayload`. Every check is offline: decode, compare, recover.
 *
 *  On-chain the seller's Resolution signature is already bound to
 *  `(exchangeId, buyerPercent)`, so a buyer who alters either invalidates the seller sig
 *  and the Diamond reverts. This layer turns that opaque revert into an explicit refusal
 *  AND stops a buyer from relaying a validly-signed split for a DIFFERENT
 *  (exchange, percent) than the ticket authorized, which would settle the chain and the
 *  merchant's books at odds. Never throws. */
export async function validateResolvePayload(
  args: ValidateResolvePayloadArgs,
): Promise<RedeemPayloadValidation> {
  if (!ADDRESS_RE.test(args.verifyingContract)) {
    return {
      ok: false,
      reason: "verifying_contract_invalid",
      message: `verifyingContract "${args.verifyingContract}" is not an EVM address.`,
    };
  }
  if (!Number.isInteger(args.buyerPercentBps)) {
    return {
      ok: false,
      reason: "buyer_percent_mismatch",
      message: `buyerPercentBps ${args.buyerPercentBps} is not an integer.`,
    };
  }

  let metaTx: ReturnType<typeof decodeSignedPayload>;
  try {
    metaTx = decodeSignedPayload(args.signedPayload as Hex);
  } catch (e) {
    return {
      ok: false,
      reason: "payload_undecodable",
      message: `signed_payload is not a decodable BosonMetaTx tuple: ${
        e instanceof Error ? e.message : String(e)
      }`,
    };
  }

  if (metaTx.functionName !== BOSON_RESOLVE_DISPUTE_FUNCTION_NAME) {
    return {
      ok: false,
      reason: "not_a_resolve",
      message: `signed_payload calls "${metaTx.functionName}", not "${BOSON_RESOLVE_DISPUTE_FUNCTION_NAME}".`,
    };
  }

  // resolveDispute(exchangeId, buyerPercentBasisPoints, sellerSignature): the id and
  // the split the Diamond will actually act on, plus the seller's counterparty sig.
  let calldataExchangeId: bigint;
  let calldataBuyerPercent: bigint;
  let sellerSignature: Hex;
  try {
    const decoded = decodeFunctionData({
      abi: RESOLVE_DISPUTE_ABI,
      data: metaTx.functionSignature as Hex,
    });
    const a0 = decoded.args?.[0];
    const a1 = decoded.args?.[1];
    const a2 = decoded.args?.[2];
    if (typeof a0 !== "bigint" || typeof a1 !== "bigint" || typeof a2 !== "string") {
      throw new Error("resolveDispute args are not (uint256, uint256, bytes)");
    }
    calldataExchangeId = a0;
    calldataBuyerPercent = a1;
    sellerSignature = a2 as Hex;
  } catch (e) {
    return {
      ok: false,
      reason: "calldata_unreadable",
      message: `signed_payload functionSignature is not a resolveDispute call: ${
        e instanceof Error ? e.message : String(e)
      }`,
    };
  }

  let claimed: bigint;
  try {
    claimed = BigInt(args.exchangeId);
  } catch {
    return {
      ok: false,
      reason: "exchange_id_mismatch",
      message: `exchange_id "${args.exchangeId}" is not a numeric exchange id.`,
    };
  }
  if (calldataExchangeId !== claimed) {
    return {
      ok: false,
      reason: "exchange_id_mismatch",
      message: `signed_payload targets exchange ${calldataExchangeId}, not ${claimed}.`,
    };
  }

  if (calldataBuyerPercent !== BigInt(args.buyerPercentBps)) {
    return {
      ok: false,
      reason: "buyer_percent_mismatch",
      message: `signed_payload splits at ${calldataBuyerPercent} bps, not the server-derived ${args.buyerPercentBps}.`,
    };
  }

  if (
    args.expectedSellerSignature !== undefined &&
    sellerSignature.toLowerCase() !== args.expectedSellerSignature.toLowerCase()
  ) {
    return {
      ok: false,
      reason: "signature_mismatch",
      message:
        "signed_payload carries a different seller Resolution signature than the one offered.",
    };
  }

  // Recover the buyer over MetaTxDisputeResolution. The buyer's signature covers the
  // nested details, so this proves internal consistency AND re-confirms that the
  // exchange id and split checked above are the ones the buyer actually signed.
  let recovered: Address;
  try {
    recovered = await recoverTypedDataAddress({
      domain: {
        name: "Boson Protocol",
        version: "V2",
        verifyingContract: args.verifyingContract as Address,
        salt: toHex(args.chainId, { size: 32 }),
      },
      types: META_TX_DISPUTE_RESOLUTION_TYPES,
      primaryType: "MetaTxDisputeResolution",
      message: {
        nonce: BigInt(metaTx.nonce),
        from: metaTx.from as Address,
        contractAddress: args.verifyingContract as Address,
        functionName: BOSON_RESOLVE_DISPUTE_FUNCTION_NAME,
        disputeResolutionDetails: {
          exchangeId: claimed,
          buyerPercentBasisPoints: calldataBuyerPercent,
          signature: sellerSignature,
        },
      },
      signature: { r: metaTx.sig.r, s: metaTx.sig.s, v: BigInt(metaTx.sig.v) },
      // deno-lint-ignore no-explicit-any
    } as any);
  } catch (e) {
    return {
      ok: false,
      reason: "signature_mismatch",
      message: `signed_payload signature could not be recovered: ${
        e instanceof Error ? e.message : String(e)
      }`,
    };
  }

  if (recovered.toLowerCase() !== metaTx.from.toLowerCase()) {
    return {
      ok: false,
      reason: "signature_mismatch",
      message: "signed_payload signature does not match its own `from` address.",
    };
  }

  return { ok: true, signer: recovered };
}
