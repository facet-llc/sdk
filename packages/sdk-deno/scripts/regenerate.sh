#!/usr/bin/env bash
# Regenerate `src/generated/schema.d.ts` from the canonical
# `openapi/openapi.yaml`. Idempotent — running twice produces no diff
# unless the spec changed. Reuses the `openapi-typescript` binary
# installed under `packages/sdk-node/node_modules/.bin/` so Deno does
# not need a separate npm install.
#
# Phase 8 of openapi-as-contract. The output is identical character-
# for-character to `packages/sdk-node/src/generated/schema.d.ts` —
# openapi-typescript emits standard `.d.ts`, which Deno consumes as-is.
# A `.gitkeep`-style hash check in `scripts/regenerate-sdks.sh`
# verifies parity.
#
# Local: `bash packages/sdk-deno/scripts/regenerate.sh`
# Top-level: `bash scripts/regenerate-sdks.sh`

set -euo pipefail

pkg_dir="$(cd "$(dirname "$0")/.." && pwd)"
repo_root="$(cd "${pkg_dir}/../.." && pwd)"
spec="${repo_root}/openapi/openapi.yaml"
out="${pkg_dir}/src/generated/schema.d.ts"
node_bin="${repo_root}/packages/sdk-node/node_modules/.bin/openapi-typescript"

if [ ! -f "${spec}" ]; then
  echo "openapi/openapi.yaml not found at ${spec}" >&2
  echo "Run scripts/build-openapi.sh first." >&2
  exit 1
fi

if [ ! -x "${node_bin}" ]; then
  echo "openapi-typescript not installed at ${node_bin}" >&2
  echo "Run pnpm install at the repo root first." >&2
  exit 1
fi

mkdir -p "$(dirname "${out}")"
"${node_bin}" "${spec}" -o "${out}" \
  --export-type \
  --default-non-nullable

line_count=$(wc -l < "${out}" | tr -d '[:space:]')
echo "sdk-deno: regenerated ${out} (${line_count} lines)"
