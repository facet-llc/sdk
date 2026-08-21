from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.ucp_checkout_create_request import UcpCheckoutCreateRequest
from ...models.ucp_checkout_create_response import UcpCheckoutCreateResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UcpCheckoutCreateRequest,
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
        "url": "/ucp/v1/checkout-sessions",
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
    body: UcpCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]:
    """ UCP checkout CREATE. Reserves a single server-priced line item and returns a checkout session
    advertising the llc.facet.x402 payment requirements (network, USDC, pay_to, amount). The amount +
    pay_to are SERVER-resolved from the reservation + the merchant's sites row, never the request body.
    Public + activation-exempt; returns 404 until the operator enables UCP via FACET_UCP_ENABLED. RFC
    9421 ES256-signed. IDENTITY: accepts EITHER an RFC 9421 ES256 platform signature (a UCP platform
    checking out for its user; the checkout is owned by the TLS-authenticated profile origin) OR a Facet
    KYA as `Authorization: Bearer <ES256 JWT>` (an autonomous agent checking out on its own behalf; the
    checkout is owned by the KYA `aid`). A valid platform signature wins when both are presented, and
    whichever principal creates a checkout is the only one that can complete it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCreateRequest): A UCP checkout create request (POST /ucp/v1/checkout-
            sessions). v1 reserves a cart of server-priced DISTINCT line items and advertises the
            llc.facet.x402 payment requirements. Every price is resolved from this merchant's catalog,
            never the request body.

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
    body: UcpCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCreateResponse | None:
    """ UCP checkout CREATE. Reserves a single server-priced line item and returns a checkout session
    advertising the llc.facet.x402 payment requirements (network, USDC, pay_to, amount). The amount +
    pay_to are SERVER-resolved from the reservation + the merchant's sites row, never the request body.
    Public + activation-exempt; returns 404 until the operator enables UCP via FACET_UCP_ENABLED. RFC
    9421 ES256-signed. IDENTITY: accepts EITHER an RFC 9421 ES256 platform signature (a UCP platform
    checking out for its user; the checkout is owned by the TLS-authenticated profile origin) OR a Facet
    KYA as `Authorization: Bearer <ES256 JWT>` (an autonomous agent checking out on its own behalf; the
    checkout is owned by the KYA `aid`). A valid platform signature wins when both are presented, and
    whichever principal creates a checkout is the only one that can complete it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCreateRequest): A UCP checkout create request (POST /ucp/v1/checkout-
            sessions). v1 reserves a cart of server-priced DISTINCT line items and advertises the
            llc.facet.x402 payment requirements. Every price is resolved from this merchant's catalog,
            never the request body.

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
    body: UcpCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]:
    """ UCP checkout CREATE. Reserves a single server-priced line item and returns a checkout session
    advertising the llc.facet.x402 payment requirements (network, USDC, pay_to, amount). The amount +
    pay_to are SERVER-resolved from the reservation + the merchant's sites row, never the request body.
    Public + activation-exempt; returns 404 until the operator enables UCP via FACET_UCP_ENABLED. RFC
    9421 ES256-signed. IDENTITY: accepts EITHER an RFC 9421 ES256 platform signature (a UCP platform
    checking out for its user; the checkout is owned by the TLS-authenticated profile origin) OR a Facet
    KYA as `Authorization: Bearer <ES256 JWT>` (an autonomous agent checking out on its own behalf; the
    checkout is owned by the KYA `aid`). A valid platform signature wins when both are presented, and
    whichever principal creates a checkout is the only one that can complete it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCreateRequest): A UCP checkout create request (POST /ucp/v1/checkout-
            sessions). v1 reserves a cart of server-priced DISTINCT line items and advertises the
            llc.facet.x402 payment requirements. Every price is resolved from this merchant's catalog,
            never the request body.

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
    body: UcpCheckoutCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCreateResponse | None:
    """ UCP checkout CREATE. Reserves a single server-priced line item and returns a checkout session
    advertising the llc.facet.x402 payment requirements (network, USDC, pay_to, amount). The amount +
    pay_to are SERVER-resolved from the reservation + the merchant's sites row, never the request body.
    Public + activation-exempt; returns 404 until the operator enables UCP via FACET_UCP_ENABLED. RFC
    9421 ES256-signed. IDENTITY: accepts EITHER an RFC 9421 ES256 platform signature (a UCP platform
    checking out for its user; the checkout is owned by the TLS-authenticated profile origin) OR a Facet
    KYA as `Authorization: Bearer <ES256 JWT>` (an autonomous agent checking out on its own behalf; the
    checkout is owned by the KYA `aid`). A valid platform signature wins when both are presented, and
    whichever principal creates a checkout is the only one that can complete it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCreateRequest): A UCP checkout create request (POST /ucp/v1/checkout-
            sessions). v1 reserves a cart of server-priced DISTINCT line items and advertises the
            llc.facet.x402 payment requirements. Every price is resolved from this merchant's catalog,
            never the request body.

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
