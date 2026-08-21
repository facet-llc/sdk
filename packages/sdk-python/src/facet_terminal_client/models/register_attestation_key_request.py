from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.attestation_party import AttestationParty
from ..types import UNSET, Unset






T = TypeVar("T", bound="RegisterAttestationKeyRequest")



@_attrs_define
class RegisterAttestationKeyRequest:
    """ 
        Attributes:
            party (AttestationParty):
            kid (str): Key id the signer will put in the JWS protected header.
            public_key (str): Raw 32-byte Ed25519 public key, base64url, as RFC 8037 publishes in 'x'.
            site_id (str | Unset): Required for party=merchant; the caller must administer it. Ignored for party=agent,
                whose subject is bound from the verified token.
     """

    party: AttestationParty
    kid: str
    public_key: str
    site_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        party = self.party.value

        kid = self.kid

        public_key = self.public_key

        site_id = self.site_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "party": party,
            "kid": kid,
            "public_key": public_key,
        })
        if site_id is not UNSET:
            field_dict["site_id"] = site_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party = AttestationParty(d.pop("party"))




        kid = d.pop("kid")

        public_key = d.pop("public_key")

        site_id = d.pop("site_id", UNSET)

        register_attestation_key_request = cls(
            party=party,
            kid=kid,
            public_key=public_key,
            site_id=site_id,
        )


        register_attestation_key_request.additional_properties = d
        return register_attestation_key_request

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
