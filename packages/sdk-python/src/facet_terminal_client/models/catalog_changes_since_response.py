from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.catalog_change import CatalogChange





T = TypeVar("T", bound="CatalogChangesSinceResponse")



@_attrs_define
class CatalogChangesSinceResponse:
    """ 
        Attributes:
            changes (list[CatalogChange]):
            next_cursor (None | str):
     """

    changes: list[CatalogChange]
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_change import CatalogChange
        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "changes": changes,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_change import CatalogChange
        d = dict(src_dict)
        changes = []
        _changes = d.pop("changes")
        for changes_item_data in (_changes):
            changes_item = CatalogChange.from_dict(changes_item_data)



            changes.append(changes_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        catalog_changes_since_response = cls(
            changes=changes,
            next_cursor=next_cursor,
        )


        catalog_changes_since_response.additional_properties = d
        return catalog_changes_since_response

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
