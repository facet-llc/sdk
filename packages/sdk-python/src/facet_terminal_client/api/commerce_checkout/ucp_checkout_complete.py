from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.ucp_checkout_complete_request import UcpCheckoutCompleteRequest
from ...models.ucp_checkout_complete_response import UcpCheckoutCompleteResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UcpCheckoutCompleteRequest,
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
        "url": "/ucp/v1/checkout-sessions/complete",
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
    body: UcpCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCompleteResponse]:
    """ UCP checkout COMPLETE. Bridges the buyer's signed credential to the Terminal dispatcher authority
    and reuses the non-custodial settle path: the amount is re-derived server-side from the reservation
    and the rail adapter re-verifies the signature, seller, escrow, asset and amount before a cent
    moves. An x402_authorization captures to the merchant's pay_to; a boson_commit_authorization COMMITS
    the escrow with the buyer's own x402B signature (the redeem is deferred to the merchant fulfillment
    webhook). The checkout id comes from the spec-correct /ucp/v1/checkout-sessions/{id}/complete path
    form, or the legacy `checkout_id` body field. Public + activation-exempt; 404 until
    FACET_UCP_ENABLED. RFC 9421 ES256-signed (a Boson commit REQUIRES a verified platform signature).

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCompleteRequest): A UCP checkout complete request (POST /ucp/v1/checkout-
            sessions/complete, or the spec-correct /{id}/complete). Bridges the buyer's credential to
            the Terminal dispatcher authority. x402 captures; a boson_commit_authorization COMMITS the
            escrow with the buyer's own x402B signature (funds escrow into the Diamond) and the redeem
            is deferred to the merchant fulfillment webhook. Money movement reuses the non-custodial
            settle path: the amount is re-derived server-side from the reservation and the rail
            adapter re-verifies the signature, seller, escrow, asset and amount before a cent moves.

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
    body: UcpCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCompleteResponse | None:
    """ UCP checkout COMPLETE. Bridges the buyer's signed credential to the Terminal dispatcher authority
    and reuses the non-custodial settle path: the amount is re-derived server-side from the reservation
    and the rail adapter re-verifies the signature, seller, escrow, asset and amount before a cent
    moves. An x402_authorization captures to the merchant's pay_to; a boson_commit_authorization COMMITS
    the escrow with the buyer's own x402B signature (the redeem is deferred to the merchant fulfillment
    webhook). The checkout id comes from the spec-correct /ucp/v1/checkout-sessions/{id}/complete path
    form, or the legacy `checkout_id` body field. Public + activation-exempt; 404 until
    FACET_UCP_ENABLED. RFC 9421 ES256-signed (a Boson commit REQUIRES a verified platform signature).

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCompleteRequest): A UCP checkout complete request (POST /ucp/v1/checkout-
            sessions/complete, or the spec-correct /{id}/complete). Bridges the buyer's credential to
            the Terminal dispatcher authority. x402 captures; a boson_commit_authorization COMMITS the
            escrow with the buyer's own x402B signature (funds escrow into the Diamond) and the redeem
            is deferred to the merchant fulfillment webhook. Money movement reuses the non-custodial
            settle path: the amount is re-derived server-side from the reservation and the rail
            adapter re-verifies the signature, seller, escrow, asset and amount before a cent moves.

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
    body: UcpCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCompleteResponse]:
    """ UCP checkout COMPLETE. Bridges the buyer's signed credential to the Terminal dispatcher authority
    and reuses the non-custodial settle path: the amount is re-derived server-side from the reservation
    and the rail adapter re-verifies the signature, seller, escrow, asset and amount before a cent
    moves. An x402_authorization captures to the merchant's pay_to; a boson_commit_authorization COMMITS
    the escrow with the buyer's own x402B signature (the redeem is deferred to the merchant fulfillment
    webhook). The checkout id comes from the spec-correct /ucp/v1/checkout-sessions/{id}/complete path
    form, or the legacy `checkout_id` body field. Public + activation-exempt; 404 until
    FACET_UCP_ENABLED. RFC 9421 ES256-signed (a Boson commit REQUIRES a verified platform signature).

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCompleteRequest): A UCP checkout complete request (POST /ucp/v1/checkout-
            sessions/complete, or the spec-correct /{id}/complete). Bridges the buyer's credential to
            the Terminal dispatcher authority. x402 captures; a boson_commit_authorization COMMITS the
            escrow with the buyer's own x402B signature (funds escrow into the Diamond) and the redeem
            is deferred to the merchant fulfillment webhook. Money movement reuses the non-custodial
            settle path: the amount is re-derived server-side from the reservation and the rail
            adapter re-verifies the signature, seller, escrow, asset and amount before a cent moves.

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
    body: UcpCheckoutCompleteRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCompleteResponse | None:
    """ UCP checkout COMPLETE. Bridges the buyer's signed credential to the Terminal dispatcher authority
    and reuses the non-custodial settle path: the amount is re-derived server-side from the reservation
    and the rail adapter re-verifies the signature, seller, escrow, asset and amount before a cent
    moves. An x402_authorization captures to the merchant's pay_to; a boson_commit_authorization COMMITS
    the escrow with the buyer's own x402B signature (the redeem is deferred to the merchant fulfillment
    webhook). The checkout id comes from the spec-correct /ucp/v1/checkout-sessions/{id}/complete path
    form, or the legacy `checkout_id` body field. Public + activation-exempt; 404 until
    FACET_UCP_ENABLED. RFC 9421 ES256-signed (a Boson commit REQUIRES a verified platform signature).

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutCompleteRequest): A UCP checkout complete request (POST /ucp/v1/checkout-
            sessions/complete, or the spec-correct /{id}/complete). Bridges the buyer's credential to
            the Terminal dispatcher authority. x402 captures; a boson_commit_authorization COMMITS the
            escrow with the buyer's own x402B signature (funds escrow into the Diamond) and the redeem
            is deferred to the merchant fulfillment webhook. Money movement reuses the non-custodial
            settle path: the amount is re-derived server-side from the reservation and the rail
            adapter re-verifies the signature, seller, escrow, asset and amount before a cent moves.

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
