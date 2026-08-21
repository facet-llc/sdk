#!/usr/bin/env bash
# Regenerate the sdk-python client from `openapi/openapi.yaml` using
# `openapi-python-client`. Idempotent — running twice produces no diff
# unless the spec changed.
#
# Phase 8 of openapi-as-contract. The generator emits a full Python
# package under `src/facet_terminal_client/`; the hand-written wrapper
# at `src/facet_sdk/__init__.py` layers an ergonomic helper on top
# (mirroring the TS-side `createTerminalClient`).
#
# Local: `bash packages/sdk-python/scripts/regenerate.sh`
# Top-level: `bash scripts/regenerate-sdks.sh`
#
# Requires `openapi-python-client` on PATH. Install via:
#     pipx install openapi-python-client==0.28.4
# or
#     pip install --user openapi-python-client==0.28.4
#
# Output is a function of the SPEC ALONE, not of the machine. That is enforced by
# `openapi-python-client.config.yml`, which pins `post_hooks: []`. Without it the
# generator's default hooks run `ruff` whenever it is on PATH, so a developer with
# ruff installed emits reformatted source (deduplicated, re-sorted imports) while
# a runner without it emits the raw output that is committed here. That mismatch
# shows up as a spurious repo-wide diff and a red SDK-drift gate for the developer,
# not for CI. Keep the --config flag.

set -euo pipefail

pkg_dir="$(cd "$(dirname "$0")/.." && pwd)"
repo_root="$(cd "${pkg_dir}/../.." && pwd)"
spec="${repo_root}/openapi/openapi.yaml"
out_dir="${pkg_dir}/src"

if [ ! -f "${spec}" ]; then
  echo "openapi/openapi.yaml not found at ${spec}" >&2
  echo "Run scripts/build-openapi.sh first." >&2
  exit 1
fi

if ! command -v openapi-python-client >/dev/null 2>&1; then
  echo "openapi-python-client not on PATH." >&2
  echo "Install with: pipx install openapi-python-client==0.28.4" >&2
  exit 1
fi

# Generate into a tempdir first, then sync into src/facet_terminal_client.
# The CLI's `--overwrite` only works when the directory already exists at
# the output path; staging through tmp keeps the script idempotent against
# previous failed runs.
tmp_dir="$(mktemp -d)"
trap 'rm -rf "${tmp_dir}"' EXIT

(
  cd "${tmp_dir}"
  openapi-python-client generate \
    --path "${spec}" \
    --meta none \
    --overwrite \
    --config "${pkg_dir}/openapi-python-client.config.yml" \
    --output-path "${tmp_dir}/facet_terminal_client" \
    >/dev/null
)

mkdir -p "${out_dir}"
rm -rf "${out_dir}/facet_terminal_client"
mv "${tmp_dir}/facet_terminal_client" "${out_dir}/facet_terminal_client"

file_count=$(find "${out_dir}/facet_terminal_client" -type f -name '*.py' | wc -l | tr -d '[:space:]')
echo "sdk-python: regenerated ${out_dir}/facet_terminal_client (${file_count} Python files)"
