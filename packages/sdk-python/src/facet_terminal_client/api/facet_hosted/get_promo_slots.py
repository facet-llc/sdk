from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.promo_slots_response import PromoSlotsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    if not isinstance(x_facet_trace_id, Unset):
        headers["X-Facet-Trace-Id"] = x_facet_trace_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/promo/slots",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | PromoSlotsResponse | None:
    if response.status_code == 200:
        response_200 = PromoSlotsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | PromoSlotsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | PromoSlotsResponse]:
    """ Public mainnet-launch promo slot counter: sites claimed against the Tier 1 (any platform) and Tier 2
    (WooCommerce) caps. Unauthenticated, rate-limited by origin, cacheable, and CORS-open so the counter
    can be embedded cross-origin.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | PromoSlotsResponse]
     """


    kwargs = _get_kwargs(
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
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | PromoSlotsResponse | None:
    """ Public mainnet-launch promo slot counter: sites claimed against the Tier 1 (any platform) and Tier 2
    (WooCommerce) caps. Unauthenticated, rate-limited by origin, cacheable, and CORS-open so the counter
    can be embedded cross-origin.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | PromoSlotsResponse
     """


    return sync_detailed(
        client=client,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | PromoSlotsResponse]:
    """ Public mainnet-launch promo slot counter: sites claimed against the Tier 1 (any platform) and Tier 2
    (WooCommerce) caps. Unauthenticated, rate-limited by origin, cacheable, and CORS-open so the counter
    can be embedded cross-origin.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | PromoSlotsResponse]
     """


    kwargs = _get_kwargs(
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
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | PromoSlotsResponse | None:
    """ Public mainnet-launch promo slot counter: sites claimed against the Tier 1 (any platform) and Tier 2
    (WooCommerce) caps. Unauthenticated, rate-limited by origin, cacheable, and CORS-open so the counter
    can be embedded cross-origin.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | PromoSlotsResponse
     """


    return (await asyncio_detailed(
        client=client,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
