from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OpenEscrowBuyerCancelRequest")



@_attrs_define
class OpenEscrowBuyerCancelRequest:
    """ Agent (Facet KYA bearer): the stored on-chain buyer cancels a not-yet-shipped escrow for a FULL refund, in two self-
    broadcast phases. Non-custodial: Facet signs only the refund-authorization and broadcasts nothing.

        Attributes:
            escrow_id (str): 32-byte 0x hex escrow id to cancel; must belong to the authenticated agent.
            reason (str | Unset): Optional free-text reason; keccak256-hashed into the evidence hash. Any body-supplied
                amount is ignored; the refund is the full server-derived snapshot amount.
     """

    escrow_id: str
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        escrow_id = self.escrow_id

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "escrowId": escrow_id,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escrow_id = d.pop("escrowId")

        reason = d.pop("reason", UNSET)

        open_escrow_buyer_cancel_request = cls(
            escrow_id=escrow_id,
            reason=reason,
        )


        open_escrow_buyer_cancel_request.additional_properties = d
        return open_escrow_buyer_cancel_request

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
