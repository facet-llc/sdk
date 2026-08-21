from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_attendee import BookingAttendee





T = TypeVar("T", bound="ConfirmBookingRequest")



@_attrs_define
class ConfirmBookingRequest:
    """ 
        Attributes:
            resource_id (str):
            slot_id (str):
            hold_token (str):
            attendee (BookingAttendee):
            deposit_kya_charge_id (str | Unset):
            notes (str | Unset):
     """

    resource_id: str
    slot_id: str
    hold_token: str
    attendee: BookingAttendee
    deposit_kya_charge_id: str | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_attendee import BookingAttendee
        resource_id = self.resource_id

        slot_id = self.slot_id

        hold_token = self.hold_token

        attendee = self.attendee.to_dict()

        deposit_kya_charge_id = self.deposit_kya_charge_id

        notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "resource_id": resource_id,
            "slot_id": slot_id,
            "hold_token": hold_token,
            "attendee": attendee,
        })
        if deposit_kya_charge_id is not UNSET:
            field_dict["deposit_kya_charge_id"] = deposit_kya_charge_id
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_attendee import BookingAttendee
        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        slot_id = d.pop("slot_id")

        hold_token = d.pop("hold_token")

        attendee = BookingAttendee.from_dict(d.pop("attendee"))




        deposit_kya_charge_id = d.pop("deposit_kya_charge_id", UNSET)

        notes = d.pop("notes", UNSET)

        confirm_booking_request = cls(
            resource_id=resource_id,
            slot_id=slot_id,
            hold_token=hold_token,
            attendee=attendee,
            deposit_kya_charge_id=deposit_kya_charge_id,
            notes=notes,
        )


        confirm_booking_request.additional_properties = d
        return confirm_booking_request

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
