// Phase 8 smoke test — drives `createTerminalClient` against a real
// Facet Terminal from Deno. Runs in the `sdk-smoke-test` CI tier; the
// default `deno task test` scopes to offline unit tests.
//
// The smoke assertion is intentionally narrow: the SDK can dispatch a
// real request, parse the response envelope, and surface either the
// success body OR the structured `FacetErrorEnvelope` to the caller.
// We do NOT assert the Terminal returns 200 — the production Terminal
// classifies unauthenticated traffic as `PAYMENT_REQUIRED` (HTTP 402)
// per spec, which is itself a load-bearing signal that the SDK round-
// trip works end-to-end against the live wire contract.
//
// `FACET_SMOKE_BASE_URL` overrides the target.

import { assert, assertExists } from "@std/assert";
import { createTerminalClient } from "../src/mod.ts";

const SMOKE_BASE_URL = Deno.env.get("FACET_SMOKE_BASE_URL") ?? "https://api.facet.llc";

Deno.test("createTerminalClient builds a working typed client (network round-trip)", async () => {
  const client = createTerminalClient({ baseUrl: SMOKE_BASE_URL });
  const { data, error, response } = await client.GET("/v1/version");
  assertExists(response);
  assert(response.status >= 200 && response.status < 600, `unexpected status: ${response.status}`);
  if (response.ok) {
    assertExists(data);
  } else {
    assertExists(error);
    const envelope = error as { error?: { code?: string } } | undefined;
    assertExists(envelope?.error?.code);
  }
});

Deno.test("openapi-fetch headers + URL composition reach the live Terminal", async () => {
  const client = createTerminalClient({
    baseUrl: SMOKE_BASE_URL,
    userAgent: "@facet-llc/sdk-deno smoke-test",
  });
  const { response } = await client.GET("/v1/version");
  const traceId =
    response.headers.get("x-facet-trace-id") ?? response.headers.get("x-agent-trace-id");
  assertExists(traceId, "Terminal must set a trace-id header");
});
