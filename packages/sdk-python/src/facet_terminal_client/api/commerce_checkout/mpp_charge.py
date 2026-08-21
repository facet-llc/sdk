from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.mpp_charge_request import MppChargeRequest
from ...models.mpp_charge_response import MppChargeResponse
from ...models.mpp_problem import MppProblem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: MppChargeRequest,
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
        "url": "/mpp/v1/charges",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | MppChargeResponse | MppProblem | None:
    if response.status_code == 200:
        response_200 = MppChargeResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = FacetErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = FacetErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = MppProblem.from_dict(response.json())



        return response_402

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | MppChargeResponse | MppProblem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MppChargeRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | MppChargeResponse | MppProblem]:
    r""" Machine Payments Protocol charge (mpp.dev). Charges an existing Facet reservation over MPP's
    challenge / credential / receipt envelope, settling through the SAME non-custodial x402 path as the
    UCP checkout: the buyer signs one ERC-3009 transferWithAuthorization straight to the merchant's own
    payout address. Send with no credential to receive a 402 carrying `WWW-Authenticate: Payment id=...,
    realm=..., method=\"evm\", intent=\"charge\", request=<base64url>`; sign the authorization with
    nonce keccak256(challenge.id || challenge.realm) and re-send it as `Authorization: Payment
    <base64url>`. A 200 carries the receipt on `Payment-Receipt`. IDENTITY: this route is
    unauthenticated BY PROTOCOL DESIGN. MPP puts the credential on the Authorization header under the
    `Payment` scheme, so a Facet KYA cannot ride the same header, and the 402 IS the authentication
    challenge. Identity is bound more strongly elsewhere: the reservation was created under an
    authenticated KYA, the unguessable reservation id is the capability, and the settlement executes as
    the reservation's own agent. Every refusal answers 402 with a FRESH challenge, never a 4xx-other.
    Amount, recipient, chain and currency are server-resolved from the reservation and the merchant's
    sites row, never the request. Returns 404 until the operator enables MPP via FACET_MPP_ENABLED with
    a FACET_MPP_SECRET_KEY of at least 32 bytes.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (MppChargeRequest): Charge an existing reservation over the Machine Payments
            Protocol. Send it with no `Authorization: Payment` credential to receive the 402
            challenge, then re-send with the signed credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | MppChargeResponse | MppProblem]
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
    body: MppChargeRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | MppChargeResponse | MppProblem | None:
    r""" Machine Payments Protocol charge (mpp.dev). Charges an existing Facet reservation over MPP's
    challenge / credential / receipt envelope, settling through the SAME non-custodial x402 path as the
    UCP checkout: the buyer signs one ERC-3009 transferWithAuthorization straight to the merchant's own
    payout address. Send with no credential to receive a 402 carrying `WWW-Authenticate: Payment id=...,
    realm=..., method=\"evm\", intent=\"charge\", request=<base64url>`; sign the authorization with
    nonce keccak256(challenge.id || challenge.realm) and re-send it as `Authorization: Payment
    <base64url>`. A 200 carries the receipt on `Payment-Receipt`. IDENTITY: this route is
    unauthenticated BY PROTOCOL DESIGN. MPP puts the credential on the Authorization header under the
    `Payment` scheme, so a Facet KYA cannot ride the same header, and the 402 IS the authentication
    challenge. Identity is bound more strongly elsewhere: the reservation was created under an
    authenticated KYA, the unguessable reservation id is the capability, and the settlement executes as
    the reservation's own agent. Every refusal answers 402 with a FRESH challenge, never a 4xx-other.
    Amount, recipient, chain and currency are server-resolved from the reservation and the merchant's
    sites row, never the request. Returns 404 until the operator enables MPP via FACET_MPP_ENABLED with
    a FACET_MPP_SECRET_KEY of at least 32 bytes.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (MppChargeRequest): Charge an existing reservation over the Machine Payments
            Protocol. Send it with no `Authorization: Payment` credential to receive the 402
            challenge, then re-send with the signed credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | MppChargeResponse | MppProblem
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
    body: MppChargeRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | MppChargeResponse | MppProblem]:
    r""" Machine Payments Protocol charge (mpp.dev). Charges an existing Facet reservation over MPP's
    challenge / credential / receipt envelope, settling through the SAME non-custodial x402 path as the
    UCP checkout: the buyer signs one ERC-3009 transferWithAuthorization straight to the merchant's own
    payout address. Send with no credential to receive a 402 carrying `WWW-Authenticate: Payment id=...,
    realm=..., method=\"evm\", intent=\"charge\", request=<base64url>`; sign the authorization with
    nonce keccak256(challenge.id || challenge.realm) and re-send it as `Authorization: Payment
    <base64url>`. A 200 carries the receipt on `Payment-Receipt`. IDENTITY: this route is
    unauthenticated BY PROTOCOL DESIGN. MPP puts the credential on the Authorization header under the
    `Payment` scheme, so a Facet KYA cannot ride the same header, and the 402 IS the authentication
    challenge. Identity is bound more strongly elsewhere: the reservation was created under an
    authenticated KYA, the unguessable reservation id is the capability, and the settlement executes as
    the reservation's own agent. Every refusal answers 402 with a FRESH challenge, never a 4xx-other.
    Amount, recipient, chain and currency are server-resolved from the reservation and the merchant's
    sites row, never the request. Returns 404 until the operator enables MPP via FACET_MPP_ENABLED with
    a FACET_MPP_SECRET_KEY of at least 32 bytes.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (MppChargeRequest): Charge an existing reservation over the Machine Payments
            Protocol. Send it with no `Authorization: Payment` credential to receive the 402
            challenge, then re-send with the signed credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | MppChargeResponse | MppProblem]
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
    body: MppChargeRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | MppChargeResponse | MppProblem | None:
    r""" Machine Payments Protocol charge (mpp.dev). Charges an existing Facet reservation over MPP's
    challenge / credential / receipt envelope, settling through the SAME non-custodial x402 path as the
    UCP checkout: the buyer signs one ERC-3009 transferWithAuthorization straight to the merchant's own
    payout address. Send with no credential to receive a 402 carrying `WWW-Authenticate: Payment id=...,
    realm=..., method=\"evm\", intent=\"charge\", request=<base64url>`; sign the authorization with
    nonce keccak256(challenge.id || challenge.realm) and re-send it as `Authorization: Payment
    <base64url>`. A 200 carries the receipt on `Payment-Receipt`. IDENTITY: this route is
    unauthenticated BY PROTOCOL DESIGN. MPP puts the credential on the Authorization header under the
    `Payment` scheme, so a Facet KYA cannot ride the same header, and the 402 IS the authentication
    challenge. Identity is bound more strongly elsewhere: the reservation was created under an
    authenticated KYA, the unguessable reservation id is the capability, and the settlement executes as
    the reservation's own agent. Every refusal answers 402 with a FRESH challenge, never a 4xx-other.
    Amount, recipient, chain and currency are server-resolved from the reservation and the merchant's
    sites row, never the request. Returns 404 until the operator enables MPP via FACET_MPP_ENABLED with
    a FACET_MPP_SECRET_KEY of at least 32 bytes.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (MppChargeRequest): Charge an existing reservation over the Machine Payments
            Protocol. Send it with no `Authorization: Payment` credential to receive the 402
            challenge, then re-send with the signed credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | MppChargeResponse | MppProblem
     """


    return (await asyncio_detailed(
        client=client,
body=body,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
