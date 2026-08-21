from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VisualSearchRequest")



@_attrs_define
class VisualSearchRequest:
    """ 
        Attributes:
            image_url (str): Buyer-supplied https image URL to match products against by visual similarity. Validated
                server-side (https-only + SSRF host guard rejecting internal / metadata / private targets) BEFORE any fetch; the
                URL and the fetched bytes are never persisted.
            limit (int | Unset): Page size (default 20, capped server-side at 50).
            offset (int | Unset): Page offset (default 0; forced to 0 on the credential-less public-safe path).
     """

    image_url: str
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        limit = self.limit

        offset = self.offset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "image_url": image_url,
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_url = d.pop("image_url")

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        visual_search_request = cls(
            image_url=image_url,
            limit=limit,
            offset=offset,
        )


        visual_search_request.additional_properties = d
        return visual_search_request

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
