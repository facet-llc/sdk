from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="HoldSlotRequest")



@_attrs_define
class HoldSlotRequest:
    """ 
        Attributes:
            resource_id (str):
            slot_id (str):
            hold_seconds (int | Unset):
     """

    resource_id: str
    slot_id: str
    hold_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        slot_id = self.slot_id

        hold_seconds = self.hold_seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "resource_id": resource_id,
            "slot_id": slot_id,
        })
        if hold_seconds is not UNSET:
            field_dict["hold_seconds"] = hold_seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        slot_id = d.pop("slot_id")

        hold_seconds = d.pop("hold_seconds", UNSET)

        hold_slot_request = cls(
            resource_id=resource_id,
            slot_id=slot_id,
            hold_seconds=hold_seconds,
        )


        hold_slot_request.additional_properties = d
        return hold_slot_request

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
