# @facet-llc/sdk-deno

Agent-side discovery SDK for the Facet protocol — Deno.

Mirror of [`@facet-llc/sdk-node`](../sdk-node/) using Deno's built-in `fetch` and `Response`. Same public surface, same typed errors, same caching semantics.

## Quick start

```ts
import { discoverAndConnect } from "@facet-llc/sdk-deno";

const client = await discoverAndConnect("acme-ingredients.example.com", {
  capabilityCheck: ["catalog"],
  kyaToken: async () => issuer.mintToken(),
});

const caps = await client.capabilities();
const results = await client.search({ query: "vanilla", limit: 10 });
```

The returned `client` is the same `FacetClient` from [`@facet-llc/client`](../client/) the Node SDK hands back — it runs on Node 20+, Bun, and Deno.

## Imports

This package resolves `@facet-llc/adapter` and `@facet-llc/client` via the workspace `deno.json`. If you're consuming the SDK from another Deno project, add equivalent import-map entries (or use the published npm artifact).

## API

Identical to `@facet-llc/sdk-node`. See [`packages/sdk-node/README.md`](../sdk-node/README.md) for the full API reference. The only behavioral difference is the runtime: `globalThis.fetch` is Deno's, not Node's, and tests run under `deno test`.

## Errors

Every failure throws a named, typed error — same set as the Node port:

- `NoManifestError` — HTTP 404 on `/.well-known/agents.txt`.
- `InvalidManifestError` — parser rejected the body.
- `UnsupportedVersionError` — `Facet-Version` not in `{0.2, 1.0, 1.1}`.
- `FetchError` — non-2xx (other than 404), DNS / TLS / abort.
- `CapabilityMismatchError` — required capability not advertised.

## Run the tests

```bash
deno task test
# or
deno test --allow-net=127.0.0.1,0.0.0.0,localhost ./test/
```

The fixture-server test in `test/discovery.test.ts` binds a Deno HTTP server on a random localhost port, so `--allow-net` is scoped to loopback.

## License

Apache License, Version 2.0 — see [`LICENSE`](LICENSE).
