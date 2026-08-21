// Deno-side tests for `@facet-llc/sdk-deno`. Mirror the Node tests in
// scope; the underlying SDK code is line-for-line equivalent to its Node
// twin, so anything that diverges in behavior here should also diverge
// in `packages/sdk-node/test/discovery.test.ts`.

import { assert, assertEquals, assertInstanceOf, assertRejects } from "@std/assert";
import {
  CapabilityMismatchError,
  clearAgentsTxtCache,
  discoverAndConnect,
  FetchError,
  fetchAgentsTxt,
  InvalidManifestError,
  NoManifestError,
  SUPPORTED_FACET_VERSIONS,
  UnsupportedVersionError,
} from "../src/mod.ts";

interface ScriptedResponse {
  status?: number;
  body?: string;
  headers?: Record<string, string>;
  throws?: unknown;
}

function fakeFetch(script: (url: string) => ScriptedResponse | Promise<ScriptedResponse>): {
  fetch: typeof fetch;
  calls: string[];
} {
  const calls: string[] = [];
  const fetchImpl = (async (input: RequestInfo | URL) => {
    const url = typeof input === "string" ? input : input instanceof URL ? input.href : input.url;
    calls.push(url);
    const resp = await script(url);
    if (resp.throws !== undefined) throw resp.throws;
    return new Response(resp.body ?? "", {
      status: resp.status ?? 200,
      headers: resp.headers ?? {},
    });
  }) as unknown as typeof fetch;
  return { fetch: fetchImpl, calls };
}

const VALID_V11 = [
  "Facet-Version: 1.1",
  "Terminal: https://api.merchant.example.com/v1",
  "KYA-Issuers: https://issuer.skyfire.xyz",
  "Capabilities: catalog, paywalled-content",
  "",
].join("\n");

Deno.test("fetchAgentsTxt — returns parsed manifest on 200 + valid v1.1", async () => {
  clearAgentsTxtCache();
  const { fetch } = fakeFetch(() => ({ status: 200, body: VALID_V11 }));
  const manifest = await fetchAgentsTxt("merchant.example.com", { fetch });
  assertEquals(manifest.facetVersion, "1.1");
  assertEquals(manifest.terminal, "https://api.merchant.example.com/v1");
  assertEquals(manifest.kyaIssuers, ["https://issuer.skyfire.xyz"]);
  assertEquals(manifest.capabilities, ["catalog", "paywalled-content"]);
});

Deno.test("fetchAgentsTxt — requests /.well-known/agents.txt via https", async () => {
  clearAgentsTxtCache();
  const { fetch, calls } = fakeFetch(() => ({ status: 200, body: VALID_V11 }));
  await fetchAgentsTxt("merchant.example.com", { fetch });
  assertEquals(calls, ["https://merchant.example.com/.well-known/agents.txt"]);
});

Deno.test("fetchAgentsTxt — accepts a fully-qualified origin", async () => {
  clearAgentsTxtCache();
  const { fetch, calls } = fakeFetch(() => ({ status: 200, body: VALID_V11 }));
  await fetchAgentsTxt("https://merchant.example.com:8443", { fetch });
  assertEquals(calls, ["https://merchant.example.com:8443/.well-known/agents.txt"]);
});

Deno.test("fetchAgentsTxt — NoManifestError on HTTP 404", async () => {
  clearAgentsTxtCache();
  const { fetch } = fakeFetch(() => ({ status: 404, body: "not found" }));
  const err = await assertRejects(
    () => fetchAgentsTxt("merchant.example.com", { fetch }),
    NoManifestError,
  );
  assertEquals((err as NoManifestError).domain, "merchant.example.com");
  assertEquals((err as NoManifestError).status, 404);
});

Deno.test("fetchAgentsTxt — FetchError on other non-2xx (e.g. 500)", async () => {
  clearAgentsTxtCache();
  const { fetch } = fakeFetch(() => ({ status: 500, body: "kaboom" }));
  await assertRejects(() => fetchAgentsTxt("merchant.example.com", { fetch }), FetchError);
});

