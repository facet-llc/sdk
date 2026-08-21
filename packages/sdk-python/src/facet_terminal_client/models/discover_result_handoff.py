from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DiscoverResultHandoff")



@_attrs_define
class DiscoverResultHandoff:
    """ 
        Attributes:
            phone (None | str):
            directions_url (None | str): https://www.google.com/maps/dir/?api=1&destination=<lat>,<lng>.
     """

    phone: None | str
    directions_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        phone: None | str
        phone = self.phone

        directions_url: None | str
        directions_url = self.directions_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "phone": phone,
            "directions_url": directions_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))


        def _parse_directions_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        directions_url = _parse_directions_url(d.pop("directions_url"))


        discover_result_handoff = cls(
            phone=phone,
            directions_url=directions_url,
        )


        discover_result_handoff.additional_properties = d
        return discover_result_handoff

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
