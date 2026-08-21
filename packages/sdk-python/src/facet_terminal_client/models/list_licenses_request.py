from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListLicensesRequest")



@_attrs_define
class ListLicensesRequest:
    """ 
        Attributes:
            include_revoked (bool | Unset):
            limit (int | Unset):
            cursor (str | Unset):
     """

    include_revoked: bool | Unset = UNSET
    limit: int | Unset = UNSET
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        include_revoked = self.include_revoked

        limit = self.limit

        cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if include_revoked is not UNSET:
            field_dict["include_revoked"] = include_revoked
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_revoked = d.pop("include_revoked", UNSET)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        list_licenses_request = cls(
            include_revoked=include_revoked,
            limit=limit,
            cursor=cursor,
        )


        list_licenses_request.additional_properties = d
        return list_licenses_request

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
