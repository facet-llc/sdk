// Deno-side typed wire surface. Mirrors the Node SDK's typed client
// line-for-line in semantics; the only difference is the `openapi-fetch`
// import path which uses Deno's `npm:` specifier to pull the same exact
// version the Node SDK depends on (see `deno.json#imports`).
//
// `createTerminalClient` returns the openapi-fetch client typed against
// the Facet Terminal OpenAPI spec. The hand-written
// `discoverAndConnect` / `fetchAgentsTxt` helpers stay on top and are
// the recommended ergonomic entry point; the typed client is exposed
// for callers that want a thin per-route handle.

import createClient, { type Client, type ClientOptions } from "openapi-fetch";
import type { paths } from "./generated/schema.d.ts";

export type { paths, components, operations } from "./generated/schema.d.ts";

export type TerminalClient = Client<paths>;

export interface CreateTerminalClientOptions {
  /**
   * Base URL of the Facet Terminal (e.g.
   * `https://terminal.facet.llc`). Trailing slashes are tolerated.
   */
  readonly baseUrl: string;
  /**
   * Optional KYA bearer token or async provider. When provided, every
   * request is sent with `Authorization: Bearer <token>`. Endpoints
   * marked `security: [{}]` (the meta + discovery surface) ignore the
   * header; the rest require it.
   */
  readonly kyaToken?: string | (() => string | Promise<string>);
  /**
   * Custom fetch implementation. Defaults to `globalThis.fetch`. Useful
   * for tests and for agents that route through a proxy / mTLS pool.
   */
  readonly fetch?: (input: Request) => Promise<Response>;
  /**
   * `User-Agent` header value. Defaults to `@facet-llc/sdk-deno`.
   */
  readonly userAgent?: string;
  /**
   * Extra headers merged into every request. Useful for callers that
   * need to thread a tenant header, an attestation, or a custom
   * `X-Facet-Trace-Id` upstream.
   */
  readonly headers?: Record<string, string>;
}

/**
 * Build a typed `openapi-fetch` client pointed at a Facet Terminal.
 *
 * ```ts
 * import { createTerminalClient } from "@facet-llc/sdk-deno";
 * const c = createTerminalClient({ baseUrl: "https://terminal.facet.llc" });
 * const { data, error } = await c.GET("/v1/health");
 * if (error) throw error;
 * console.log(data.status); // "ok"
 * ```
 */
export function createTerminalClient(opts: CreateTerminalClientOptions): TerminalClient {
  const baseUrl = opts.baseUrl.replace(/\/+$/, "");
  const userAgent = opts.userAgent ?? "@facet-llc/sdk-deno";

  const tokenProvider = opts.kyaToken;
  const userFetch = opts.fetch;
  const extraHeaders = opts.headers ?? {};

  const fetchImpl: (input: Request) => Promise<Response> = async (input) => {
    const headers = new Headers(input.headers);
    if (!headers.has("user-agent")) headers.set("user-agent", userAgent);
    for (const [k, v] of Object.entries(extraHeaders)) {
      if (!headers.has(k)) headers.set(k, v);
    }
    if (tokenProvider !== undefined && !headers.has("authorization")) {
      const token = typeof tokenProvider === "string" ? tokenProvider : await tokenProvider();
      headers.set("authorization", `Bearer ${token}`);
    }
    const next = new Request(input, { headers });
    return userFetch !== undefined ? userFetch(next) : fetch(next);
  };

  const clientOptions: ClientOptions = {
    baseUrl,
    fetch: fetchImpl,
  };
  return createClient<paths>(clientOptions);
}
