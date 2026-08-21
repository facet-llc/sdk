from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FacetRateLimitState")



@_attrs_define
class FacetRateLimitState:
    """ Rate-limit posture mirrored in the X-Facet-RateLimit-* response headers.

        Attributes:
            limit (int):
            remaining (int):
            reset (int): Unix-epoch seconds at which the bucket refills.
     """

    limit: int
    remaining: int
    reset: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        remaining = self.remaining

        reset = self.reset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "limit": limit,
            "remaining": remaining,
            "reset": reset,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        remaining = d.pop("remaining")

        reset = d.pop("reset")

        facet_rate_limit_state = cls(
            limit=limit,
            remaining=remaining,
            reset=reset,
        )


        facet_rate_limit_state.additional_properties = d
        return facet_rate_limit_state

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
