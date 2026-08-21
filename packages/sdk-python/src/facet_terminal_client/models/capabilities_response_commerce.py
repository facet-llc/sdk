from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CapabilitiesResponseCommerce")



@_attrs_define
class CapabilitiesResponseCommerce:
    """ 
        Attributes:
            search (bool):
            quote (bool):
            reserve (bool):
            settle (bool):
     """

    search: bool
    quote: bool
    reserve: bool
    settle: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        search = self.search

        quote = self.quote

        reserve = self.reserve

        settle = self.settle


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "search": search,
            "quote": quote,
            "reserve": reserve,
            "settle": settle,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search = d.pop("search")

        quote = d.pop("quote")

        reserve = d.pop("reserve")

        settle = d.pop("settle")

        capabilities_response_commerce = cls(
            search=search,
            quote=quote,
            reserve=reserve,
            settle=settle,
        )


        capabilities_response_commerce.additional_properties = d
        return capabilities_response_commerce

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
