from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.ucp_originated_checkout_redeem_request import UcpOriginatedCheckoutRedeemRequest
from ...models.ucp_submit_redeem_response import UcpSubmitRedeemResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UcpOriginatedCheckoutRedeemRequest,
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
        "url": "/ucp/v1/originated-checkouts/redeem",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | UcpSubmitRedeemResponse | None:
    if response.status_code == 200:
        response_200 = UcpSubmitRedeemResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | UcpSubmitRedeemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UcpOriginatedCheckoutRedeemRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpSubmitRedeemResponse]:
    """ Originated UCP deferred-redeem STORE. Forwards the buyer's pre-signed boson-redeem (signed CLIENT-
    side against the exchange id the COMMIT assigned) to the `target` merchant's redeem store under this
    platform's RFC 9421 ES256 signature plus the forwarded buyer KYA. This is the SECOND round-trip
    after the complete leg and is how a platform-originated checkout arms release-on-fulfillment: a
    buyer-only client cannot reach the merchant's redeem store directly because it is bound to the
    platform origin that COMMITTED the exchange. Non-custodial: no buyer key reaches this server, the
    platform key is auth and provenance only and never touches funds, the merchant STORES the redeem
    (moves no funds), and the on-chain release fires later from the merchant fulfillment webhook. Same
    first-party guard and enable flag as the create / complete legs.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutRedeemRequest): An originated UCP deferred-redeem store (POST
            /ucp/v1/originated-checkouts/redeem). Forwards the buyer's pre-signed boson-redeem to the
            target merchant's redeem store under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA, so a platform-originated checkout can arm release-on-fulfillment.
            Non-custodial: the platform key is auth and provenance only and never touches funds; the
            merchant stores the redeem and the on-chain release fires later from its fulfillment
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpSubmitRedeemResponse]
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
    body: UcpOriginatedCheckoutRedeemRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpSubmitRedeemResponse | None:
    """ Originated UCP deferred-redeem STORE. Forwards the buyer's pre-signed boson-redeem (signed CLIENT-
    side against the exchange id the COMMIT assigned) to the `target` merchant's redeem store under this
    platform's RFC 9421 ES256 signature plus the forwarded buyer KYA. This is the SECOND round-trip
    after the complete leg and is how a platform-originated checkout arms release-on-fulfillment: a
    buyer-only client cannot reach the merchant's redeem store directly because it is bound to the
    platform origin that COMMITTED the exchange. Non-custodial: no buyer key reaches this server, the
    platform key is auth and provenance only and never touches funds, the merchant STORES the redeem
    (moves no funds), and the on-chain release fires later from the merchant fulfillment webhook. Same
    first-party guard and enable flag as the create / complete legs.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutRedeemRequest): An originated UCP deferred-redeem store (POST
            /ucp/v1/originated-checkouts/redeem). Forwards the buyer's pre-signed boson-redeem to the
            target merchant's redeem store under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA, so a platform-originated checkout can arm release-on-fulfillment.
            Non-custodial: the platform key is auth and provenance only and never touches funds; the
            merchant stores the redeem and the on-chain release fires later from its fulfillment
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpSubmitRedeemResponse
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
    body: UcpOriginatedCheckoutRedeemRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpSubmitRedeemResponse]:
    """ Originated UCP deferred-redeem STORE. Forwards the buyer's pre-signed boson-redeem (signed CLIENT-
    side against the exchange id the COMMIT assigned) to the `target` merchant's redeem store under this
    platform's RFC 9421 ES256 signature plus the forwarded buyer KYA. This is the SECOND round-trip
    after the complete leg and is how a platform-originated checkout arms release-on-fulfillment: a
    buyer-only client cannot reach the merchant's redeem store directly because it is bound to the
    platform origin that COMMITTED the exchange. Non-custodial: no buyer key reaches this server, the
    platform key is auth and provenance only and never touches funds, the merchant STORES the redeem
    (moves no funds), and the on-chain release fires later from the merchant fulfillment webhook. Same
    first-party guard and enable flag as the create / complete legs.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutRedeemRequest): An originated UCP deferred-redeem store (POST
            /ucp/v1/originated-checkouts/redeem). Forwards the buyer's pre-signed boson-redeem to the
            target merchant's redeem store under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA, so a platform-originated checkout can arm release-on-fulfillment.
            Non-custodial: the platform key is auth and provenance only and never touches funds; the
            merchant stores the redeem and the on-chain release fires later from its fulfillment
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | UcpSubmitRedeemResponse]
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
    body: UcpOriginatedCheckoutRedeemRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpSubmitRedeemResponse | None:
    """ Originated UCP deferred-redeem STORE. Forwards the buyer's pre-signed boson-redeem (signed CLIENT-
    side against the exchange id the COMMIT assigned) to the `target` merchant's redeem store under this
    platform's RFC 9421 ES256 signature plus the forwarded buyer KYA. This is the SECOND round-trip
    after the complete leg and is how a platform-originated checkout arms release-on-fulfillment: a
    buyer-only client cannot reach the merchant's redeem store directly because it is bound to the
    platform origin that COMMITTED the exchange. Non-custodial: no buyer key reaches this server, the
    platform key is auth and provenance only and never touches funds, the merchant STORES the redeem
    (moves no funds), and the on-chain release fires later from the merchant fulfillment webhook. Same
    first-party guard and enable flag as the create / complete legs.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpOriginatedCheckoutRedeemRequest): An originated UCP deferred-redeem store (POST
            /ucp/v1/originated-checkouts/redeem). Forwards the buyer's pre-signed boson-redeem to the
            target merchant's redeem store under this platform's RFC 9421 ES256 signature plus the
            forwarded buyer KYA, so a platform-originated checkout can arm release-on-fulfillment.
            Non-custodial: the platform key is auth and provenance only and never touches funds; the
            merchant stores the redeem and the on-chain release fires later from its fulfillment
            webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | UcpSubmitRedeemResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
