from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReconcileSettlementsRequest")



@_attrs_define
class ReconcileSettlementsRequest:
    """ 
        Attributes:
            site_id (str): UUID. The caller must be an admin+ member of this site.
            grace_seconds (int | Unset): Only scan exchanges last updated at least this long ago (default + min bounded
                server-side).
            limit (int | Unset): Max stuck exchanges to scan in one pass (bounded server-side).
     """

    site_id: str
    grace_seconds: int | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        grace_seconds = self.grace_seconds

        limit = self.limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
        })
        if grace_seconds is not UNSET:
            field_dict["grace_seconds"] = grace_seconds
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        grace_seconds = d.pop("grace_seconds", UNSET)

        limit = d.pop("limit", UNSET)

        reconcile_settlements_request = cls(
            site_id=site_id,
            grace_seconds=grace_seconds,
            limit=limit,
        )


        reconcile_settlements_request.additional_properties = d
        return reconcile_settlements_request

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
