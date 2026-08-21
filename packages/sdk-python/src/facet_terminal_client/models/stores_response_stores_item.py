from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StoresResponseStoresItem")



@_attrs_define
class StoresResponseStoresItem:
    """ 
        Attributes:
            name (str): Merchant display name.
            storefront_url (str): The merchant's own website to browse (an https origin).
            terminal_url (str): The merchant's Facet Terminal base URL.
            handle (str | Unset): Merchant handle (subdomain label); omitted when unset.
            vertical (str | Unset): Business vertical, e.g. floral or retail.ecommerce; omitted when unset.
     """

    name: str
    storefront_url: str
    terminal_url: str
    handle: str | Unset = UNSET
    vertical: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        storefront_url = self.storefront_url

        terminal_url = self.terminal_url

        handle = self.handle

        vertical = self.vertical


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "storefront_url": storefront_url,
            "terminal_url": terminal_url,
        })
        if handle is not UNSET:
            field_dict["handle"] = handle
        if vertical is not UNSET:
            field_dict["vertical"] = vertical

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        storefront_url = d.pop("storefront_url")

        terminal_url = d.pop("terminal_url")

        handle = d.pop("handle", UNSET)

        vertical = d.pop("vertical", UNSET)

        stores_response_stores_item = cls(
            name=name,
            storefront_url=storefront_url,
            terminal_url=terminal_url,
            handle=handle,
            vertical=vertical,
        )


        stores_response_stores_item.additional_properties = d
        return stores_response_stores_item

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
