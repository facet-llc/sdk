from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.ucp_cart_create_request import UcpCartCreateRequest
from ...models.ucp_cart_response import UcpCartResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UcpCartCreateRequest,
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
        "url": "/ucp/v1/carts",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | UcpCartResponse | None:
    if response.status_code == 200:
        response_200 = UcpCartResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | UcpCartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UcpCartCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCartResponse]:
    """ UCP cart CREATE. Builds a pre-checkout, MUTABLE cart: prices a set of DISTINCT line items server-
    side from the catalog (ESTIMATED, goods-only, no ship-to) and returns the cart resource (id,
    currency, line_items, totals). A cart moves NO money and holds NO inventory. Promote it to a real
    checkout by sending its id as `cart_id` to POST /ucp/v1/checkout-sessions. Public + activation-
    exempt; 404 until FACET_UCP_ENABLED. IDENTITY: an RFC 9421 ES256 platform signature (cart owned by
    the TLS-authenticated profile origin) OR a Facet KYA as `Authorization: Bearer <ES256 JWT>` (cart
    owned by the KYA `aid`); whichever principal creates a cart is the only one that can read, update,
    or cancel it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCartCreateRequest): A UCP cart create request (POST /ucp/v1/carts). Prices a set
            of DISTINCT line items server-side and stores a pre-checkout, MUTABLE cart. Estimated
            pricing only (goods-only, no ship-to); the cart moves no money and holds no inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpCartResponse]
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
    body: UcpCartCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCartResponse | None:
    """ UCP cart CREATE. Builds a pre-checkout, MUTABLE cart: prices a set of DISTINCT line items server-
    side from the catalog (ESTIMATED, goods-only, no ship-to) and returns the cart resource (id,
    currency, line_items, totals). A cart moves NO money and holds NO inventory. Promote it to a real
    checkout by sending its id as `cart_id` to POST /ucp/v1/checkout-sessions. Public + activation-
    exempt; 404 until FACET_UCP_ENABLED. IDENTITY: an RFC 9421 ES256 platform signature (cart owned by
    the TLS-authenticated profile origin) OR a Facet KYA as `Authorization: Bearer <ES256 JWT>` (cart
    owned by the KYA `aid`); whichever principal creates a cart is the only one that can read, update,
    or cancel it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCartCreateRequest): A UCP cart create request (POST /ucp/v1/carts). Prices a set
            of DISTINCT line items server-side and stores a pre-checkout, MUTABLE cart. Estimated
            pricing only (goods-only, no ship-to); the cart moves no money and holds no inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpCartResponse
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
    body: UcpCartCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCartResponse]:
    """ UCP cart CREATE. Builds a pre-checkout, MUTABLE cart: prices a set of DISTINCT line items server-
    side from the catalog (ESTIMATED, goods-only, no ship-to) and returns the cart resource (id,
    currency, line_items, totals). A cart moves NO money and holds NO inventory. Promote it to a real
    checkout by sending its id as `cart_id` to POST /ucp/v1/checkout-sessions. Public + activation-
    exempt; 404 until FACET_UCP_ENABLED. IDENTITY: an RFC 9421 ES256 platform signature (cart owned by
    the TLS-authenticated profile origin) OR a Facet KYA as `Authorization: Bearer <ES256 JWT>` (cart
    owned by the KYA `aid`); whichever principal creates a cart is the only one that can read, update,
    or cancel it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCartCreateRequest): A UCP cart create request (POST /ucp/v1/carts). Prices a set
            of DISTINCT line items server-side and stores a pre-checkout, MUTABLE cart. Estimated
            pricing only (goods-only, no ship-to); the cart moves no money and holds no inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpCartResponse]
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
    body: UcpCartCreateRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCartResponse | None:
    """ UCP cart CREATE. Builds a pre-checkout, MUTABLE cart: prices a set of DISTINCT line items server-
    side from the catalog (ESTIMATED, goods-only, no ship-to) and returns the cart resource (id,
    currency, line_items, totals). A cart moves NO money and holds NO inventory. Promote it to a real
    checkout by sending its id as `cart_id` to POST /ucp/v1/checkout-sessions. Public + activation-
    exempt; 404 until FACET_UCP_ENABLED. IDENTITY: an RFC 9421 ES256 platform signature (cart owned by
    the TLS-authenticated profile origin) OR a Facet KYA as `Authorization: Bearer <ES256 JWT>` (cart
    owned by the KYA `aid`); whichever principal creates a cart is the only one that can read, update,
    or cancel it.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCartCreateRequest): A UCP cart create request (POST /ucp/v1/carts). Prices a set
            of DISTINCT line items server-side and stores a pre-checkout, MUTABLE cart. Estimated
            pricing only (goods-only, no ship-to); the cart moves no money and holds no inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpCartResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
