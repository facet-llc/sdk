"""Facet Terminal Python SDK — ergonomic layer.

Public entry points
-------------------
``create_terminal_client(base_url, ...)``
    Construct an authenticated httpx-backed client targeting a Facet
    Terminal. Returns an instance of the generated ``Client`` /
    ``AuthenticatedClient`` from ``facet_terminal_client``, configured
    with sensible defaults (User-Agent, timeout, optional KYA bearer).

``Client`` / ``AuthenticatedClient``
    Generated httpx-based client classes from ``facet_terminal_client``
    — re-exported here so callers can import them from one place.

Generated namespaces
--------------------
``facet_terminal_client.api.<tag>.<operation_id>`` — per-endpoint
    request functions, each one typed against the generated request /
    response models.
``facet_terminal_client.models.*`` — every schema in
    ``components.schemas`` becomes a frozen attrs class with
    ``.from_dict()`` and ``.to_dict()`` helpers.

The wire surface is fully spec-driven; this wrapper provides only the
ergonomic helpers (auth + defaults) on top so callers don't have to wire
httpx by hand.
"""

from __future__ import annotations

from typing import Awaitable, Callable, Optional, Union

from facet_terminal_client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "create_terminal_client",
    "DEFAULT_USER_AGENT",
    "DEFAULT_TIMEOUT_SECONDS",
    "__version__",
)

__version__ = "0.1.0"

DEFAULT_USER_AGENT = f"facet-sdk-python/{__version__}"
DEFAULT_TIMEOUT_SECONDS = 30.0

TokenProvider = Union[str, Callable[[], Union[str, Awaitable[str]]]]


def create_terminal_client(
    base_url: str,
    *,
    kya_token: Optional[str] = None,
    user_agent: str = DEFAULT_USER_AGENT,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    headers: Optional[dict[str, str]] = None,
    verify_ssl: bool = True,
) -> Union[Client, AuthenticatedClient]:
    """Build a configured Facet Terminal client.

    Parameters
    ----------
    base_url:
        Origin of the Facet Terminal — e.g.
        ``"https://terminal.facet.llc"``. Trailing slashes are
        tolerated. Per-merchant deployments pass their own origin.
    kya_token:
        Optional KYA bearer token. When provided, returns an
        ``AuthenticatedClient`` whose every request carries
        ``Authorization: Bearer <token>``. When ``None`` (the meta /
        discovery surface and the public reputation lookup), an
        unauthenticated ``Client`` is returned instead.
    user_agent:
        ``User-Agent`` header value. Defaults to
        ``facet-sdk-python/<version>``.
    timeout_seconds:
        Per-request timeout, threaded into httpx. Defaults to 30s,
        matching the TS SDK.
    headers:
        Extra headers merged into every request. Useful for tenant
        headers, attestations, or custom trace ids.
    verify_ssl:
        Whether to verify TLS certificates. Defaults to ``True`` —
        only set to ``False`` for local fixtures.

    Returns
    -------
    ``Client`` when ``kya_token`` is ``None``; ``AuthenticatedClient``
    otherwise. Both classes wrap an underlying ``httpx.Client`` /
    ``httpx.AsyncClient``; the generated endpoint functions accept
    either as their first positional argument.

    Usage
    -----
    >>> from facet_sdk import create_terminal_client
    >>> from facet_terminal_client.api.protocol_core import get_health
    >>> client = create_terminal_client("https://terminal.facet.llc")
    >>> resp = get_health.sync(client=client)
    >>> # resp is a HealthResponse, FacetErrorEnvelope, or None
    """
    normalized_url = base_url.rstrip("/")
    merged_headers: dict[str, str] = {
        "User-Agent": user_agent,
    }
    if headers is not None:
        merged_headers.update(headers)

    common = {
        "base_url": normalized_url,
        "timeout": _build_timeout(timeout_seconds),
        "verify_ssl": verify_ssl,
        "headers": merged_headers,
    }

    if kya_token is not None:
        return AuthenticatedClient(token=kya_token, **common)
    return Client(**common)


def _build_timeout(seconds: float):
    # Lazy import — keep the module-level surface httpx-free so a
    # `python -c "import facet_sdk"` smoke check doesn't pull httpx
    # unless the caller actually constructs a client.
    import httpx

    return httpx.Timeout(seconds)
