from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AdapterSlot")



@_attrs_define
class AdapterSlot:
    """ 
        Attributes:
            external_slot_id (str):
            start_at (str): ISO 8601.
            end_at (str):
            capacity_total (int):
            capacity_remaining (int):
     """

    external_slot_id: str
    start_at: str
    end_at: str
    capacity_total: int
    capacity_remaining: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        external_slot_id = self.external_slot_id

        start_at = self.start_at

        end_at = self.end_at

        capacity_total = self.capacity_total

        capacity_remaining = self.capacity_remaining


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "external_slot_id": external_slot_id,
            "start_at": start_at,
            "end_at": end_at,
            "capacity_total": capacity_total,
            "capacity_remaining": capacity_remaining,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_slot_id = d.pop("external_slot_id")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        capacity_total = d.pop("capacity_total")

        capacity_remaining = d.pop("capacity_remaining")

        adapter_slot = cls(
            external_slot_id=external_slot_id,
            start_at=start_at,
            end_at=end_at,
            capacity_total=capacity_total,
            capacity_remaining=capacity_remaining,
        )


        adapter_slot.additional_properties = d
        return adapter_slot

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
