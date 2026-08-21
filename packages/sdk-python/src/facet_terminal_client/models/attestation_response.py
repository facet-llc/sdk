from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.attestation_party import AttestationParty
from ..models.attestation_response_attestation import AttestationResponseAttestation
from ..models.attestation_response_strength import AttestationResponseStrength






T = TypeVar("T", bound="AttestationResponse")



@_attrs_define
class AttestationResponse:
    """ 
        Attributes:
            recorded (bool): Always true on this branch.
            party (AttestationParty):
            attestation (AttestationResponseAttestation):
            this_hash (str):
            kid (str): Which registered key the signature was verified against. Echoed because it is the first thing a
                caller needs when debugging a rejection.
            strength (AttestationResponseStrength): Always 'signed' from these routes: the attestation was verified against
                a registered key. The field exists so a future session-authority path would be visibly weaker rather than
                silently counted alongside verified signatures.
            idempotent (bool): True when this party had already attested to this entry.
     """

    recorded: bool
    party: AttestationParty
    attestation: AttestationResponseAttestation
    this_hash: str
    kid: str
    strength: AttestationResponseStrength
    idempotent: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        recorded = self.recorded

        party = self.party.value

        attestation = self.attestation.value

        this_hash = self.this_hash

        kid = self.kid

        strength = self.strength.value

        idempotent = self.idempotent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "recorded": recorded,
            "party": party,
            "attestation": attestation,
            "this_hash": this_hash,
            "kid": kid,
            "strength": strength,
            "idempotent": idempotent,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recorded = d.pop("recorded")

        party = AttestationParty(d.pop("party"))




        attestation = AttestationResponseAttestation(d.pop("attestation"))




        this_hash = d.pop("this_hash")

        kid = d.pop("kid")

        strength = AttestationResponseStrength(d.pop("strength"))




        idempotent = d.pop("idempotent")

        attestation_response = cls(
            recorded=recorded,
            party=party,
            attestation=attestation,
            this_hash=this_hash,
            kid=kid,
            strength=strength,
            idempotent=idempotent,
        )


        attestation_response.additional_properties = d
        return attestation_response

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
