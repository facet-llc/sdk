// Per-line escrow (S2, behind FACET_BOSON_PER_LINE_ESCROW): the three adapter
// legs go N-per-line when options.line_items / authority.lines are present.
// Drives quote -> verify -> reserve against the mocked SDK (validatePaymentPayload
// + the x402b server handlers stubbed; decodeXPaymentHeader stays real), and
// asserts the money-path invariants: each line seller-signed, the per-line
// amounts bind to the cart total, one buyer across the cart, and a partial commit
// records its successes without unwinding.

import { describe, expect, it, vi } from "vitest";

import type {
  MerchantConfig,
  RailRequestContext,
  ReserveAuthorityInput,
  VerifyAuthorityInput,
} from "@facet-llc/adapter";
import type { EscrowPaymentRequirements } from "@bosonprotocol/x402-core/schemes/escrow";

const h = vi.hoisted(() => ({ buildReqFn: vi.fn(), validateFn: vi.fn(), commitFn: vi.fn() }));

vi.mock("@bosonprotocol/x402-server", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@bosonprotocol/x402-server")>();
  return {
    ...actual,
    validatePaymentPayload: h.validateFn,
    createX402bServer: () => ({
      buildPaymentRequirements: h.buildReqFn,
      facilitator: { performAction: vi.fn() },
      handlers: { commit: h.commitFn },
    }),
  };
});

import { BosonEscrowAdapter, type BosonMerchantConfig } from "../src/adapter.ts";

const SELLER = "0x1111111111111111111111111111111111111111";
const BUYER = "0x2222222222222222222222222222222222222222";
const BUYER2 = "0x3333333333333333333333333333333333333333";
const ESCROW = "0x7de418a7ce94debd057c34ebac232e7027634ade";
const ASSET = "0x036cbd53842c5426634e7929541ec2318f3dcf7e";
const FACILITATOR = "https://facilitator.example.test";
const RPC = "https://base-sepolia-rpc.publicnode.com";
const HEX32 = "0x" + "ab".repeat(32);

function merchantConfig(over: Partial<Record<string, unknown>> = {}): MerchantConfig {
  return {
    network: "eip155:84532",
    chainId: 84532,
    escrow: ESCROW,
    sellerId: "42",
    disputeResolverId: "1",
    asset: ASSET,
    facilitatorUrl: FACILITATOR,
    signer: { address: SELLER, signTypedData: vi.fn(async () => HEX32 as `0x${string}`) },
    ...over,
  };
}

function requirements(amount: string, over: Partial<EscrowPaymentRequirements> = {}) {
  return {
    scheme: "escrow",
    network: "eip155:84532",
    asset: ASSET,
    amount,
    escrowAddress: ESCROW,
    recipientId: "42",
    maxTimeoutSeconds: 3600,
    offer: { fullOffer: { price: amount }, sellerSig: HEX32, creator: SELLER },
    tokenAuthStrategies: ["none"],
    actions: { next: [{ id: "boson-createOfferAndCommit", channels: ["facilitator"] }] },
    ...over,
  } as EscrowPaymentRequirements;
}

/** A structurally-valid escrow X-PAYMENT (real decodeXPaymentHeader parses it). */
function xPaymentHeader(buyer = BUYER): string {
  const payload = {
    x402Version: 1,
    scheme: "escrow",
    network: "eip155:84532",
    payload: {
      action: "boson-createOfferAndCommit",
      tokenAuthStrategy: "none",
      offerRef: { fullOffer: { price: "1" }, sellerSig: HEX32 },
      buyer,
      metaTx: {
        from: buyer,
        nonce: "1",
        functionName: "executeMetaTransaction",
        functionSignature: "0xdeadbeef",
        sig: { v: 27, r: HEX32, s: HEX32 },
      },
    },
  };
  return Buffer.from(JSON.stringify(payload), "utf-8").toString("base64");
}

function ctx(): RailRequestContext {
  return {
    trace_id: "trace_pl",
    idempotency_key: "co_1",
    merchant_id: "m1",
    site_id: "11111111-1111-1111-1111-111111111111",
    received_at: new Date().toISOString(),
  };
}

function makeAdapter() {
  return new BosonEscrowAdapter({
    facilitatorUrl: FACILITATOR,
    rpcUrl: RPC,
    exchangeReaderFactory: (_cfg: BosonMerchantConfig) => ({ read: async () => null }),
    mode: "development",
    now: () => Date.parse("2026-06-02T00:00:00.000Z"),
  });
}