Deno.test("fetchAgentsTxt — FetchError when network layer fails", async () => {
  clearAgentsTxtCache();
  const { fetch } = fakeFetch(() => ({ throws: new Error("ECONNREFUSED") }));
  const err = await assertRejects(
    () => fetchAgentsTxt("merchant.example.com", { fetch }),
    FetchError,
  );
  assertInstanceOf((err as FetchError).cause, Error);
});

Deno.test("fetchAgentsTxt — InvalidManifestError on malformed body", async () => {
  clearAgentsTxtCache();
  const malformed = "this is not\nan agents.txt\n";
  const { fetch } = fakeFetch(() => ({ status: 200, body: malformed }));
  await assertRejects(
    () => fetchAgentsTxt("merchant.example.com", { fetch }),
    InvalidManifestError,
  );
});

Deno.test("fetchAgentsTxt — UnsupportedVersionError on Facet-Version: 0.1", async () => {
  clearAgentsTxtCache();
  const body = [
    "Facet-Version: 0.1",
    "Terminal: https://api.merchant.example.com/v1",
    "KYA-Issuers: https://issuer.skyfire.xyz",
    "",
  ].join("\n");
  const { fetch } = fakeFetch(() => ({ status: 200, body }));
  const err = await assertRejects(
    () => fetchAgentsTxt("merchant.example.com", { fetch }),
    UnsupportedVersionError,
  );
  assertEquals((err as UnsupportedVersionError).facetVersion, "0.1");
  assertEquals((err as UnsupportedVersionError).supported, SUPPORTED_FACET_VERSIONS);
});

Deno.test("fetchAgentsTxt — accepts all supported versions (0.2 + 1.0 + 1.1 + 1.2)", async () => {
  for (const v of SUPPORTED_FACET_VERSIONS) {
    clearAgentsTxtCache();
    const body = [
      `Facet-Version: ${v}`,
      "Terminal: https://api.merchant.example.com/v1",
      "KYA-Issuers: https://issuer.skyfire.xyz",
      "",
    ].join("\n");
    const { fetch } = fakeFetch(() => ({ status: 200, body }));
    const manifest = await fetchAgentsTxt(`merchant-${v}.example.com`, {
      fetch,
    });
    assertEquals(manifest.facetVersion, v);
  }
});

Deno.test("fetchAgentsTxt — caches by Cache-Control: max-age", async () => {
  clearAgentsTxtCache();
  let hits = 0;
  const { fetch } = fakeFetch(() => {
    hits += 1;
    return {
      status: 200,
      body: VALID_V11,
      headers: { "cache-control": "public, max-age=600" },
    };
  });
  const t0 = 1_000_000;
  await fetchAgentsTxt("merchant.example.com", { fetch, now: () => t0 });
  assertEquals(hits, 1);
  await fetchAgentsTxt("merchant.example.com", {
    fetch,
    now: () => t0 + 599_000,
  });
  assertEquals(hits, 1);
  await fetchAgentsTxt("merchant.example.com", {
    fetch,
    now: () => t0 + 601_000,
  });
  assertEquals(hits, 2);
});

Deno.test("fetchAgentsTxt — falls back to opts.ttlMs when Cache-Control absent", async () => {
  clearAgentsTxtCache();
  let hits = 0;
  const { fetch } = fakeFetch(() => {
    hits += 1;
    return { status: 200, body: VALID_V11 };
  });
  const t0 = 2_000_000;
  await fetchAgentsTxt("merchant.example.com", {
    fetch,
    ttlMs: 60_000,
    now: () => t0,
  });
  await fetchAgentsTxt("merchant.example.com", {
    fetch,
    ttlMs: 60_000,
    now: () => t0 + 30_000,
  });
  assertEquals(hits, 1);
  await fetchAgentsTxt("merchant.example.com", {
    fetch,
    ttlMs: 60_000,
    now: () => t0 + 70_000,
  });
  assertEquals(hits, 2);
});

