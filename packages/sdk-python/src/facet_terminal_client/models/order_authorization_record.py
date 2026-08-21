from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_authorization_record_kind import OrderAuthorizationRecordKind
from ..models.order_authorization_record_leg import OrderAuthorizationRecordLeg
from ..models.order_authorization_record_verification import OrderAuthorizationRecordVerification
from typing import cast






T = TypeVar("T", bound="OrderAuthorizationRecord")



@_attrs_define
class OrderAuthorizationRecord:
    """ One row of the inbound authorization ledger: a credential the counterparty presented and Facet verified (or, for the
    Boson seller offer, attested). `artifact` is the credential verbatim for the RFC 9421 platform signature, the
    ERC-3009 authorization, and the seller offer, and is always null for a KYA, whose value is never returned;
    `artifact_sha256` (hex) is the KYA's integrity anchor. The encrypted-at-rest KYA slot is never exposed.

        Attributes:
            leg (OrderAuthorizationRecordLeg):
            kind (OrderAuthorizationRecordKind):
            verification (OrderAuthorizationRecordVerification):
            subject_ref (None | str):
            profile_origin (None | str):
            artifact (None | str):
            artifact_input (None | str):
            content_digest (None | str):
            artifact_sha256 (None | str):
            recorded_at (str):
     """

    leg: OrderAuthorizationRecordLeg
    kind: OrderAuthorizationRecordKind
    verification: OrderAuthorizationRecordVerification
    subject_ref: None | str
    profile_origin: None | str
    artifact: None | str
    artifact_input: None | str
    content_digest: None | str
    artifact_sha256: None | str
    recorded_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        leg = self.leg.value

        kind = self.kind.value

        verification = self.verification.value

        subject_ref: None | str
        subject_ref = self.subject_ref

        profile_origin: None | str
        profile_origin = self.profile_origin

        artifact: None | str
        artifact = self.artifact

        artifact_input: None | str
        artifact_input = self.artifact_input

        content_digest: None | str
        content_digest = self.content_digest

        artifact_sha256: None | str
        artifact_sha256 = self.artifact_sha256

        recorded_at = self.recorded_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "leg": leg,
            "kind": kind,
            "verification": verification,
            "subject_ref": subject_ref,
            "profile_origin": profile_origin,
            "artifact": artifact,
            "artifact_input": artifact_input,
            "content_digest": content_digest,
            "artifact_sha256": artifact_sha256,
            "recorded_at": recorded_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        leg = OrderAuthorizationRecordLeg(d.pop("leg"))




        kind = OrderAuthorizationRecordKind(d.pop("kind"))




        verification = OrderAuthorizationRecordVerification(d.pop("verification"))




        def _parse_subject_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject_ref = _parse_subject_ref(d.pop("subject_ref"))


        def _parse_profile_origin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_origin = _parse_profile_origin(d.pop("profile_origin"))


        def _parse_artifact(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        artifact = _parse_artifact(d.pop("artifact"))


        def _parse_artifact_input(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        artifact_input = _parse_artifact_input(d.pop("artifact_input"))


        def _parse_content_digest(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_digest = _parse_content_digest(d.pop("content_digest"))


        def _parse_artifact_sha256(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        artifact_sha256 = _parse_artifact_sha256(d.pop("artifact_sha256"))


        recorded_at = d.pop("recorded_at")

        order_authorization_record = cls(
            leg=leg,
            kind=kind,
            verification=verification,
            subject_ref=subject_ref,
            profile_origin=profile_origin,
            artifact=artifact,
            artifact_input=artifact_input,
            content_digest=content_digest,
            artifact_sha256=artifact_sha256,
            recorded_at=recorded_at,
        )


        order_authorization_record.additional_properties = d
        return order_authorization_record

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