function commitOk(exchangeId: string) {
  return {
    ok: true as const,
    status: 200,
    body: {
      nextActions: { exchangeId, exchangeState: "Committed" },
      txHash: `0xtx${exchangeId}`,
    },
  };
}

function commitFail() {
  return {
    ok: false as const,
    status: 402,
    body: { code: "INSUFFICIENT_FUNDS", reason: "buyer balance too low", details: {} },
  };
}

// ─── quote: N offers, one per line, bound to the cart total ────────────────────

describe("quotePerLine: options.line_items -> N seller-signed offers", () => {
  it("builds one offer per line at qty*unit_price and returns { per_line, lines }", async () => {
    h.buildReqFn.mockReset();
    h.buildReqFn.mockImplementation((input: Record<string, unknown>) =>
      requirements(String(input.amount)),
    );
    const res = await makeAdapter().quoteRequirements!({
      ctx: ctx(),
      merchant_config: merchantConfig(),
      amount: { amount: 2_000_000, currency: "USDC" },
      options: {
        line_items: [
          { line_index: 0, qty: 1, unit_price_atomic: "1000000", product: { name: "A" } },
          { line_index: 1, qty: 2, unit_price_atomic: "500000", product: { name: "B" } },
        ],
      },
    });
    expect(res.kind).toBe("ok");
    if (res.kind !== "ok") return;
    const reqs = res.value.requirements as {
      per_line: boolean;
      lines: Array<{ line_index: number }>;
    };
    expect(reqs.per_line).toBe(true);
    expect(reqs.lines.map((l) => l.line_index)).toEqual([0, 1]);
    // Each line's offer was signed at its own total: line 0 = 1*1e6, line 1 = 2*5e5.
    const amounts = h.buildReqFn.mock.calls.map((c) => (c[0] as { amount: string }).amount).sort();
    expect(amounts).toEqual(["1000000", "1000000"]);
  });

  it("rejects a cart whose per-line amounts do not sum to amount.amount", async () => {
    h.buildReqFn.mockReset();
    h.buildReqFn.mockImplementation((input: Record<string, unknown>) =>
      requirements(String(input.amount)),
    );
    const res = await makeAdapter().quoteRequirements!({
      ctx: ctx(),
      merchant_config: merchantConfig(),
      amount: { amount: 999, currency: "USDC" }, // != 1000000 + 1000000
      options: {
        line_items: [
          { line_index: 0, qty: 1, unit_price_atomic: "1000000" },
          { line_index: 1, qty: 1, unit_price_atomic: "1000000" },
        ],
      },
    });
    expect(res.kind).toBe("error");
  });

  it("rejects malformed line_items (present but not per-line-shaped)", async () => {
    const res = await makeAdapter().quoteRequirements!({
      ctx: ctx(),
      merchant_config: merchantConfig(),
      amount: { amount: 1_000_000, currency: "USDC" },
      options: { line_items: [{ line_index: 0, qty: 0, unit_price_atomic: "1000000" }] }, // qty <= 0
    });
    expect(res.kind).toBe("error");
  });
});

// ─── verify: gate each line, bind the sum, one buyer, encode the handle ────────

function verifyInput(
  lines: Array<{ line_index: number; x_payment: string; requirements: EscrowPaymentRequirements }>,
  cartTotal: number,
): VerifyAuthorityInput {
  return {
    ctx: ctx(),
    merchant_config: merchantConfig(),
    authority: { lines },
    amount: { amount: cartTotal, currency: "USDC" },
  };
}

