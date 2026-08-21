from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_escrow_buyer_cancel_already_refunded_phase import OpenEscrowBuyerCancelAlreadyRefundedPhase
from ..models.open_escrow_buyer_cancel_already_refunded_status import OpenEscrowBuyerCancelAlreadyRefundedStatus






T = TypeVar("T", bound="OpenEscrowBuyerCancelAlreadyRefunded")



@_attrs_define
class OpenEscrowBuyerCancelAlreadyRefunded:
    """ 
        Attributes:
            field_status (OpenEscrowBuyerCancelAlreadyRefundedStatus):
            phase (OpenEscrowBuyerCancelAlreadyRefundedPhase):
            escrow_id (str):
     """

    field_status: OpenEscrowBuyerCancelAlreadyRefundedStatus
    phase: OpenEscrowBuyerCancelAlreadyRefundedPhase
    escrow_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_status = self.field_status.value

        phase = self.phase.value

        escrow_id = self.escrow_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "_status": field_status,
            "phase": phase,
            "escrowId": escrow_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_status = OpenEscrowBuyerCancelAlreadyRefundedStatus(d.pop("_status"))




        phase = OpenEscrowBuyerCancelAlreadyRefundedPhase(d.pop("phase"))




        escrow_id = d.pop("escrowId")

        open_escrow_buyer_cancel_already_refunded = cls(
            field_status=field_status,
            phase=phase,
            escrow_id=escrow_id,
        )


        open_escrow_buyer_cancel_already_refunded.additional_properties = d
        return open_escrow_buyer_cancel_already_refunded

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
