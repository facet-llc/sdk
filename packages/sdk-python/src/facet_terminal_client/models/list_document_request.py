from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListDocumentRequest")



@_attrs_define
class ListDocumentRequest:
    """ 
        Attributes:
            site_id (str): UUID. The caller must be a viewer+ member of this site.
            product_id (str | Unset): Optional — narrow the listing to one product.
            limit (int | Unset):
            cursor (str | Unset):
     """

    site_id: str
    product_id: str | Unset = UNSET
    limit: int | Unset = UNSET
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        product_id = self.product_id

        limit = self.limit

        cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        product_id = d.pop("product_id", UNSET)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        list_document_request = cls(
            site_id=site_id,
            product_id=product_id,
            limit=limit,
            cursor=cursor,
        )


        list_document_request.additional_properties = d
        return list_document_request

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
