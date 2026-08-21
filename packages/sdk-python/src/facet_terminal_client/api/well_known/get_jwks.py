from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.facet_error_envelope import FacetErrorEnvelope
from ...models.jwks import Jwks
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
        "url": "/.well-known/jwks.json",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FacetErrorEnvelope | Jwks | None:
    if response.status_code == 200:
        response_200 = Jwks.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FacetErrorEnvelope | Jwks]:
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

) -> Response[FacetErrorEnvelope | Jwks]:
    r""" The same Ed25519 response-signing keys as a standards-compliant JWKS (RFC 7517 + RFC 8037),
    consumable by any JOSE library. /.well-known/facet-keys.json publishes the identical keys in a
    Facet-specific envelope whose field names no standard verifier can read: alg is \"Ed25519\" where
    RFC 8037 requires \"EdDSA\" (Ed25519 is the CURVE), the key material sits under public_key_b64
    rather than x, and kty and crv are absent entirely. Both endpoints serve the same key set and both
    remain supported; this one exists so that verifying a Facet-signed response does not require bespoke
    code, which for a signature whose whole purpose is third-party verification was close to self-
    defeating.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | Jwks]
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

) -> FacetErrorEnvelope | Jwks | None:
    r""" The same Ed25519 response-signing keys as a standards-compliant JWKS (RFC 7517 + RFC 8037),
    consumable by any JOSE library. /.well-known/facet-keys.json publishes the identical keys in a
    Facet-specific envelope whose field names no standard verifier can read: alg is \"Ed25519\" where
    RFC 8037 requires \"EdDSA\" (Ed25519 is the CURVE), the key material sits under public_key_b64
    rather than x, and kty and crv are absent entirely. Both endpoints serve the same key set and both
    remain supported; this one exists so that verifying a Facet-signed response does not require bespoke
    code, which for a signature whose whole purpose is third-party verification was close to self-
    defeating.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | Jwks
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

) -> Response[FacetErrorEnvelope | Jwks]:
    r""" The same Ed25519 response-signing keys as a standards-compliant JWKS (RFC 7517 + RFC 8037),
    consumable by any JOSE library. /.well-known/facet-keys.json publishes the identical keys in a
    Facet-specific envelope whose field names no standard verifier can read: alg is \"Ed25519\" where
    RFC 8037 requires \"EdDSA\" (Ed25519 is the CURVE), the key material sits under public_key_b64
    rather than x, and kty and crv are absent entirely. Both endpoints serve the same key set and both
    remain supported; this one exists so that verifying a Facet-signed response does not require bespoke
    code, which for a signature whose whole purpose is third-party verification was close to self-
    defeating.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacetErrorEnvelope | Jwks]
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

) -> FacetErrorEnvelope | Jwks | None:
    r""" The same Ed25519 response-signing keys as a standards-compliant JWKS (RFC 7517 + RFC 8037),
    consumable by any JOSE library. /.well-known/facet-keys.json publishes the identical keys in a
    Facet-specific envelope whose field names no standard verifier can read: alg is \"Ed25519\" where
    RFC 8037 requires \"EdDSA\" (Ed25519 is the CURVE), the key material sits under public_key_b64
    rather than x, and kty and crv are absent entirely. Both endpoints serve the same key set and both
    remain supported; this one exists so that verifying a Facet-signed response does not require bespoke
    code, which for a signature whose whole purpose is third-party verification was close to self-
    defeating.

    Args:
        accept (str | Unset):  Default: 'application/vnd.facet+json; version=0.2'.
        x_facet_trace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacetErrorEnvelope | Jwks
     """


    return (await asyncio_detailed(
        client=client,
accept=accept,
x_facet_trace_id=x_facet_trace_id,

    )).parsed
