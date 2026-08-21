from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.catalog_change_action import CatalogChangeAction
from ..models.catalog_change_kind import CatalogChangeKind






T = TypeVar("T", bound="CatalogChange")



@_attrs_define
class CatalogChange:
    """ 
        Attributes:
            kind (CatalogChangeKind):
            action (CatalogChangeAction):
            id (str):
            product_id (str): Empty string when kind='manifest'.
            updated_at (str): ISO 8601.
     """

    kind: CatalogChangeKind
    action: CatalogChangeAction
    id: str
    product_id: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        action = self.action.value

        id = self.id

        product_id = self.product_id

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "action": action,
            "id": id,
            "product_id": product_id,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = CatalogChangeKind(d.pop("kind"))




        action = CatalogChangeAction(d.pop("action"))




        id = d.pop("id")

        product_id = d.pop("product_id")

        updated_at = d.pop("updated_at")

        catalog_change = cls(
            kind=kind,
            action=action,
            id=id,
            product_id=product_id,
            updated_at=updated_at,
        )


        catalog_change.additional_properties = d
        return catalog_change

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
