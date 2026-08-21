from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.attestation_party import AttestationParty
from ..models.register_attestation_key_response_status import RegisterAttestationKeyResponseStatus






T = TypeVar("T", bound="RegisterAttestationKeyResponse")



@_attrs_define
class RegisterAttestationKeyResponse:
    """ 
        Attributes:
            registered (bool): Always true on this branch.
            party (AttestationParty):
            subject_ref (str): Who the key speaks for: the agent aid, or the site id for a merchant. Always derived from the
                authenticated principal, never the request body.
            kid (str):
            status (RegisterAttestationKeyResponseStatus):
     """

    registered: bool
    party: AttestationParty
    subject_ref: str
    kid: str
    status: RegisterAttestationKeyResponseStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        registered = self.registered

        party = self.party.value

        subject_ref = self.subject_ref

        kid = self.kid

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "registered": registered,
            "party": party,
            "subject_ref": subject_ref,
            "kid": kid,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registered = d.pop("registered")

        party = AttestationParty(d.pop("party"))




        subject_ref = d.pop("subject_ref")

        kid = d.pop("kid")

        status = RegisterAttestationKeyResponseStatus(d.pop("status"))




        register_attestation_key_response = cls(
            registered=registered,
            party=party,
            subject_ref=subject_ref,
            kid=kid,
            status=status,
        )


        register_attestation_key_response.additional_properties = d
        return register_attestation_key_response

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
