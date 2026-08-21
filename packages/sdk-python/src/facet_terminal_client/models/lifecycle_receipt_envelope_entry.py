from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LifecycleReceiptEnvelopeEntry")



@_attrs_define
class LifecycleReceiptEnvelopeEntry:
    """ 
        Attributes:
            format_ (str): The JWS media type, "facet-lifecycle+jws". Routes a consumer to the lifecycle-receipt validator.
            jws (str): RFC 7515 EdDSA compact JWS over the lifecycle event. Verifiable by a stock JOSE library against the
                provider JWKS, with no callback to Facet.
            kid (str): The signing key id; selects the verifying key in the JWKS.
            provider_jwks (str): Hint URL for the verifying JWKS (the issuer's /.well-known/jwks.json). Non-normative: a
                pinned key set wins.
     """

    format_: str
    jws: str
    kid: str
    provider_jwks: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        jws = self.jws

        kid = self.kid

        provider_jwks = self.provider_jwks


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "format": format_,
            "jws": jws,
            "kid": kid,
            "provider_jwks": provider_jwks,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format")

        jws = d.pop("jws")

        kid = d.pop("kid")

        provider_jwks = d.pop("provider_jwks")

        lifecycle_receipt_envelope_entry = cls(
            format_=format_,
            jws=jws,
            kid=kid,
            provider_jwks=provider_jwks,
        )


        lifecycle_receipt_envelope_entry.additional_properties = d
        return lifecycle_receipt_envelope_entry

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
