from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.ucp_checkout_complete_response import UcpCheckoutCompleteResponse
from ...models.ucp_originated_checkout_complete_request import UcpOriginatedCheckoutCompleteRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UcpOriginatedCheckoutCompleteRequest,
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
        "url": "/ucp/v1/originated-checkouts/complete",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | UcpCheckoutCompleteResponse | None:
    if response.status_code == 200:
        response_200 = UcpCheckoutCompleteResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | UcpCheckoutCompleteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UcpOriginatedCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCompleteResponse]:
    """ Originated UCP checkout COMPLETE. Forwards the buyer's payment (signed CLIENT-side against the
    merchant offer from the create leg) to the `target` merchant's complete route under this platform's
    RFC 9421 ES256 signature plus the forwarded buyer KYA. No buyer key ever reaches this server; the
    platform re-signs only the outbound envelope. Non-custodial: the platform key is auth and provenance
    only and never touches funds, and the merchant's settlement response relays verbatim. Same first-
    party guard and enable flag as the create leg.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCompleteRequest): An originated UCP checkout complete (POST
            /ucp/v1/originated-checkouts/complete). Forwards the buyer's client-signed payment to the
            target merchant's complete route under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA. Non-custodial: the platform key is auth and provenance only and never
            touches funds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpCheckoutCompleteResponse]
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
    body: UcpOriginatedCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCompleteResponse | None:
    """ Originated UCP checkout COMPLETE. Forwards the buyer's payment (signed CLIENT-side against the
    merchant offer from the create leg) to the `target` merchant's complete route under this platform's
    RFC 9421 ES256 signature plus the forwarded buyer KYA. No buyer key ever reaches this server; the
    platform re-signs only the outbound envelope. Non-custodial: the platform key is auth and provenance
    only and never touches funds, and the merchant's settlement response relays verbatim. Same first-
    party guard and enable flag as the create leg.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCompleteRequest): An originated UCP checkout complete (POST
            /ucp/v1/originated-checkouts/complete). Forwards the buyer's client-signed payment to the
            target merchant's complete route under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA. Non-custodial: the platform key is auth and provenance only and never
            touches funds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpCheckoutCompleteResponse
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
    body: UcpOriginatedCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCompleteResponse]:
    """ Originated UCP checkout COMPLETE. Forwards the buyer's payment (signed CLIENT-side against the
    merchant offer from the create leg) to the `target` merchant's complete route under this platform's
    RFC 9421 ES256 signature plus the forwarded buyer KYA. No buyer key ever reaches this server; the
    platform re-signs only the outbound envelope. Non-custodial: the platform key is auth and provenance
    only and never touches funds, and the merchant's settlement response relays verbatim. Same first-
    party guard and enable flag as the create leg.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCompleteRequest): An originated UCP checkout complete (POST
            /ucp/v1/originated-checkouts/complete). Forwards the buyer's client-signed payment to the
            target merchant's complete route under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA. Non-custodial: the platform key is auth and provenance only and never
            touches funds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpCheckoutCompleteResponse]
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
    body: UcpOriginatedCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCompleteResponse | None:
    """ Originated UCP checkout COMPLETE. Forwards the buyer's payment (signed CLIENT-side against the
    merchant offer from the create leg) to the `target` merchant's complete route under this platform's
    RFC 9421 ES256 signature plus the forwarded buyer KYA. No buyer key ever reaches this server; the
    platform re-signs only the outbound envelope. Non-custodial: the platform key is auth and provenance
    only and never touches funds, and the merchant's settlement response relays verbatim. Same first-
    party guard and enable flag as the create leg.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutCompleteRequest): An originated UCP checkout complete (POST
            /ucp/v1/originated-checkouts/complete). Forwards the buyer's client-signed payment to the
            target merchant's complete route under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA. Non-custodial: the platform key is auth and provenance only and never
            touches funds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpCheckoutCompleteResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