Deno.test("fetchAgentsTxt — Cache-Control: no-store disables caching", async () => {
  clearAgentsTxtCache();
  let hits = 0;
  const { fetch } = fakeFetch(() => {
    hits += 1;
    return {
      status: 200,
      body: VALID_V11,
      headers: { "cache-control": "no-store" },
    };
  });
  await fetchAgentsTxt("merchant.example.com", { fetch });
  await fetchAgentsTxt("merchant.example.com", { fetch });
  assertEquals(hits, 2);
});

Deno.test("fetchAgentsTxt — noCache forces a re-fetch", async () => {
  clearAgentsTxtCache();
  let hits = 0;
  const { fetch } = fakeFetch(() => {
    hits += 1;
    return { status: 200, body: VALID_V11 };
  });
  await fetchAgentsTxt("merchant.example.com", { fetch });
  await fetchAgentsTxt("merchant.example.com", { fetch, noCache: true });
  assertEquals(hits, 2);
});

Deno.test("discoverAndConnect — returns a TerminalClient that calls Terminal URL", async () => {
  clearAgentsTxtCache();
  const calls: string[] = [];
  const fetchImpl = (async (input: RequestInfo | URL) => {
    const url = typeof input === "string" ? input : input instanceof URL ? input.href : input.url;
    calls.push(url);
    if (url.endsWith("/.well-known/agents.txt")) {
      return new Response(VALID_V11, { status: 200 });
    }
    return new Response(JSON.stringify({ tools: [], webhook_events: [] }), {
      status: 200,
      headers: { "content-type": "application/json" },
    });
  }) as unknown as typeof fetch;

  const client = await discoverAndConnect("merchant.example.com", {
    fetch: fetchImpl,
  });
  await client.capabilities();
  assert(
    calls.some((u) => u.startsWith("https://api.merchant.example.com/v1/v1/capabilities")),
    `expected a /v1/capabilities call, saw: ${calls.join(", ")}`,
  );
});

Deno.test("discoverAndConnect — passes capability check when caps match", async () => {
  clearAgentsTxtCache();
  const fetchImpl = (async () =>
    new Response(VALID_V11, { status: 200 })) as unknown as typeof fetch;
  const client = await discoverAndConnect("merchant.example.com", {
    fetch: fetchImpl,
    capabilityCheck: ["catalog"],
  });
  assert(client !== undefined);
});

Deno.test("discoverAndConnect — CapabilityMismatchError on missing cap", async () => {
  clearAgentsTxtCache();
  const fetchImpl = (async () =>
    new Response(VALID_V11, { status: 200 })) as unknown as typeof fetch;
  const err = await assertRejects(
    () =>
      discoverAndConnect("merchant.example.com", {
        fetch: fetchImpl,
        capabilityCheck: ["catalog", "auction"],
      }),
    CapabilityMismatchError,
  );
  assertEquals((err as CapabilityMismatchError).missing, ["auction"]);
});

Deno.test("discoverAndConnect — propagates NoManifestError up", async () => {
  clearAgentsTxtCache();
  const fetchImpl = (async () =>
    new Response("not found", { status: 404 })) as unknown as typeof fetch;
  await assertRejects(
    () => discoverAndConnect("merchant.example.com", { fetch: fetchImpl }),
    NoManifestError,
  );
});

// ── happy path against a local HTTP fixture server ────────────────────────

