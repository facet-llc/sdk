from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
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
        "url": "/orders/:id",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 404:
        response_404 = FacetErrorEnvelope.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = FacetErrorEnvelope.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | str]:
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

) -> Response[FacetErrorEnvelope | str]:
    """ Public, PII-minimal order receipt at the permalink returned by checkout-complete. A browser (Accept:
    text/html) gets an HTML receipt page; any other client gets the same non-PII fields as JSON: order
    id, status, amount, currency, rail, the settlement/charge reference, timestamps, the merchant name,
    and a pointer to POST /v1/get_receipt for the cryptographically signed receipt. The order id is an
    unguessable capability, so no KYA is required and a missing or malformed id returns the same
    NOT_FOUND. The recipient name, delivery address, gift/card message, buyer identity (aid), buyer
    wallet, email, and line items are NEVER exposed.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | str]
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

) -> FacetErrorEnvelope | str | None:
    """ Public, PII-minimal order receipt at the permalink returned by checkout-complete. A browser (Accept:
    text/html) gets an HTML receipt page; any other client gets the same non-PII fields as JSON: order
    id, status, amount, currency, rail, the settlement/charge reference, timestamps, the merchant name,
    and a pointer to POST /v1/get_receipt for the cryptographically signed receipt. The order id is an
    unguessable capability, so no KYA is required and a missing or malformed id returns the same
    NOT_FOUND. The recipient name, delivery address, gift/card message, buyer identity (aid), buyer
    wallet, email, and line items are NEVER exposed.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | str
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

) -> Response[FacetErrorEnvelope | str]:
    """ Public, PII-minimal order receipt at the permalink returned by checkout-complete. A browser (Accept:
    text/html) gets an HTML receipt page; any other client gets the same non-PII fields as JSON: order
    id, status, amount, currency, rail, the settlement/charge reference, timestamps, the merchant name,
    and a pointer to POST /v1/get_receipt for the cryptographically signed receipt. The order id is an
    unguessable capability, so no KYA is required and a missing or malformed id returns the same
    NOT_FOUND. The recipient name, delivery address, gift/card message, buyer identity (aid), buyer
    wallet, email, and line items are NEVER exposed.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | str]
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

) -> FacetErrorEnvelope | str | None:
    """ Public, PII-minimal order receipt at the permalink returned by checkout-complete. A browser (Accept:
    text/html) gets an HTML receipt page; any other client gets the same non-PII fields as JSON: order
    id, status, amount, currency, rail, the settlement/charge reference, timestamps, the merchant name,
    and a pointer to POST /v1/get_receipt for the cryptographically signed receipt. The order id is an
    unguessable capability, so no KYA is required and a missing or malformed id returns the same
    NOT_FOUND. The recipient name, delivery address, gift/card message, buyer identity (aid), buyer
    wallet, email, and line items are NEVER exposed.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | str
     """


    return (await asyncio_detailed(
        client=client,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
