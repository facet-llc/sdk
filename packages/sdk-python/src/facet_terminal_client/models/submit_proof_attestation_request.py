from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.proof_kind import ProofKind
from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitProofAttestationRequest")



@_attrs_define
class SubmitProofAttestationRequest:
    """ 
        Attributes:
            proof_kind (ProofKind):
            issuer (str):
            jws (str): Compact JWS — 3 base64url segments separated by '.'.
            expires_at (str | Unset): ISO 8601.
     """

    proof_kind: ProofKind
    issuer: str
    jws: str
    expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        proof_kind = self.proof_kind.value

        issuer = self.issuer

        jws = self.jws

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "proof_kind": proof_kind,
            "issuer": issuer,
            "jws": jws,
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proof_kind = ProofKind(d.pop("proof_kind"))




        issuer = d.pop("issuer")

        jws = d.pop("jws")

        expires_at = d.pop("expires_at", UNSET)

        submit_proof_attestation_request = cls(
            proof_kind=proof_kind,
            issuer=issuer,
            jws=jws,
            expires_at=expires_at,
        )


        submit_proof_attestation_request.additional_properties = d
        return submit_proof_attestation_request

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
