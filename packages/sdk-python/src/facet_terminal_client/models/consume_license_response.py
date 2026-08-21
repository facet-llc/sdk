from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ConsumeLicenseResponse")



@_attrs_define
class ConsumeLicenseResponse:
    """ 
        Attributes:
            license_id (str):
            scope (str):
            usage_count (int):
            usage_limit (int | None):
            expires_at (str):
     """

    license_id: str
    scope: str
    usage_count: int
    usage_limit: int | None
    expires_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        license_id = self.license_id

        scope = self.scope

        usage_count = self.usage_count

        usage_limit: int | None
        usage_limit = self.usage_limit

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "license_id": license_id,
            "scope": scope,
            "usage_count": usage_count,
            "usage_limit": usage_limit,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_id = d.pop("license_id")

        scope = d.pop("scope")

        usage_count = d.pop("usage_count")

        def _parse_usage_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        usage_limit = _parse_usage_limit(d.pop("usage_limit"))


        expires_at = d.pop("expires_at")

        consume_license_response = cls(
            license_id=license_id,
            scope=scope,
            usage_count=usage_count,
            usage_limit=usage_limit,
            expires_at=expires_at,
        )


        consume_license_response.additional_properties = d
        return consume_license_response

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
