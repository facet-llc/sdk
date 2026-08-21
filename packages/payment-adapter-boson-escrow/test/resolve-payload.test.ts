// validateResolvePayload proven against REAL resolve payloads.
//
// A resolve payload is built exactly as the SDK's signMetaTxResolveDispute builds it:
// the buyer signs the outer MetaTxDisputeResolution struct (whose nested details carry
// the exchange id, the split, and the SELLER's Resolution signature), and the wire
// packs the resolveDispute(uint256,uint256,bytes) calldata plus that buyer signature.
// The types here are copied verbatim from the SDK source the validator was built from,
// so a passing happy path pins the wire contract and the attack cases pin the guards.

import { encodeSignedPayload } from "@bosonprotocol/x402-evm/codec";
import { type Address, encodeFunctionData, type Hex, parseAbi, toHex } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { describe, expect, it } from "vitest";
import { validateResolvePayload } from "../src/redeem-payload.ts";

const DIAMOND: Address = "0x000000000000000000000000000000000000d1a3";
const CHAIN_ID = 8453; // Base mainnet
const RESOLVE_ABI = parseAbi([
  "function resolveDispute(uint256 _exchangeId, uint256 _buyerPercentBasisPoints, bytes _signature)",
]);

const BUYER = privateKeyToAccount(`0x${"11".repeat(32)}` as Hex);
const SELLER = privateKeyToAccount(`0x${"33".repeat(32)}` as Hex);
const ATTACKER = privateKeyToAccount(`0x${"22".repeat(32)}` as Hex);

const BOSON_DOMAIN = {
  name: "Boson Protocol",
  version: "V2",
  verifyingContract: DIAMOND,
  salt: toHex(CHAIN_ID, { size: 32 }),
} as const;

const RESOLUTION_TYPES = {
  Resolution: [
    { name: "exchangeId", type: "uint256" },
    { name: "buyerPercentBasisPoints", type: "uint256" },
  ],
} as const;

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

/** The seller's half: an EIP-712 Resolution signature over (exchangeId, bps). */
function sellerResolutionSig(seller: typeof SELLER, exchangeId: bigint, bps: number): Promise<Hex> {
  return seller.signTypedData({
    domain: BOSON_DOMAIN,
    types: RESOLUTION_TYPES,
    primaryType: "Resolution",
    message: { exchangeId, buyerPercentBasisPoints: BigInt(bps) },
    // deno-lint-ignore no-explicit-any
  } as any);
}

/** Produce a real resolve payload exactly as a buyer's wallet would. The signed struct
 *  and the calldata are built from the same values (as the SDK does); overrides let a
 *  test desync them or smuggle a different action through. */
async function buildResolvePayload(opts: {
  account: typeof BUYER;
  exchangeId: bigint;
  buyerPercentBps: number;
  sellerSig: Hex;
  functionName?: string;
  calldataExchangeId?: bigint;
  calldataBuyerPercent?: number;
  calldataSellerSig?: Hex;
}): Promise<string> {
  const functionName = opts.functionName ?? "resolveDispute(uint256,uint256,bytes)";
  const cdExchange = opts.calldataExchangeId ?? opts.exchangeId;
  const cdPercent = BigInt(opts.calldataBuyerPercent ?? opts.buyerPercentBps);
  const cdSellerSig = opts.calldataSellerSig ?? opts.sellerSig;
  const nonce = 7n;
  const signature = await opts.account.signTypedData({
    domain: BOSON_DOMAIN,
    types: META_TX_DISPUTE_RESOLUTION_TYPES,
    primaryType: "MetaTxDisputeResolution",
    message: {
      nonce,
      from: opts.account.address,
      contractAddress: DIAMOND,
      functionName,
      disputeResolutionDetails: {
        exchangeId: cdExchange,
        buyerPercentBasisPoints: cdPercent,
        signature: cdSellerSig,
      },
    },
    // deno-lint-ignore no-explicit-any
  } as any);
  return encodeSignedPayload({
    from: opts.account.address,
    nonce: "7",
    functionName,
    functionSignature: encodeFunctionData({
      abi: RESOLVE_ABI,
      functionName: "resolveDispute",
      args: [cdExchange, cdPercent, cdSellerSig],
    }),
    sig: {
      v: parseInt(signature.slice(130, 132), 16),
      r: signature.slice(0, 66) as Hex,
      s: `0x${signature.slice(66, 130)}` as Hex,
    },
  });
}

const validate = (
  signedPayload: string,
  exchangeId: string,
  buyerPercentBps: number,
  expectedSellerSignature?: string,
) =>
  validateResolvePayload({
    signedPayload,
    exchangeId,
    buyerPercentBps,
    chainId: CHAIN_ID,
    verifyingContract: DIAMOND,
    ...(expectedSellerSignature !== undefined ? { expectedSellerSignature } : {}),
  });

