# Changelog

All notable changes to `@facet-llc/sdk-deno` are documented here. The
format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
this package adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-08-21

### Fixed

- **Import map repair.** `@facet-llc/adapter` was pointed at a retired
  `../protocol/src/index.ts` path (left over from the protocol-to-adapter
  package rename), so every `deno` resolve (check, test, publish) failed
  against the working-tree source. It now points at
  `../adapter/src/index.ts`.

### Added

- **The Deno suite now runs in CI.** A new `sdk-suites` job runs
  `deno task check` and `deno task test`, so this package's shipped surface
  can no longer regress silently.

### Changed

- **Regenerated `src/generated/schema.d.ts` from the current OpenAPI spec.**
  Picks up the new route families added since 0.1.0, including the public
  `/v1/stores` live-merchant directory.
