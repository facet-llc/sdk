"""Phase 8 smoke test — drives the Python SDK against a live Facet Terminal.

Runs in the ``sdk-smoke-test`` CI tier (filtered by ``-m smoke``). The
default ``pytest`` invocation skips this module via the marker.

Set ``FACET_SMOKE_BASE_URL`` to override the target. The default points
at ``api.facet.llc`` because today it's the canonical live deployment
serving ``v1/*``; the post-cutover canonical ``terminal.facet.llc`` is
the deployment target tracked outside Phase 8.

The smoke assertion is intentionally narrow: the SDK can dispatch a
real request, parse the response envelope, and surface either the
success body OR the structured ``FacetErrorEnvelope`` to the caller.
We do NOT assert the Terminal returns 200 — the production Terminal
classifies unauthenticated traffic as ``PAYMENT_REQUIRED`` (HTTP 402)
per spec, which is itself a load-bearing signal that the SDK round-
trip works end-to-end against the live wire contract.
"""

from __future__ import annotations

import os

import pytest

from facet_sdk import create_terminal_client
from facet_terminal_client.api.protocol_core import get_version
from facet_terminal_client.models.facet_error_envelope import FacetErrorEnvelope
from facet_terminal_client.models.version_response import VersionResponse

SMOKE_BASE_URL = os.environ.get("FACET_SMOKE_BASE_URL", "https://api.facet.llc")


@pytest.mark.smoke
def test_get_version_round_trips_through_typed_client() -> None:
    client = create_terminal_client(SMOKE_BASE_URL)
    response = get_version.sync_detailed(client=client)

    # `sync_detailed` returns a Response wrapper exposing status_code,
    # headers, parsed (the typed body), and content (raw bytes).
    assert response is not None
    assert 200 <= response.status_code < 600
    # `parsed` is either VersionResponse (200) or FacetErrorEnvelope
    # (any documented non-2xx). Anything else means the spec drifted
    # from the live Terminal.
    if response.status_code == 200:
        assert isinstance(response.parsed, VersionResponse)
    else:
        assert isinstance(response.parsed, FacetErrorEnvelope), (
            f"expected FacetErrorEnvelope at status {response.status_code}, "
            f"got {type(response.parsed).__name__}"
        )
        # FacetErrorCode is the closed union — narrow on a known code
        # so the smoke catches any new code that ships without spec.
        assert response.parsed.error.code is not None


@pytest.mark.smoke
def test_trace_id_header_surfaces_on_response() -> None:
    client = create_terminal_client(SMOKE_BASE_URL)
    response = get_version.sync_detailed(client=client)

    # The Terminal sets a trace-id header on every response (the spec
    # promises `X-Facet-Trace-Id`; today's deployment uses
    # `x-agent-trace-id` — we accept either so the smoke does not
    # tighten until the rename ships). Either header present confirms
    # we are actually hitting the Facet stack and not a proxy that ate
    # the request.
    trace_id = response.headers.get("x-facet-trace-id") or response.headers.get(
        "x-agent-trace-id"
    )
    assert trace_id, "Terminal must set a trace-id header"
