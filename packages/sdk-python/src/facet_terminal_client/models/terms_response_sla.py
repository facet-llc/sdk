from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TermsResponseSla")



@_attrs_define
class TermsResponseSla:
    """ 
        Attributes:
            read_p95_ms (int):
            transactional_p95_ms (int):
            uptime_target_monthly (str):
     """

    read_p95_ms: int
    transactional_p95_ms: int
    uptime_target_monthly: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        read_p95_ms = self.read_p95_ms

        transactional_p95_ms = self.transactional_p95_ms

        uptime_target_monthly = self.uptime_target_monthly


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "read_p95_ms": read_p95_ms,
            "transactional_p95_ms": transactional_p95_ms,
            "uptime_target_monthly": uptime_target_monthly,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read_p95_ms = d.pop("read_p95_ms")

        transactional_p95_ms = d.pop("transactional_p95_ms")

        uptime_target_monthly = d.pop("uptime_target_monthly")

        terms_response_sla = cls(
            read_p95_ms=read_p95_ms,
            transactional_p95_ms=transactional_p95_ms,
            uptime_target_monthly=uptime_target_monthly,
        )


        terms_response_sla.additional_properties = d
        return terms_response_sla

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
