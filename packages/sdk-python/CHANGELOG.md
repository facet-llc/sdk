# Changelog

All notable changes to `facet-sdk` (Python) are documented here. The
format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
this package adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-08-21

### Added

- The pytest suite now runs in CI via a new `sdk-suites` job.

### Changed

- Regenerated the typed client (`src/facet_terminal_client`) from the
  current OpenAPI spec, picking up the new route families including the
  public `/v1/stores` live-merchant directory.

### Fixed

- Corrected the public repository URL in the package metadata.

## [0.1.0] - 2026-05-25

### Added

- Initial release.
- Typed wire surface (`facet_terminal_client.*`) generated from
  `openapi/openapi.yaml` via `openapi-python-client@0.28.4`. Every
  endpoint in the canonical spec is exposed as a Python function under
  `facet_terminal_client.api.<tag>.<operation_id>`; every
  `components.schemas.*` entry becomes an `attrs` class under
  `facet_terminal_client.models.*`.
- Ergonomic factory `facet_sdk.create_terminal_client(base_url, ...)`
  with sensible defaults (User-Agent, timeout, KYA bearer threading).
- Smoke test suite under `tests/smoke/` that hits a live Facet
  Terminal, gated to the `sdk-smoke-test` CI tier via the `smoke`
  marker.
- Idempotent regen script at `scripts/regenerate.sh`; wired into the
  top-level `scripts/regenerate-sdks.sh` orchestrator.

### Notes

- `FacetErrorCode` is a closed union per the spec; new codes MUST
  land in `openapi/openapi.yaml` first.
- Discriminated-union narrowing (`PaymentsDispatchRequest`,
  webhook envelopes) is preserved end-to-end through the generated
  attrs classes.
