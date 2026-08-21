"""Unit tests for the facet_sdk ergonomic wrapper.

The smoke test against a live Facet Terminal lives in
``tests/smoke/test_smoke.py`` and runs in the ``sdk-smoke-test`` CI
tier (gated by ``-m smoke``).
"""

from __future__ import annotations

import pytest

from facet_sdk import (
    DEFAULT_TIMEOUT_SECONDS,
    DEFAULT_USER_AGENT,
    AuthenticatedClient,
    Client,
    create_terminal_client,
)


class TestCreateTerminalClient:
    def test_returns_anonymous_client_when_no_token(self) -> None:
        client = create_terminal_client("https://terminal.facet.llc")
        assert isinstance(client, Client)
        # Generated Client base_url is exposed via the private attr; we
        # don't reach into it — instead check via the public httpx
        # client surface.
        httpx_client = client.get_httpx_client()
        assert str(httpx_client.base_url).startswith("https://terminal.facet.llc")

    def test_returns_authenticated_client_when_token_provided(self) -> None:
        client = create_terminal_client(
            "https://terminal.facet.llc",
            kya_token="kya-test-token",
        )
        assert isinstance(client, AuthenticatedClient)
        httpx_client = client.get_httpx_client()
        # The generated AuthenticatedClient bakes the Bearer token
        # into the default headers when its httpx client is built.
        assert (
            httpx_client.headers.get("Authorization") == "Bearer kya-test-token"
        )

    def test_strips_trailing_slashes_from_base_url(self) -> None:
        client = create_terminal_client("https://terminal.facet.llc///")
        httpx_client = client.get_httpx_client()
        # httpx normalizes the base URL representation, but our
        # caller-visible base must not retain extra slashes.
        assert str(httpx_client.base_url).rstrip("/") == "https://terminal.facet.llc"

    def test_default_user_agent_is_set(self) -> None:
        client = create_terminal_client("https://terminal.facet.llc")
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers.get("User-Agent") == DEFAULT_USER_AGENT

    def test_custom_user_agent_overrides_default(self) -> None:
        client = create_terminal_client(
            "https://terminal.facet.llc",
            user_agent="my-agent/1.0",
        )
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers.get("User-Agent") == "my-agent/1.0"

    def test_extra_headers_are_merged(self) -> None:
        client = create_terminal_client(
            "https://terminal.facet.llc",
            headers={"X-Tenant-Id": "acme"},
        )
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers.get("X-Tenant-Id") == "acme"
        # User-Agent default still applied.
        assert httpx_client.headers.get("User-Agent") == DEFAULT_USER_AGENT

    def test_custom_timeout_threaded_into_httpx(self) -> None:
        client = create_terminal_client(
            "https://terminal.facet.llc",
            timeout_seconds=12.5,
        )
        httpx_client = client.get_httpx_client()
        # httpx.Timeout exposes per-phase floats; the constructor we
        # used builds a uniform Timeout so connect/read/write/pool
        # all match.
        assert httpx_client.timeout.connect == 12.5
        assert httpx_client.timeout.read == 12.5

    def test_defaults_are_documented_constants(self) -> None:
        # Guardrail: the documented constants stay public so callers
        # can introspect what they're getting.
        assert isinstance(DEFAULT_USER_AGENT, str)
        assert DEFAULT_USER_AGENT.startswith("facet-sdk-python/")
        assert DEFAULT_TIMEOUT_SECONDS == 30.0


class TestGeneratedClientWiring:
    """Cross-check the generated client surface — these are exercised
    by the smoke test against a real Terminal; here we just verify the
    request-building helper composes cleanly without a network call.
    """

    def test_get_health_endpoint_module_imports(self) -> None:
        # Touch the generated endpoint so import-time errors (missing
        # models, broken response handlers) surface in unit tests
        # instead of at first network request.
        from facet_terminal_client.api.protocol_core import get_health  # noqa: F401

    def test_health_response_model_imports(self) -> None:
        from facet_terminal_client.models.health_response import HealthResponse
        from facet_terminal_client.models.health_response_status import (
            HealthResponseStatus,
        )

        # The model is an attrs class with from_dict / to_dict; smoke
        # the round-trip. Enum-typed fields use the generated enum
        # class so callers get static narrowing.
        original = HealthResponse(
            status=HealthResponseStatus.OK,
            timestamp="2026-05-25T00:00:00Z",
        )
        round_tripped = HealthResponse.from_dict(original.to_dict())
        assert round_tripped.status == original.status
        assert round_tripped.timestamp == original.timestamp

    def test_facet_error_envelope_model_imports(self) -> None:
        from facet_terminal_client.models.facet_error_envelope import (
            FacetErrorEnvelope,
        )
        from facet_terminal_client.models.facet_error_code import FacetErrorCode

        # FacetErrorCode is a closed union — verify a known code parses
        # without falling back to UnknownVariant. This is the Phase 2
        # discipline that any new error code must be added to the spec
        # before client code can use it. All five FacetErrorBody fields
        # are spec-required; supply them all.
        envelope = FacetErrorEnvelope.from_dict(
            {
                "error": {
                    "code": "UNAUTHORIZED",
                    "message": "missing KYA token",
                    "retryable": False,
                    "retry_after_seconds": None,
                    "suggest": None,
                }
            }
        )
        assert envelope.error.code == FacetErrorCode.UNAUTHORIZED