Deno.test("discoverAndConnect — happy path against local HTTP fixture server", async () => {
  clearAgentsTxtCache();

  const calls: string[] = [];

  // Latched once Deno.serve binds — `originPromise` resolves to the bound
  // origin so the manifest body can reference `${origin}/v1` (the test
  // pretends the same origin hosts both the manifest and the Terminal).
  let resolveOrigin!: (origin: string) => void;
  const originPromise = new Promise<string>((resolve) => {
    resolveOrigin = resolve;
  });

  const server = Deno.serve(
    {
      hostname: "127.0.0.1",
      port: 0,
      onListen: ({ hostname, port }) => {
        resolveOrigin(`http://${hostname}:${port}`);
      },
    },
    async (req) => {
      const url = new URL(req.url);
      calls.push(url.pathname);
      if (url.pathname === "/.well-known/agents.txt") {
        const origin = await originPromise;
        const body = [
          "Facet-Version: 1.1",
          `Terminal: ${origin}/v1`,
          "KYA-Issuers: https://issuer.skyfire.xyz",
          "Capabilities: catalog",
          "",
        ].join("\n");
        return new Response(body, {
          status: 200,
          headers: {
            "content-type": "text/plain; charset=utf-8",
            "cache-control": "public, max-age=300",
          },
        });
      }
      if (url.pathname === "/v1/v1/capabilities") {
        return new Response(JSON.stringify({ tools: ["search"], webhook_events: [] }), {
          status: 200,
          headers: { "content-type": "application/json" },
        });
      }
      return new Response("not found", { status: 404 });
    },
  );

  try {
    const origin = await originPromise;
    const client = await discoverAndConnect(origin, {
      capabilityCheck: ["catalog"],
    });
    const caps = await client.capabilities();
    assertEquals(caps.tools, ["search"]);
    assert(calls.includes("/.well-known/agents.txt"));
    assert(calls.includes("/v1/v1/capabilities"));
  } finally {
    await server.shutdown();
  }
});

// ── v1.2 (regression: the live Terminal emits 1.2) ─────────────────────────

Deno.test("fetchAgentsTxt — SUPPORTED_FACET_VERSIONS includes 1.2", () => {
  assert((SUPPORTED_FACET_VERSIONS as readonly string[]).includes("1.2"));
});

Deno.test("fetchAgentsTxt — accepts Facet-Version: 1.2 (what the Terminal emits)", async () => {
  clearAgentsTxtCache();
  const body = [
    "Facet-Version: 1.2",
    "Terminal: https://api.merchant.example.com/v1",
    "KYA-Issuers: https://issuer.skyfire.xyz",
    "OpenAPI: https://api.merchant.example.com/v1/openapi.json",
    "",
  ].join("\n");
  const { fetch } = fakeFetch(() => ({ status: 200, body }));
  const manifest = await fetchAgentsTxt("merchant.example.com", { fetch });
  assertEquals(manifest.facetVersion, "1.2");
  assertEquals(manifest.openApiUrl, "https://api.merchant.example.com/v1/openapi.json");
});

// ── storefront discovery-pointer fallback (404 on /.well-known/) ───────────

const FALLBACK_TERMINAL_AGENTS_TXT = "https://t.facet.llc/.well-known/agents.txt";
const FALLBACK_MANIFEST = [
  "Facet-Version: 1.2",
  "Terminal: https://t.facet.llc/v1",
  "KYA-Issuers: https://issuer.skyfire.xyz",
  "",
].join("\n");

// shop 404s /.well-known/agents.txt; its root returns `rootResp`; the
// pointed-at Terminal serves the manifest.
function storefront(rootResp: ScriptedResponse) {
  return fakeFetch((url) => {
    if (url === "https://shop.example.com/.well-known/agents.txt") return { status: 404, body: "" };
    if (url === "https://shop.example.com/") return rootResp;
    if (url === FALLBACK_TERMINAL_AGENTS_TXT) return { status: 200, body: FALLBACK_MANIFEST };
    return { status: 404, body: "" };
  });
}

Deno.test('fallback — resolves via <link rel="agents"> in storefront HTML', async () => {
  clearAgentsTxtCache();
  const { fetch, calls } = storefront({
    status: 200,
    headers: { "content-type": "text/html; charset=utf-8" },
    body: `<html><head><link rel="agents" href="${FALLBACK_TERMINAL_AGENTS_TXT}"></head><body>shop</body></html>`,
  });
  const m = await fetchAgentsTxt("shop.example.com", { fetch });
  assertEquals(m.facetVersion, "1.2");
  assertEquals(m.terminal, "https://t.facet.llc/v1");
  assertEquals(calls, [
    "https://shop.example.com/.well-known/agents.txt",
    "https://shop.example.com/",
    FALLBACK_TERMINAL_AGENTS_TXT,
  ]);
});

