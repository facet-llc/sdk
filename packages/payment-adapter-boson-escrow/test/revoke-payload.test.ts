// validateRevokePayload, proven against REAL signed payloads.
//
// A revoke is the SELLER's half of a pre-redeem refund, and it differs from every
// buyer action in this package in a way that is easy to get wrong and silent when
// you do: it is signed over the GENERIC `MetaTransaction` struct, not
// `MetaTxExchange`. The two produce different digests, so validating a revoke with
// the buyer recovery (or vice versa) recovers a stranger's address and rejects a
// perfectly good payload. The struct-mismatch tests below are the ones that pin it.
//
// Fixtures are signed with the same primitives that produce a live payload, so these
// pin the actual wire contract rather than a hand-rolled mock of it.

import { encodeSignedPayload } from "@bosonprotocol/x402-evm/codec";
import { metaTransactionExchangeTypedData } from "@bosonprotocol/x402-core/eip712";
import { type Address, encodeFunctionData, type Hex, parseAbi, toHex } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { describe, expect, it } from "vitest";
import { validateCancelPayload, validateRevokePayload } from "../src/redeem-payload.ts";

const DIAMOND: Address = "0x000000000000000000000000000000000000d1a3";
const CHAIN_ID = 8453; // Base mainnet
const REVOKE_ABI = parseAbi(["function revokeVoucher(uint256 _exchangeId)"]);
const CANCEL_ABI = parseAbi(["function cancelVoucher(uint256 _exchangeId)"]);

/** The offer's seller assistant. */
const SELLER = privateKeyToAccount(`0x${"33".repeat(32)}` as Hex);
/** Anyone else. Note this account can produce a payload that passes every check
 *  here, because this module is the INTEGRITY layer: proving `from` is the real
 *  assistant is the caller's job (boson-seller-revoke.ts reads getSeller on-chain). */
const STRANGER = privateKeyToAccount(`0x${"44".repeat(32)}` as Hex);

/** Boson's generic MetaTransaction domain. Non-standard twice over: NO `chainId`
 *  field, and the chain carried in `salt` as 32 bytes. */
const domainFor = (chainId: number) =>
  ({
    name: "Boson Protocol",
    version: "V2",
    verifyingContract: DIAMOND,
    salt: toHex(chainId, { size: 32 }),
  }) as const;

const META_TX_TYPES = {
  MetaTransaction: [
    { name: "nonce", type: "uint256" },
    { name: "from", type: "address" },
    { name: "contractAddress", type: "address" },
    { name: "functionName", type: "string" },
    { name: "functionSignature", type: "bytes" },
  ],
} as const;

/** Produce a real seller-signed revoke, exactly as boson-seller-revoke.ts does. */
async function buildRevokePayload(opts: {
  account: typeof SELLER;
  exchangeId: bigint;
  /** Smuggle a different function through the seller path. */
  functionName?: string;
  /** Ship DIFFERENT calldata than the one the signature covers, modelling a
   *  tamper after signing. The signature is taken over `exchangeId`'s calldata and
   *  the payload then carries this id's calldata instead. */
  shippedCalldataExchangeId?: bigint;
  /** Sign over the BUYER struct instead, to prove the recovery variant matters. */
  useExchangeStruct?: boolean;
}): Promise<string> {
  const functionName = opts.functionName ?? "revokeVoucher(uint256)";
  const abi = functionName.startsWith("cancel") ? CANCEL_ABI : REVOKE_ABI;
  const fnName = functionName.startsWith("cancel") ? "cancelVoucher" : "revokeVoucher";
  // What the SIGNATURE covers.
  const signedFunctionSignature = encodeFunctionData({
    abi,
    functionName: fnName,
    args: [opts.exchangeId],
  });
  // What the payload actually SHIPS. Same unless the test is modelling a tamper.
  const shippedFunctionSignature =
    opts.shippedCalldataExchangeId === undefined
      ? signedFunctionSignature
      : encodeFunctionData({
          abi,
          functionName: fnName,
          args: [opts.shippedCalldataExchangeId],
        });
  const functionSignature = signedFunctionSignature;

  let signature: Hex;
  if (opts.useExchangeStruct === true) {
    const typedData = await metaTransactionExchangeTypedData({
      chainId: CHAIN_ID,
      verifyingContract: DIAMOND,
      nonce: 9n,
      from: opts.account.address,
      functionName,
      exchangeId: opts.exchangeId,
    });
    // deno-lint-ignore no-explicit-any
    signature = await opts.account.signTypedData(typedData as any);
  } else {
    signature = await opts.account.signTypedData({
      domain: domainFor(CHAIN_ID),
      types: META_TX_TYPES,
      primaryType: "MetaTransaction",
      message: {
        nonce: 9n,
        from: opts.account.address,
        contractAddress: DIAMOND,
        functionName,
        functionSignature,
      },
      // deno-lint-ignore no-explicit-any
    } as any);
  }

  return encodeSignedPayload({
    from: opts.account.address,
    nonce: "9",
    functionName,
    functionSignature: shippedFunctionSignature,
    sig: {
      v: parseInt(signature.slice(130, 132), 16),
      r: signature.slice(0, 66) as Hex,
      s: `0x${signature.slice(66, 130)}` as Hex,
    },
    // deno-lint-ignore no-explicit-any
  } as any) as string;
}

