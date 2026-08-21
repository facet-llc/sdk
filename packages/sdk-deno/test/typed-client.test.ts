// Deno-side unit tests for `createTerminalClient`. Mirrors
// `packages/sdk-node/test/typed-client.test.ts`. The smoke test
// against a live Facet Terminal lives in `smoke.test.ts` and runs in
// the `sdk-smoke-test` CI tier.

import { assertEquals, assertExists } from "@std/assert";
import { createTerminalClient } from "../src/mod.ts";

interface ScriptedResponse {
  status?: number;
  body: unknown;
  headers?: Record<string, string>;
}

function fakeFetch(script: (input: Request) => ScriptedResponse | Promise<ScriptedResponse>): {
  fetch: (input: Request) => Promise<Response>;
  calls: Request[];
} {
  const calls: Request[] = [];
  const fetchImpl = async (input: Request): Promise<Response> => {
    calls.push(input);
    const resp = await script(input);
    const body = typeof resp.body === "string" ? resp.body : JSON.stringify(resp.body);
    return new Response(body, {
      status: resp.status ?? 200,
      headers: {
        "content-type": "application/json",
        ...(resp.headers ?? {}),
      },
    });
  };
  return { fetch: fetchImpl, calls };
}

Deno.test(
  "createTerminalClient returns a typed openapi-fetch client; GET /v1/health resolves to a HealthResponse",
  async () => {
    const { fetch, calls } = fakeFetch(() => ({
      body: { status: "ok", timestamp: "2026-05-25T00:00:00Z" },
    }));
    const client = createTerminalClient({
      baseUrl: "https://terminal.facet.llc",
      fetch,
    });
    const { data, error } = await client.GET("/v1/health");
    assertEquals(error, undefined);
    assertExists(data);
    assertEquals(data?.status, "ok");
    assertEquals(data?.timestamp, "2026-05-25T00:00:00Z");
    assertEquals(calls.length, 1);
    assertEquals(calls[0]!.url, "https://terminal.facet.llc/v1/health");
    assertEquals(calls[0]!.method, "GET");
  },
);

Deno.test("createTerminalClient strips trailing slashes from baseUrl", async () => {
  const { fetch, calls } = fakeFetch(() => ({
    body: { status: "ok", timestamp: "2026-05-25T00:00:00Z" },
  }));
  const client = createTerminalClient({
    baseUrl: "https://terminal.facet.llc///",
    fetch,
  });
  await client.GET("/v1/health");
  assertEquals(calls[0]!.url, "https://terminal.facet.llc/v1/health");
});

Deno.test(
  "createTerminalClient sends Authorization: Bearer <token> when kyaToken is a string",
  async () => {
    const { fetch, calls } = fakeFetch(() => ({
      body: { status: "ok", timestamp: "2026-05-25T00:00:00Z" },
    }));
    const client = createTerminalClient({
      baseUrl: "https://terminal.facet.llc",
      kyaToken: "kya-test-token",
      fetch,
    });
    await client.GET("/v1/health");
    assertEquals(calls[0]!.headers.get("authorization"), "Bearer kya-test-token");
  },
);

Deno.test(
  "createTerminalClient resolves async kyaToken providers lazily on each request",
  async () => {
    const { fetch, calls } = fakeFetch(() => ({
      body: { status: "ok", timestamp: "2026-05-25T00:00:00Z" },
    }));
    let counter = 0;
    const client = createTerminalClient({
      baseUrl: "https://terminal.facet.llc",
      kyaToken: () => Promise.resolve(`kya-${++counter}`),
      fetch,
    });
    await client.GET("/v1/health");
    await client.GET("/v1/health");
    assertEquals(calls[0]!.headers.get("authorization"), "Bearer kya-1");
    assertEquals(calls[1]!.headers.get("authorization"), "Bearer kya-2");
  },
);

Deno.test("createTerminalClient threads custom headers + userAgent", async () => {
  const { fetch, calls } = fakeFetch(() => ({
    body: { status: "ok", timestamp: "2026-05-25T00:00:00Z" },
  }));
  const client = createTerminalClient({
    baseUrl: "https://terminal.facet.llc",
    headers: { "x-tenant-id": "acme" },
    userAgent: "test-agent/1.0",
    fetch,
  });
  await client.GET("/v1/health");
  assertEquals(calls[0]!.headers.get("x-tenant-id"), "acme");
  assertEquals(calls[0]!.headers.get("user-agent"), "test-agent/1.0");
});

Deno.test("createTerminalClient exposes the FacetErrorEnvelope on non-2xx as `error`", async () => {
  const { fetch } = fakeFetch(() => ({
    status: 401,
    body: {
      error: {
        code: "UNAUTHORIZED",
        message: "missing KYA token",
      },
    },
  }));
  const client = createTerminalClient({
    baseUrl: "https://terminal.facet.llc",
    fetch,
  });
  const { data, error, response } = await client.GET("/v1/health");
  assertEquals(data, undefined);
  assertEquals(response.status, 401);
  assertExists(error);
  assertEquals((error as { error: { code: string } }).error.code, "UNAUTHORIZED");
});
