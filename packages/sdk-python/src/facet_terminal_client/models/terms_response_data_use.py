from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TermsResponseDataUse")



@_attrs_define
class TermsResponseDataUse:
    """ 
        Attributes:
            retention_hot_days (int):
            retention_warm_days (int):
            retention_cold_days (int):
            agent_visible_fields (list[str]):
     """

    retention_hot_days: int
    retention_warm_days: int
    retention_cold_days: int
    agent_visible_fields: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        retention_hot_days = self.retention_hot_days

        retention_warm_days = self.retention_warm_days

        retention_cold_days = self.retention_cold_days

        agent_visible_fields = self.agent_visible_fields




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "retention_hot_days": retention_hot_days,
            "retention_warm_days": retention_warm_days,
            "retention_cold_days": retention_cold_days,
            "agent_visible_fields": agent_visible_fields,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retention_hot_days = d.pop("retention_hot_days")

        retention_warm_days = d.pop("retention_warm_days")

        retention_cold_days = d.pop("retention_cold_days")

        agent_visible_fields = cast(list[str], d.pop("agent_visible_fields"))


        terms_response_data_use = cls(
            retention_hot_days=retention_hot_days,
            retention_warm_days=retention_warm_days,
            retention_cold_days=retention_cold_days,
            agent_visible_fields=agent_visible_fields,
        )


        terms_response_data_use.additional_properties = d
        return terms_response_data_use

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