describe("verifyPerLine: gate + validate each line's X-PAYMENT", () => {
  it("accepts N valid lines, binds the sum, and surfaces the single buyer", async () => {
    h.validateFn.mockReset();
    h.validateFn.mockResolvedValue({ ok: true });
    const res = await makeAdapter().verifyAuthority(
      verifyInput(
        [
          {
            line_index: 0,
            x_payment: xPaymentHeader(BUYER),
            requirements: requirements("1000000"),
          },
          {
            line_index: 1,
            x_payment: xPaymentHeader(BUYER),
            requirements: requirements("1000000"),
          },
        ],
        2_000_000,
      ),
    );
    expect(res.kind).toBe("ok");
    if (res.kind !== "ok") return;
    expect(res.value.authority_handle.startsWith("bosonv1:")).toBe(true);
    expect(res.value.payer?.toLowerCase()).toBe(BUYER.toLowerCase());
  });

  it("rejects a cart whose per-line amounts do not sum to the cart total", async () => {
    h.validateFn.mockReset();
    h.validateFn.mockResolvedValue({ ok: true });
    const res = await makeAdapter().verifyAuthority(
      verifyInput(
        [
          {
            line_index: 0,
            x_payment: xPaymentHeader(BUYER),
            requirements: requirements("1000000"),
          },
          {
            line_index: 1,
            x_payment: xPaymentHeader(BUYER),
            requirements: requirements("1000000"),
          },
        ],
        5, // != 2000000
      ),
    );
    expect(res.kind).toBe("error");
  });

  it("rejects a cart committed by two different buyers", async () => {
    h.validateFn.mockReset();
    h.validateFn.mockResolvedValue({ ok: true });
    const res = await makeAdapter().verifyAuthority(
      verifyInput(
        [
          {
            line_index: 0,
            x_payment: xPaymentHeader(BUYER),
            requirements: requirements("1000000"),
          },
          {
            line_index: 1,
            x_payment: xPaymentHeader(BUYER2),
            requirements: requirements("1000000"),
          },
        ],
        2_000_000,
      ),
    );
    expect(res.kind).toBe("error");
  });

  it("rejects a line whose offer was not signed by this merchant's seller", async () => {
    h.validateFn.mockReset();
    h.validateFn.mockResolvedValue({ ok: true });
    const bad = requirements("2000000", {
      offer: { fullOffer: { price: "2000000" }, sellerSig: HEX32, creator: BUYER2 },
    } as Partial<EscrowPaymentRequirements>);
    const res = await makeAdapter().verifyAuthority(
      verifyInput(
        [{ line_index: 0, x_payment: xPaymentHeader(BUYER), requirements: bad }],
        2_000_000,
      ),
    );
    expect(res.kind).toBe("error");
  });

  // MONEY-PATH: the seller signature covers offer.fullOffer (the escrowed `price`),
  // NOT the sibling requirements.amount. A buyer who echoes a real $1 seller-signed
  // offer under amount:"$100" would, without the amount->price bind, pass the
  // (self-consistent) gate and sum to a $100 cart while $1 sits in escrow. Verify
  // must reject the diverging label.
  it("rejects a line whose amount label exceeds the seller-signed offer price", async () => {
    h.validateFn.mockReset();
    h.validateFn.mockResolvedValue({ ok: true });
    // amount label = 100_000_000 ($100), but the seller-signed price = 1_000_000 ($1).
    const inflated = requirements("100000000", {
      offer: { fullOffer: { price: "1000000" }, sellerSig: HEX32, creator: SELLER },
    } as Partial<EscrowPaymentRequirements>);
    const res = await makeAdapter().verifyAuthority(
      // cartTotal matches the LABEL, so ONLY the amount->price bind can catch this
      // (a sum-over-label check would pass). Proves the vuln is closed at the bind.
      verifyInput(
        [{ line_index: 0, x_payment: xPaymentHeader(BUYER), requirements: inflated }],
        100000000,
      ),
    );
    expect(res.kind).toBe("error");
    if (res.kind === "error") {
      expect(res.message).toContain("seller-signed offer price");
    }
  });

  // The inverse: a line whose amount label is LOWER than the signed price is also a
  // divergence and must be rejected (an under-labeled line could otherwise let a
  // cart appear to bind to a smaller total than is escrowed).
  it("rejects a line whose amount label is lower than the seller-signed offer price", async () => {
    h.validateFn.mockReset();
    h.validateFn.mockResolvedValue({ ok: true });
    const under = requirements("1", {
      offer: { fullOffer: { price: "1000000" }, sellerSig: HEX32, creator: SELLER },
    } as Partial<EscrowPaymentRequirements>);
    const res = await makeAdapter().verifyAuthority(
      verifyInput([{ line_index: 0, x_payment: xPaymentHeader(BUYER), requirements: under }], 1),
    );
    expect(res.kind).toBe("error");
  });

  // ROBUSTNESS: fullOffer is z.record(z.unknown()), so a hostile buyer can echo a
  // NUMERIC price like 1e21. String(1e21) is "1e+21", which BigInt() throws on. The
  // helper must reject an unsafe-integer double gracefully (returns an error result),
  // NOT let the throw propagate as an unhandled 500 out of verifyAuthority.
  it("rejects a hostile numeric offer price (1e21) gracefully, without throwing", async () => {
    h.validateFn.mockReset();
    h.validateFn.mockResolvedValue({ ok: true });
    const hostile = requirements("1000000", {
      offer: { fullOffer: { price: 1e21 }, sellerSig: HEX32, creator: SELLER },
    } as unknown as Partial<EscrowPaymentRequirements>);
    // The await resolving at all (rather than rejecting) is half the assertion.
    const res = await makeAdapter().verifyAuthority(
      verifyInput(
        [{ line_index: 0, x_payment: xPaymentHeader(BUYER), requirements: hostile }],
        1000000,
      ),
    );
    expect(res.kind).toBe("error");
  });
});

