# facet-sdk (Python)

Python SDK for the [Facet Terminal](https://facet.llc) — the per-merchant
HTTP contract that every Facet deployment exposes.

The typed request/response surface is **generated from `openapi/openapi.yaml`**
via [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client).
A thin ergonomic wrapper at `facet_sdk` provides defaults (User-Agent,
timeout) and an authenticated-client factory.

> The wire surface is spec-driven — never edit
> `src/facet_terminal_client/` by hand; it is regenerated from
> `openapi/openapi.yaml`.

## Install

```bash
pip install facet-sdk
```

## Quickstart

```python
from facet_sdk import create_terminal_client
from facet_terminal_client.api.protocol_core import get_health, get_capabilities

client = create_terminal_client("https://terminal.facet.llc")

health = get_health.sync(client=client)
# `health` is a HealthResponse, a FacetErrorEnvelope, or None

caps = get_capabilities.sync(client=client)
```

## Authenticated calls (KYA token)

Endpoints in the four-verb commerce primitive surface (search, quote,
reserve, settle) and most tool surfaces require a KYA bearer token:

```python
from facet_sdk import create_terminal_client
from facet_terminal_client.api.protocol_core import quote
from facet_terminal_client.models import QuoteRequest

client = create_terminal_client(
    "https://terminal.facet.llc",
    kya_token="kya-bearer-from-skyfire-or-similar",
)

resp = quote.sync(client=client, body=QuoteRequest(sku="abc", quantity=1))
```

## Architecture

| Layer              | Module                                                 | What it is                                                                      |
| ------------------ | ------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Ergonomic helpers  | `facet_sdk`                                            | Hand-written wrappers (`create_terminal_client`). Stable API.                   |
| Typed wire surface | `facet_terminal_client.api.*`                          | Auto-generated per-endpoint functions. **Do not edit.**                         |
| Typed schemas      | `facet_terminal_client.models.*`                       | Auto-generated attrs classes for every `components.schemas.*`. **Do not edit.** |
| Generated client   | `facet_terminal_client.Client` / `AuthenticatedClient` | Auto-generated httpx-backed dispatch class.                                     |

## Regenerating from the spec

```bash
# Prerequisite: openapi-python-client on PATH
pipx install openapi-python-client==0.28.4

# Regenerate just sdk-python:
bash packages/sdk-python/scripts/regenerate.sh

# Or regenerate all three language SDKs from the spec:
bash scripts/regenerate-sdks.sh
```

The regen scripts are idempotent — running twice produces no diff
unless `openapi/openapi.yaml` changed.

## Tests

```bash
# Unit tests (offline):
pip install -e .[dev]
pytest

# Smoke tests against a live Facet Terminal (gated by marker):
pytest -m smoke

# Override the smoke target:
FACET_SMOKE_BASE_URL=https://my-merchant.example.com pytest -m smoke
```

## License

Apache-2.0.