Deno.test('fallback — resolves via <meta name="agents-txt"> (order swapped)', async () => {
  clearAgentsTxtCache();
  const { fetch } = storefront({
    status: 200,
    headers: { "content-type": "text/html" },
    body: `<head><meta content="${FALLBACK_TERMINAL_AGENTS_TXT}" name="agents-txt"/></head>`,
  });
  const m = await fetchAgentsTxt("shop.example.com", { fetch });
  assertEquals(m.terminal, "https://t.facet.llc/v1");
});

Deno.test('fallback — resolves via HTTP Link: rel="agents" header', async () => {
  clearAgentsTxtCache();
  const { fetch } = storefront({
    status: 200,
    headers: {
      link: `<${FALLBACK_TERMINAL_AGENTS_TXT}>; rel="agents"`,
      "content-type": "text/html",
    },
    body: "<html></html>",
  });
  const m = await fetchAgentsTxt("shop.example.com", { fetch });
  assertEquals(m.terminal, "https://t.facet.llc/v1");
});

Deno.test("fallback — decodes &amp; in the pointer href", async () => {
  clearAgentsTxtCache();
  const withQuery = "https://t.facet.llc/.well-known/agents.txt?a=1&b=2";
  const { fetch } = fakeFetch((url) => {
    if (url === "https://shop.example.com/.well-known/agents.txt") return { status: 404, body: "" };
    if (url === "https://shop.example.com/") {
      return {
        status: 200,
        headers: { "content-type": "text/html" },
        body: `<link rel="agents" href="https://t.facet.llc/.well-known/agents.txt?a=1&amp;b=2">`,
      };
    }
    if (url === withQuery) return { status: 200, body: FALLBACK_MANIFEST };
    return { status: 404, body: "" };
  });
  const m = await fetchAgentsTxt("shop.example.com", { fetch });
  assertEquals(m.terminal, "https://t.facet.llc/v1");
});

Deno.test("fallback — NoManifestError when storefront has no pointer", async () => {
  clearAgentsTxtCache();
  const { fetch } = storefront({
    status: 200,
    headers: { "content-type": "text/html" },
    body: "<html><head></head><body>just a shop</body></html>",
  });
  await assertRejects(() => fetchAgentsTxt("shop.example.com", { fetch }), NoManifestError);
});

Deno.test("fallback — ignores a non-https pointer (downgrade guard)", async () => {
  clearAgentsTxtCache();
  const { fetch } = storefront({
    status: 200,
    headers: { "content-type": "text/html" },
    body: `<link rel="agents" href="http://t.facet.llc/.well-known/agents.txt">`,
  });
  await assertRejects(() => fetchAgentsTxt("shop.example.com", { fetch }), NoManifestError);
});

Deno.test("fallback — ignores a non-HTML storefront root", async () => {
  clearAgentsTxtCache();
  const { fetch } = storefront({
    status: 200,
    headers: { "content-type": "application/json" },
    body: "{}",
  });
  await assertRejects(() => fetchAgentsTxt("shop.example.com", { fetch }), NoManifestError);
});

Deno.test("fallback — propagates NoManifestError when the pointed-at manifest 404s", async () => {
  clearAgentsTxtCache();
  const { fetch } = fakeFetch((url) => {
    if (url === "https://shop.example.com/.well-known/agents.txt") return { status: 404, body: "" };
    if (url === "https://shop.example.com/") {
      return {
        status: 200,
        headers: { "content-type": "text/html" },
        body: `<link rel="agents" href="${FALLBACK_TERMINAL_AGENTS_TXT}">`,
      };
    }
    return { status: 404, body: "" };
  });
  await assertRejects(() => fetchAgentsTxt("shop.example.com", { fetch }), NoManifestError);
});
