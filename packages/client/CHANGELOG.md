# Changelog

All notable changes to `@facet-llc/client` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2026-08-21

### Added

- `discover()` for agents.txt Terminal discovery, plus the shared `FACET_MCP_TOOLS` tool schemas.

### Changed

- Renamed the underlying package dependency from `@facet-llc/protocol` to `@facet-llc/adapter`; imports and re-exported types were updated to match.
- UCP checkout is now the advertised default across the live rails.

This changelog begins at 0.5.0; earlier 0.x releases predate it.
