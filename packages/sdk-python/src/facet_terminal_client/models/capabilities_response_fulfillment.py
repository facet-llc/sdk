from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.capabilities_response_fulfillment_modes_item import CapabilitiesResponseFulfillmentModesItem
from typing import cast






T = TypeVar("T", bound="CapabilitiesResponseFulfillment")



@_attrs_define
class CapabilitiesResponseFulfillment:
    """ 
        Attributes:
            enabled (bool):
            required_for_physical (bool):
            modes (list[CapabilitiesResponseFulfillmentModesItem]):
     """

    enabled: bool
    required_for_physical: bool
    modes: list[CapabilitiesResponseFulfillmentModesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        required_for_physical = self.required_for_physical

        modes = []
        for modes_item_data in self.modes:
            modes_item = modes_item_data.value
            modes.append(modes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "enabled": enabled,
            "required_for_physical": required_for_physical,
            "modes": modes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        required_for_physical = d.pop("required_for_physical")

        modes = []
        _modes = d.pop("modes")
        for modes_item_data in (_modes):
            modes_item = CapabilitiesResponseFulfillmentModesItem(modes_item_data)



            modes.append(modes_item)


        capabilities_response_fulfillment = cls(
            enabled=enabled,
            required_for_physical=required_for_physical,
            modes=modes,
        )


        capabilities_response_fulfillment.additional_properties = d
        return capabilities_response_fulfillment

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