const args = (signedPayload: string, exchangeId: string) => ({
  signedPayload,
  exchangeId,
  chainId: CHAIN_ID,
  verifyingContract: DIAMOND,
});

describe("validateRevokePayload", () => {
  // The load-bearing case. A validator that refused a genuine revoke would strand
  // escrow (and a merchant approval) far more often than any attack.
  it("accepts a genuine seller-signed revoke and returns its signer", async () => {
    const payload = await buildRevokePayload({ account: SELLER, exchangeId: 42n });
    const res = await validateRevokePayload(args(payload, "42"));
    expect(res.ok).toBe(true);
    expect(res.signer?.toLowerCase()).toBe(SELLER.address.toLowerCase());
  });

  // Pins `recoverOver: "generic"`. Signed over the BUYER struct, the same bytes
  // recover to a different address, so this must fail rather than silently pass.
  it("REFUSES a revoke signed over the buyer MetaTxExchange struct", async () => {
    const payload = await buildRevokePayload({
      account: SELLER,
      exchangeId: 42n,
      useExchangeStruct: true,
    });
    const res = await validateRevokePayload(args(payload, "42"));
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("signature_mismatch");
  });

  // The inverse, which is what would break if someone "simplified" revoke onto the
  // shared buyer recovery: a genuine revoke must NOT validate as a cancel.
  it("REFUSES a genuine revoke when validated as a cancel", async () => {
    const payload = await buildRevokePayload({ account: SELLER, exchangeId: 42n });
    const res = await validateCancelPayload(args(payload, "42"));
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("not_a_cancel");
  });

  // A BUYER-signed cancel must not ride the seller path. Same refund outcome
  // on-chain, but the seller path is the one the assistant-address gate guards, so
  // letting a cancel through it would skip that gate entirely.
  it("REFUSES a cancelVoucher smuggled in as a revoke", async () => {
    const payload = await buildRevokePayload({
      account: SELLER,
      exchangeId: 42n,
      functionName: "cancelVoucher(uint256)",
    });
    const res = await validateRevokePayload(args(payload, "42"));
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("not_a_revoke");
  });

  // Self-binding. The exchange id lives inside the signed `functionSignature`, so a
  // payload cannot be re-filed against a different exchange.
  it("REFUSES a revoke filed against a different exchange id", async () => {
    const payload = await buildRevokePayload({ account: SELLER, exchangeId: 42n });
    const res = await validateRevokePayload(args(payload, "43"));
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("exchange_id_mismatch");
  });

  // Tampering with the calldata after signing breaks the digest, because the
  // calldata bytes ARE part of the signed message on this struct.
  it("REFUSES a revoke whose calldata was swapped after signing", async () => {
    // Signed for exchange 42, ships calldata for 99, then filed as 99. The id check
    // passes (the shipped calldata says 99), so this can ONLY be caught by the
    // signature, which covers the original bytes. That is the point of the test.
    const payload = await buildRevokePayload({
      account: SELLER,
      exchangeId: 42n,
      shippedCalldataExchangeId: 99n,
    });
    const res = await validateRevokePayload(args(payload, "99"));
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("signature_mismatch");
  });

  // Documents the DELIBERATE gap. A stranger can sign a well-formed revoke naming
  // their own address and it passes every check in this module, because proving
  // `from` is the offer's real assistant needs an on-chain read this module does not
  // do. boson-seller-revoke.ts performs that check against getSeller before relaying,
  // and the Diamond would reject it anyway. If this test ever starts failing, the
  // integrity/authorization split has changed and the caller's gate needs revisiting.
  it("accepts a stranger's well-formed revoke: authorization is the CALLER's job", async () => {
    const payload = await buildRevokePayload({ account: STRANGER, exchangeId: 42n });
    const res = await validateRevokePayload(args(payload, "42"));
    expect(res.ok).toBe(true);
    expect(res.signer?.toLowerCase()).toBe(STRANGER.address.toLowerCase());
  });

  it("REFUSES an undecodable payload", async () => {
    const res = await validateRevokePayload(args("0xdeadbeef", "42"));
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("payload_undecodable");
  });
});
