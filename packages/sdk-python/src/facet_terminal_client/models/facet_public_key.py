from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.facet_public_key_alg import FacetPublicKeyAlg






T = TypeVar("T", bound="FacetPublicKey")



@_attrs_define
class FacetPublicKey:
    """ 
        Attributes:
            kid (str):
            alg (FacetPublicKeyAlg):
            public_key_b64 (str): Raw 32-byte public key, base64url.
     """

    kid: str
    alg: FacetPublicKeyAlg
    public_key_b64: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kid = self.kid

        alg = self.alg.value

        public_key_b64 = self.public_key_b64


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kid": kid,
            "alg": alg,
            "public_key_b64": public_key_b64,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kid = d.pop("kid")

        alg = FacetPublicKeyAlg(d.pop("alg"))




        public_key_b64 = d.pop("public_key_b64")

        facet_public_key = cls(
            kid=kid,
            alg=alg,
            public_key_b64=public_key_b64,
        )


        facet_public_key.additional_properties = d
        return facet_public_key

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
