from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DisputeRuling")



@_attrs_define
class DisputeRuling:
    """ 
        Attributes:
            refund_id (str):
            order_id (str):
            ruling (str): 'uphold_buyer' or 'uphold_merchant'.
            evidence_hash (str): keccak256 of the canonical reconstructed evidence bundle.
            arbiter_id (str):
            ruling_body (str): The canonical body that was Ed25519-signed.
            signature (str): The Facet response signature over ruling_body, verifiable against the published JWKS.
            kid (str):
            trace_id (str): The trace id bound into the signed canonical string; required to reconstruct and verify the
                signature (method POST, path /v1/refund_adjudicate, this trace_id, sha256(ruling_body)).
            created_at (str):
            rationale (None | str | Unset):
     """

    refund_id: str
    order_id: str
    ruling: str
    evidence_hash: str
    arbiter_id: str
    ruling_body: str
    signature: str
    kid: str
    trace_id: str
    created_at: str
    rationale: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        refund_id = self.refund_id

        order_id = self.order_id

        ruling = self.ruling

        evidence_hash = self.evidence_hash

        arbiter_id = self.arbiter_id

        ruling_body = self.ruling_body

        signature = self.signature

        kid = self.kid

        trace_id = self.trace_id

        created_at = self.created_at

        rationale: None | str | Unset
        if isinstance(self.rationale, Unset):
            rationale = UNSET
        else:
            rationale = self.rationale


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refund_id": refund_id,
            "order_id": order_id,
            "ruling": ruling,
            "evidence_hash": evidence_hash,
            "arbiter_id": arbiter_id,
            "ruling_body": ruling_body,
            "signature": signature,
            "kid": kid,
            "trace_id": trace_id,
            "created_at": created_at,
        })
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refund_id = d.pop("refund_id")

        order_id = d.pop("order_id")

        ruling = d.pop("ruling")

        evidence_hash = d.pop("evidence_hash")

        arbiter_id = d.pop("arbiter_id")

        ruling_body = d.pop("ruling_body")

        signature = d.pop("signature")

        kid = d.pop("kid")

        trace_id = d.pop("trace_id")

        created_at = d.pop("created_at")

        def _parse_rationale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rationale = _parse_rationale(d.pop("rationale", UNSET))


        dispute_ruling = cls(
            refund_id=refund_id,
            order_id=order_id,
            ruling=ruling,
            evidence_hash=evidence_hash,
            arbiter_id=arbiter_id,
            ruling_body=ruling_body,
            signature=signature,
            kid=kid,
            trace_id=trace_id,
            created_at=created_at,
            rationale=rationale,
        )


        dispute_ruling.additional_properties = d
        return dispute_ruling

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
