from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CancelBookingResponse")



@_attrs_define
class CancelBookingResponse:
    """ 
        Attributes:
            cancelled_at (str):
            refund_eligible (bool):
     """

    cancelled_at: str
    refund_eligible: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cancelled_at = self.cancelled_at

        refund_eligible = self.refund_eligible


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cancelled_at": cancelled_at,
            "refund_eligible": refund_eligible,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancelled_at = d.pop("cancelled_at")

        refund_eligible = d.pop("refund_eligible")

        cancel_booking_response = cls(
            cancelled_at=cancelled_at,
            refund_eligible=refund_eligible,
        )


        cancel_booking_response.additional_properties = d
        return cancel_booking_response

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
