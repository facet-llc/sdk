from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.ucp_checkout_create_response import UcpCheckoutCreateResponse
from ...models.ucp_originated_checkout_create_request import UcpOriginatedCheckoutCreateRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UcpOriginatedCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    if not isinstance(x_facet_trace_id, Unset):
        headers["X-Facet-Trace-Id"] = x_facet_trace_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ucp/v1/originated-checkouts",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | UcpCheckoutCreateResponse | None:
    if response.status_code == 200:
        response_200 = UcpCheckoutCreateResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = FacetErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = FacetErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = FacetErrorEnvelope.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = FacetErrorEnvelope.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = FacetErrorEnvelope.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = FacetErrorEnvelope.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UcpOriginatedCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]:
    """ Originated UCP checkout CREATE. This platform Terminal forwards a buyer's checkout to a `target`
    merchant Terminal (POST /ucp/v1/checkout-sessions) and adds the RFC 9421 ES256 platform signature
    SERVER-side, so the buyer never holds the platform key. The buyer authenticates to this Terminal
    with its own KYA (Authorization: Bearer), which is forwarded verbatim as the merchant's second auth
    factor; the merchant then sees both the platform signature and the buyer KYA and enforces its own
    dual-auth. First-party only: `target` must match a configured allowed suffix, and the route 404s
    until the operator provisions FACET_UCP_PLATFORM_SIGNER_JWK and sets
    FACET_UCP_PLATFORM_ORIGINATION_ENABLED. The merchant response (with its 402/offer body) relays
    verbatim. Moves no funds itself.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCreateRequest): An originated UCP checkout create (POST
            /ucp/v1/originated-checkouts). This platform Terminal forwards the buyer's checkout to the
            `target` merchant Terminal and adds the RFC 9421 ES256 platform signature server-side, so
            the buyer never holds the platform key. The buyer authenticates to this Terminal with its
            own KYA (Authorization: Bearer), which is forwarded to the merchant as the second auth
            factor. Moves no funds; the merchant response (including its 402/offer body) relays
            verbatim.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]
     """


    kwargs = _get_kwargs(
        body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: UcpOriginatedCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCreateResponse | None:
    """ Originated UCP checkout CREATE. This platform Terminal forwards a buyer's checkout to a `target`
    merchant Terminal (POST /ucp/v1/checkout-sessions) and adds the RFC 9421 ES256 platform signature
    SERVER-side, so the buyer never holds the platform key. The buyer authenticates to this Terminal
    with its own KYA (Authorization: Bearer), which is forwarded verbatim as the merchant's second auth
    factor; the merchant then sees both the platform signature and the buyer KYA and enforces its own
    dual-auth. First-party only: `target` must match a configured allowed suffix, and the route 404s
    until the operator provisions FACET_UCP_PLATFORM_SIGNER_JWK and sets
    FACET_UCP_PLATFORM_ORIGINATION_ENABLED. The merchant response (with its 402/offer body) relays
    verbatim. Moves no funds itself.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCreateRequest): An originated UCP checkout create (POST
            /ucp/v1/originated-checkouts). This platform Terminal forwards the buyer's checkout to the
            `target` merchant Terminal and adds the RFC 9421 ES256 platform signature server-side, so
            the buyer never holds the platform key. The buyer authenticates to this Terminal with its
            own KYA (Authorization: Bearer), which is forwarded to the merchant as the second auth
            factor. Moves no funds; the merchant response (including its 402/offer body) relays
            verbatim.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpCheckoutCreateResponse
     """


    return sync_detailed(
        client=client,
body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UcpOriginatedCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]:
    """ Originated UCP checkout CREATE. This platform Terminal forwards a buyer's checkout to a `target`
    merchant Terminal (POST /ucp/v1/checkout-sessions) and adds the RFC 9421 ES256 platform signature
    SERVER-side, so the buyer never holds the platform key. The buyer authenticates to this Terminal
    with its own KYA (Authorization: Bearer), which is forwarded verbatim as the merchant's second auth
    factor; the merchant then sees both the platform signature and the buyer KYA and enforces its own
    dual-auth. First-party only: `target` must match a configured allowed suffix, and the route 404s
    until the operator provisions FACET_UCP_PLATFORM_SIGNER_JWK and sets
    FACET_UCP_PLATFORM_ORIGINATION_ENABLED. The merchant response (with its 402/offer body) relays
    verbatim. Moves no funds itself.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCreateRequest): An originated UCP checkout create (POST
            /ucp/v1/originated-checkouts). This platform Terminal forwards the buyer's checkout to the
            `target` merchant Terminal and adds the RFC 9421 ES256 platform signature server-side, so
            the buyer never holds the platform key. The buyer authenticates to this Terminal with its
            own KYA (Authorization: Bearer), which is forwarded to the merchant as the second auth
            factor. Moves no funds; the merchant response (including its 402/offer body) relays
            verbatim.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]
     """


    kwargs = _get_kwargs(
        body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UcpOriginatedCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCreateResponse | None:
    """ Originated UCP checkout CREATE. This platform Terminal forwards a buyer's checkout to a `target`
    merchant Terminal (POST /ucp/v1/checkout-sessions) and adds the RFC 9421 ES256 platform signature
    SERVER-side, so the buyer never holds the platform key. The buyer authenticates to this Terminal
    with its own KYA (Authorization: Bearer), which is forwarded verbatim as the merchant's second auth
    factor; the merchant then sees both the platform signature and the buyer KYA and enforces its own
    dual-auth. First-party only: `target` must match a configured allowed suffix, and the route 404s
    until the operator provisions FACET_UCP_PLATFORM_SIGNER_JWK and sets
    FACET_UCP_PLATFORM_ORIGINATION_ENABLED. The merchant response (with its 402/offer body) relays
    verbatim. Moves no funds itself.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCreateRequest): An originated UCP checkout create (POST
            /ucp/v1/originated-checkouts). This platform Terminal forwards the buyer's checkout to the
            `target` merchant Terminal and adds the RFC 9421 ES256 platform signature server-side, so
            the buyer never holds the platform key. The buyer authenticates to this Terminal with its
            own KYA (Authorization: Bearer), which is forwarded to the merchant as the second auth
            factor. Moves no funds; the merchant response (including its 402/offer body) relays
            verbatim.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpCheckoutCreateResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