describe("validateResolvePayload", () => {
  it("accepts a genuine buyer-signed resolve at the server-derived split", async () => {
    const sellerSig = await sellerResolutionSig(SELLER, 42n, 1140);
    const payload = await buildResolvePayload({
      account: BUYER,
      exchangeId: 42n,
      buyerPercentBps: 1140,
      sellerSig,
    });
    const result = await validate(payload, "42", 1140, sellerSig);
    expect(result.ok).toBe(true);
    expect(result.signer?.toLowerCase()).toBe(BUYER.address.toLowerCase());
  });

  it("refuses a resolve whose split is not the server-derived bps", async () => {
    // A genuine, well-signed resolve at 1140 bps, but the server authorized 5000. The
    // buyer does not get to choose the percentage.
    const sellerSig = await sellerResolutionSig(SELLER, 42n, 1140);
    const payload = await buildResolvePayload({
      account: BUYER,
      exchangeId: 42n,
      buyerPercentBps: 1140,
      sellerSig,
    });
    const result = await validate(payload, "42", 5000, sellerSig);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("buyer_percent_mismatch");
  });

  it("refuses a resolve filed against a different exchange", async () => {
    const sellerSig = await sellerResolutionSig(SELLER, 42n, 1140);
    const payload = await buildResolvePayload({
      account: BUYER,
      exchangeId: 42n,
      buyerPercentBps: 1140,
      sellerSig,
    });
    const result = await validate(payload, "99", 1140, sellerSig);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("exchange_id_mismatch");
  });

  it("refuses a non-resolve action (a raiseDispute smuggled in)", async () => {
    const sellerSig = await sellerResolutionSig(SELLER, 42n, 1140);
    const payload = await buildResolvePayload({
      account: BUYER,
      exchangeId: 42n,
      buyerPercentBps: 1140,
      sellerSig,
      functionName: "raiseDispute(uint256)",
    });
    const result = await validate(payload, "42", 1140, sellerSig);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("not_a_resolve");
  });

  it("refuses a resolve carrying a different seller signature than the one offered", async () => {
    const offered = await sellerResolutionSig(SELLER, 42n, 1140);
    const stale = await sellerResolutionSig(SELLER, 42n, 5000);
    const payload = await buildResolvePayload({
      account: BUYER,
      exchangeId: 42n,
      buyerPercentBps: 1140,
      sellerSig: stale,
    });
    const result = await validate(payload, "42", 1140, offered);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("signature_mismatch");
  });

  it("refuses calldata desynced from the buyer's signed struct", async () => {
    // The buyer signs a struct for exchange 42, but the calldata says 99: the Diamond
    // acts on the calldata, so the buyer signature must cover exactly what is submitted.
    const sellerSig = await sellerResolutionSig(SELLER, 42n, 1140);
    const nonce = 7n;
    const signature = await BUYER.signTypedData({
      domain: BOSON_DOMAIN,
      types: META_TX_DISPUTE_RESOLUTION_TYPES,
      primaryType: "MetaTxDisputeResolution",
      message: {
        nonce,
        from: BUYER.address,
        contractAddress: DIAMOND,
        functionName: "resolveDispute(uint256,uint256,bytes)",
        disputeResolutionDetails: {
          exchangeId: 42n,
          buyerPercentBasisPoints: 1140n,
          signature: sellerSig,
        },
      },
      // deno-lint-ignore no-explicit-any
    } as any);
    const desynced = encodeSignedPayload({
      from: BUYER.address,
      nonce: "7",
      functionName: "resolveDispute(uint256,uint256,bytes)",
      functionSignature: encodeFunctionData({
        abi: RESOLVE_ABI,
        functionName: "resolveDispute",
        args: [99n, 1140n, sellerSig],
      }),
      sig: {
        v: parseInt(signature.slice(130, 132), 16),
        r: signature.slice(0, 66) as Hex,
        s: `0x${signature.slice(66, 130)}` as Hex,
      },
    });
    const result = await validate(desynced, "99", 1140, sellerSig);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("signature_mismatch");
  });

  it("refuses a payload whose signature does not match its own from (forged)", async () => {
    // Signed by the attacker but the wire claims the buyer is `from`.
    const sellerSig = await sellerResolutionSig(SELLER, 42n, 1140);
    const nonce = 7n;
    const signature = await ATTACKER.signTypedData({
      domain: BOSON_DOMAIN,
      types: META_TX_DISPUTE_RESOLUTION_TYPES,
      primaryType: "MetaTxDisputeResolution",
      message: {
        nonce,
        from: BUYER.address,
        contractAddress: DIAMOND,
        functionName: "resolveDispute(uint256,uint256,bytes)",
        disputeResolutionDetails: {
          exchangeId: 42n,
          buyerPercentBasisPoints: 1140n,
          signature: sellerSig,
        },
      },
      // deno-lint-ignore no-explicit-any
    } as any);
    const forged = encodeSignedPayload({
      from: BUYER.address,
      nonce: "7",
      functionName: "resolveDispute(uint256,uint256,bytes)",
      functionSignature: encodeFunctionData({
        abi: RESOLVE_ABI,
        functionName: "resolveDispute",
        args: [42n, 1140n, sellerSig],
      }),
      sig: {
        v: parseInt(signature.slice(130, 132), 16),
        r: signature.slice(0, 66) as Hex,
        s: `0x${signature.slice(66, 130)}` as Hex,
      },
    });
    const result = await validate(forged, "42", 1140, sellerSig);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("signature_mismatch");
  });

  it("refuses undecodable bytes rather than throwing", async () => {
    const result = await validate("0xdeadbeef", "42", 1140);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("payload_undecodable");
  });

  it("refuses a non-integer server bps rather than signing garbage", async () => {
    const sellerSig = await sellerResolutionSig(SELLER, 42n, 1140);
    const payload = await buildResolvePayload({
      account: BUYER,
      exchangeId: 42n,
      buyerPercentBps: 1140,
      sellerSig,
    });
    const result = await validate(payload, "42", 11.4);
    expect(result.ok).toBe(false);
    expect(result.reason).toBe("buyer_percent_mismatch");
  });
});
