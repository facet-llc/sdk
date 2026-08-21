from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.stores_response_stores_item import StoresResponseStoresItem





T = TypeVar("T", bound="StoresResponse")



@_attrs_define
class StoresResponse:
    """ 
        Attributes:
            count (int): Number of live, verified merchants a buyer can check out at right now.
            stores (list[StoresResponseStoresItem]): The live, verified merchants, sorted by name.
            live (bool): False when no database is configured (stores is then empty).
     """

    count: int
    stores: list[StoresResponseStoresItem]
    live: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stores_response_stores_item import StoresResponseStoresItem
        count = self.count

        stores = []
        for stores_item_data in self.stores:
            stores_item = stores_item_data.to_dict()
            stores.append(stores_item)



        live = self.live


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "count": count,
            "stores": stores,
            "live": live,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stores_response_stores_item import StoresResponseStoresItem
        d = dict(src_dict)
        count = d.pop("count")

        stores = []
        _stores = d.pop("stores")
        for stores_item_data in (_stores):
            stores_item = StoresResponseStoresItem.from_dict(stores_item_data)



            stores.append(stores_item)


        live = d.pop("live")

        stores_response = cls(
            count=count,
            stores=stores,
            live=live,
        )


        stores_response.additional_properties = d
        return stores_response

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
