from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.ucp_checkout_create_response import UcpCheckoutCreateResponse
from ...models.ucp_checkout_session_cancel_request import UcpCheckoutSessionCancelRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UcpCheckoutSessionCancelRequest,
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
        "url": "/ucp/v1/checkout-sessions/:id/cancel",
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
    body: UcpCheckoutSessionCancelRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]:
    """ UCP checkout SESSION-cancel (pre-completion). Releases the reservation's inventory hold and returns
    the session with status canceled plus a messages[] note. Owner-scoped (404 on missing/foreign) and
    idempotent (a second cancel returns the canceled snapshot). DISTINCT from POST /ucp/v1/checkout-
    sessions/cancel, which is the post-commit Boson ESCROW cancel of a committed exchange: this releases
    a hold and moves no money. Public + activation-exempt; 404 until FACET_UCP_ENABLED.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutSessionCancelRequest): A UCP checkout SESSION-cancel request (POST
            /ucp/v1/checkout-sessions/:id/cancel). The body is empty; the checkout id comes from the
            path. Releases the reservation's inventory hold pre-completion (idempotent). Distinct from
            POST /ucp/v1/checkout-sessions/cancel, which is the post-commit Boson escrow cancel of a
            committed exchange.

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
    body: UcpCheckoutSessionCancelRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCreateResponse | None:
    """ UCP checkout SESSION-cancel (pre-completion). Releases the reservation's inventory hold and returns
    the session with status canceled plus a messages[] note. Owner-scoped (404 on missing/foreign) and
    idempotent (a second cancel returns the canceled snapshot). DISTINCT from POST /ucp/v1/checkout-
    sessions/cancel, which is the post-commit Boson ESCROW cancel of a committed exchange: this releases
    a hold and moves no money. Public + activation-exempt; 404 until FACET_UCP_ENABLED.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutSessionCancelRequest): A UCP checkout SESSION-cancel request (POST
            /ucp/v1/checkout-sessions/:id/cancel). The body is empty; the checkout id comes from the
            path. Releases the reservation's inventory hold pre-completion (idempotent). Distinct from
            POST /ucp/v1/checkout-sessions/cancel, which is the post-commit Boson escrow cancel of a
            committed exchange.

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
    body: UcpCheckoutSessionCancelRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> Response[FacetErrorEnvelope | UcpCheckoutCreateResponse]:
    """ UCP checkout SESSION-cancel (pre-completion). Releases the reservation's inventory hold and returns
    the session with status canceled plus a messages[] note. Owner-scoped (404 on missing/foreign) and
    idempotent (a second cancel returns the canceled snapshot). DISTINCT from POST /ucp/v1/checkout-
    sessions/cancel, which is the post-commit Boson ESCROW cancel of a committed exchange: this releases
    a hold and moves no money. Public + activation-exempt; 404 until FACET_UCP_ENABLED.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutSessionCancelRequest): A UCP checkout SESSION-cancel request (POST
            /ucp/v1/checkout-sessions/:id/cancel). The body is empty; the checkout id comes from the
            path. Releases the reservation's inventory hold pre-completion (idempotent). Distinct from
            POST /ucp/v1/checkout-sessions/cancel, which is the post-commit Boson escrow cancel of a
            committed exchange.

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
    body: UcpCheckoutSessionCancelRequest,
    accept: str | Unset = 'application/vnd.facet+json; version=0.2',
    x_facet_trace_id: str | Unset = UNSET,

) -> FacetErrorEnvelope | UcpCheckoutCreateResponse | None:
    """ UCP checkout SESSION-cancel (pre-completion). Releases the reservation's inventory hold and returns
    the session with status canceled plus a messages[] note. Owner-scoped (404 on missing/foreign) and
    idempotent (a second cancel returns the canceled snapshot). DISTINCT from POST /ucp/v1/checkout-
    sessions/cancel, which is the post-commit Boson ESCROW cancel of a committed exchange: this releases
    a hold and moves no money. Public + activation-exempt; 404 until FACET_UCP_ENABLED.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):
        body (UcpCheckoutSessionCancelRequest): A UCP checkout SESSION-cancel request (POST
            /ucp/v1/checkout-sessions/:id/cancel). The body is empty; the checkout id comes from the
            path. Releases the reservation's inventory hold pre-completion (idempotent). Distinct from
            POST /ucp/v1/checkout-sessions/cancel, which is the post-commit Boson escrow cancel of a
            committed exchange.

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
