import { describe, expect, it } from "vitest";
import { keccak256, toBytes } from "viem";

import {
  buildLineOfferMetadata,
  buildOfferMetadata,
  canonicalStringify,
  decodeMetadataPath,
  encodeMetadataPath,
  metadataParamFromUrl,
} from "../src/metadata.ts";

const BASE = "https://acme.facet.llc";
const ASSET = "0x036cbd53842c5426634e7929541ec2318f3dcf7e";
const NETWORK = "eip155:84532";

function build(over: Parameters<typeof buildOfferMetadata>[0] | Record<string, unknown> = {}) {
  return buildOfferMetadata({
    product: undefined,
    exchangeToken: ASSET,
    network: NETWORK,
    metadataBaseUri: BASE,
    ...(over as object),
  });
}

describe("buildOfferMetadata — BPIP-1 BASE offer metadata", () => {
  it("emits a valid BPIP-1 BASE document with a resolvable URI and real keccak hash", () => {
    const { metadata, metadataUri, metadataHash } = build({
      product: {
        id: "p1",
        name: "Acme Serum",
        description: "Brightening serum",
        category: "skincare",
        origin: "US",
        htsCode: "3304.99",
        allergens: ["none"],
        tags: ["vegan"],
      },
    });
    expect(metadata.type).toBe("BASE");
    expect(metadata.name).toBe("Acme Serum");
    expect(metadata.schemaUrl).toMatch(/^https:\/\//);
    // Product facts surface as BPIP-1 attributes.
    const traits = Object.fromEntries(metadata.attributes.map((a) => [a.traitType, a.value]));
    expect(traits["Product ID"]).toBe("p1");
    expect(traits["Country of Origin"]).toBe("US");
    expect(traits["HTS Code"]).toBe("3304.99");
    expect(traits["Exchange Token"]).toBe(ASSET);
    // URI is a resolvable HTTPS route; hash is a real keccak-256.
    expect(metadataUri).toMatch(/^https:\/\/acme\.facet\.llc\/v1\/boson\/offer-metadata\?d=/);
    expect(metadataUri).not.toContain("ipfs://");
    expect(metadataHash).toMatch(/^0x[0-9a-f]{64}$/);
  });

  it("fills protocol-safe defaults for a catalog-less quote (still real, fully populated)", () => {
    const { metadata, metadataHash } = build();
    expect(metadata.name).toBe("Facet agent-commerce order");
    expect(metadata.description.length).toBeGreaterThan(0);
    expect(metadataHash).toMatch(/^0x[0-9a-f]{64}$/);
  });

  it("is deterministic without a nonce: identical inputs → identical hash + URI", () => {
    const a = build({ product: { name: "X" } });
    const b = build({ product: { name: "X" } });
    expect(a.metadataHash).toBe(b.metadataHash);
    expect(a.metadataUri).toBe(b.metadataUri);
  });

  it("is unique with a nonce: same product, different nonce → different hash (anti-collision)", () => {
    const a = build({ product: { name: "X" }, nonce: "nonce-1" });
    const b = build({ product: { name: "X" }, nonce: "nonce-2" });
    expect(a.metadataHash).not.toBe(b.metadataHash);
    expect(a.metadataUri).not.toBe(b.metadataUri);
    // The nonce rides the document, not the human-facing traits.
    expect(a.metadata.offerNonce).toBe("nonce-1");
    expect(a.metadata.attributes.some((t) => /nonce/i.test(t.traitType))).toBe(false);
  });

  it("the on-chain hash commits to the exact served bytes (resolver round-trip)", () => {
    const { metadataUri, metadataHash, canonicalJson } = build({
      product: { name: "Round Trip", description: "verify me" },
      nonce: "abc",
    });
    // A resolver fetches the URI's `d` param and decodes it.
    const segment = metadataParamFromUrl(metadataUri)!;
    const decoded = decodeMetadataPath(segment);
    expect(decoded).not.toBeNull();
    expect(decoded!.canonicalJson).toBe(canonicalJson);
    // Re-hashing the served bytes reproduces the on-chain metadataHash.
    expect(keccak256(toBytes(decoded!.canonicalJson))).toBe(metadataHash);
  });

  it("encodeMetadataPath/decodeMetadataPath round-trips and rejects garbage", () => {
    const json = canonicalStringify({ type: "BASE", name: "ok", attributes: [] });
    const seg = encodeMetadataPath(json);
    const back = decodeMetadataPath(seg);
    expect(back!.metadata.name).toBe("ok");
    // Not base64 / not JSON / not BASE-typed → null (route answers 404, never throws).
    expect(decodeMetadataPath("!!!not-base64!!!")).toBeNull();
    expect(decodeMetadataPath(encodeMetadataPath("not json"))).toBeNull();
    expect(decodeMetadataPath(encodeMetadataPath(JSON.stringify({ type: "NOPE" })))).toBeNull();
  });
});

const COMMON = { exchangeToken: ASSET, network: NETWORK, metadataBaseUri: BASE };

describe("buildLineOfferMetadata: per-line offers (S2)", () => {
  it("threads the line's own product into the offer", () => {
    const built = buildLineOfferMetadata(
      { product: { name: "Line A SKU", id: "sku-a" }, lineNonce: "co_1:0" },
      COMMON,
    );
    expect(built.metadata.name).toBe("Line A SKU");
    const traits = Object.fromEntries(built.metadata.attributes.map((a) => [a.traitType, a.value]));
    expect(traits["Product ID"]).toBe("sku-a");
  });

  it("uses the line nonce as the offerNonce (on the document, not the traits)", () => {
    const built = buildLineOfferMetadata({ product: { name: "X" }, lineNonce: "co_1:3" }, COMMON);
    expect(built.metadata.offerNonce).toBe("co_1:3");
    expect(built.metadata.attributes.some((t) => /nonce/i.test(t.traitType))).toBe(false);
  });

  it("same product + different line nonce produce DISTINCT offers (no OfferSoldOut collision)", () => {
    const l0 = buildLineOfferMetadata(
      { product: { name: "Same SKU" }, lineNonce: "co_1:0" },
      COMMON,
    );
    const l1 = buildLineOfferMetadata(
      { product: { name: "Same SKU" }, lineNonce: "co_1:1" },
      COMMON,
    );
    expect(l0.metadataHash).not.toBe(l1.metadataHash);
    expect(l0.metadataUri).not.toBe(l1.metadataUri);
  });

  it("is deterministic per line: the same line rebuilt is byte-identical (idempotent retry)", () => {
    const line = { product: { name: "Retry me", id: "sku-r" }, lineNonce: "co_9:2" };
    const first = buildLineOfferMetadata(line, COMMON);
    const again = buildLineOfferMetadata(line, COMMON);
    expect(first.metadataHash).toBe(again.metadataHash);
    expect(first.metadataUri).toBe(again.metadataUri);
    expect(first.canonicalJson).toBe(again.canonicalJson);
  });

  it("equals buildOfferMetadata with product + nonce (thin wrapper, no drift)", () => {
    const line = { product: { name: "Parity", id: "p" }, lineNonce: "co_1:5" };
    const viaWrapper = buildLineOfferMetadata(line, COMMON);
    const viaDirect = buildOfferMetadata({
      ...COMMON,
      product: line.product,
      nonce: line.lineNonce,
    });
    expect(viaWrapper.metadataHash).toBe(viaDirect.metadataHash);
    expect(viaWrapper.canonicalJson).toBe(viaDirect.canonicalJson);
  });
});
