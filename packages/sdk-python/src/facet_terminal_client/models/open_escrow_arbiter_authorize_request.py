from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OpenEscrowArbiterAuthorizeRequest")



@_attrs_define
class OpenEscrowArbiterAuthorizeRequest:
    """ Internal (Facet operator): authorize a split of ONE Disputed OpenEscrow escrow. The arbiter binds the STORED on-
    chain payer/merchant (never a caller field) and caps the refund at the escrow amount. Facet signs only; it
    broadcasts nothing.

        Attributes:
            escrow_id (str): 32-byte 0x hex escrow id of the disputed escrow to split.
            refund_amount_minor (int): Refund amount in USD cents (positive integer). Scaled x10000 to USDC base units and
                capped at the on-chain escrow amount.
            evidence_hash (str | Unset): Optional 32-byte 0x hex evidence hash; defaults to keccak256('') when omitted.
     """

    escrow_id: str
    refund_amount_minor: int
    evidence_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        escrow_id = self.escrow_id

        refund_amount_minor = self.refund_amount_minor

        evidence_hash = self.evidence_hash


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "escrowId": escrow_id,
            "refundAmountMinor": refund_amount_minor,
        })
        if evidence_hash is not UNSET:
            field_dict["evidenceHash"] = evidence_hash

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escrow_id = d.pop("escrowId")

        refund_amount_minor = d.pop("refundAmountMinor")

        evidence_hash = d.pop("evidenceHash", UNSET)

        open_escrow_arbiter_authorize_request = cls(
            escrow_id=escrow_id,
            refund_amount_minor=refund_amount_minor,
            evidence_hash=evidence_hash,
        )


        open_escrow_arbiter_authorize_request.additional_properties = d
        return open_escrow_arbiter_authorize_request

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