// ─── reserve: N concurrent commits, partial commit is a valid mid-state ────────

async function handleFor(
  lines: Array<{ line_index: number; x_payment: string; requirements: EscrowPaymentRequirements }>,
  cartTotal: number,
): Promise<string> {
  h.validateFn.mockReset();
  h.validateFn.mockResolvedValue({ ok: true });
  const res = await makeAdapter().verifyAuthority(verifyInput(lines, cartTotal));
  if (res.kind !== "ok") throw new Error(`verify failed: ${JSON.stringify(res)}`);
  return res.value.authority_handle;
}

function reserveInput(handle: string, cartTotal: number): ReserveAuthorityInput {
  return {
    ctx: ctx(),
    merchant_config: merchantConfig(),
    authority_handle: handle,
    amount: { amount: cartTotal, currency: "USDC" },
  };
}

describe("reservePerLine: commit each line concurrently", () => {
  const twoLines = () => [
    { line_index: 0, x_payment: xPaymentHeader(BUYER), requirements: requirements("1000000") },
    { line_index: 1, x_payment: xPaymentHeader(BUYER), requirements: requirements("1000000") },
  ];

  it("commits all lines -> reservation_active true, one escrow_line per line", async () => {
    const handle = await handleFor(twoLines(), 2_000_000);
    let n = 0;
    h.commitFn.mockReset();
    h.commitFn.mockImplementation(async () => commitOk(`ex${n++}`));
    const res = await makeAdapter().reserveAuthority(reserveInput(handle, 2_000_000));
    expect(res.kind).toBe("ok");
    if (res.kind !== "ok") return;
    expect(res.value.reservation_active).toBe(true);
    const rm = res.value.rail_metadata as {
      committed_count: number;
      escrow_lines: Array<{
        line_index: number;
        status: string;
        exchange_id?: string;
        amount?: string;
      }>;
    };
    expect(rm.committed_count).toBe(2);
    expect(rm.escrow_lines.map((l) => l.status)).toEqual(["committed", "committed"]);
    expect(rm.escrow_lines.every((l) => typeof l.exchange_id === "string")).toBe(true);
    // Each escrow_line carries its sealed per-line amount so the Terminal persists
    // the boson_exchange_lines row (and later captures) at the signed value, never a
    // re-derived one.
    expect(rm.escrow_lines.every((l) => l.amount === "1000000")).toBe(true);
  });

  it("partial commit: one line lands, one fails -> reservation_active false, mixed escrow_lines", async () => {
    const handle = await handleFor(twoLines(), 2_000_000);
    let call = 0;
    h.commitFn.mockReset();
    h.commitFn.mockImplementation(async () => (call++ === 0 ? commitOk("ex0") : commitFail()));
    const res = await makeAdapter().reserveAuthority(reserveInput(handle, 2_000_000));
    expect(res.kind).toBe("ok");
    if (res.kind !== "ok") return;
    // A partial commit is NOT an error: the landed line is recorded, the failed
    // line stays retryable, and reservation_active is false so the Terminal retries.
    expect(res.value.reservation_active).toBe(false);
    const rm = res.value.rail_metadata as {
      committed_count: number;
      escrow_lines: Array<{ line_index: number; status: string }>;
    };
    expect(rm.committed_count).toBe(1);
    const byIndex = Object.fromEntries(rm.escrow_lines.map((l) => [l.line_index, l.status]));
    expect(byIndex[0]).toBe("committed");
    expect(byIndex[1]).toBe("failed");
  });
});
