from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DispatchAgentSummary")



@_attrs_define
class DispatchAgentSummary:
    """ 
        Attributes:
            aid (str):
            issuer (str):
            acting_for (None | str):
     """

    aid: str
    issuer: str
    acting_for: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        aid = self.aid

        issuer = self.issuer

        acting_for: None | str
        acting_for = self.acting_for


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "aid": aid,
            "issuer": issuer,
            "acting_for": acting_for,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aid = d.pop("aid")

        issuer = d.pop("issuer")

        def _parse_acting_for(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acting_for = _parse_acting_for(d.pop("acting_for"))


        dispatch_agent_summary = cls(
            aid=aid,
            issuer=issuer,
            acting_for=acting_for,
        )


        dispatch_agent_summary.additional_properties = d
        return dispatch_agent_summary

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
