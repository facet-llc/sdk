from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.attestation_party import AttestationParty






T = TypeVar("T", bound="RevokeAttestationKeyResponse")



@_attrs_define
class RevokeAttestationKeyResponse:
    """ 
        Attributes:
            revoked (bool): Always true on this branch.
            party (AttestationParty):
            kid (str):
            revoked_at (str): Attestations signed before this moment remain verifiable. Revocation stops future signing; it
                does not let a party unsay what they already said.
     """

    revoked: bool
    party: AttestationParty
    kid: str
    revoked_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        revoked = self.revoked

        party = self.party.value

        kid = self.kid

        revoked_at = self.revoked_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "revoked": revoked,
            "party": party,
            "kid": kid,
            "revoked_at": revoked_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revoked = d.pop("revoked")

        party = AttestationParty(d.pop("party"))




        kid = d.pop("kid")

        revoked_at = d.pop("revoked_at")

        revoke_attestation_key_response = cls(
            revoked=revoked,
            party=party,
            kid=kid,
            revoked_at=revoked_at,
        )


        revoke_attestation_key_response.additional_properties = d
        return revoke_attestation_key_response

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
