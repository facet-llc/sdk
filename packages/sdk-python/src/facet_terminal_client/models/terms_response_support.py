from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TermsResponseSupport")



@_attrs_define
class TermsResponseSupport:
    """ 
        Attributes:
            contact (str):
            escalate_via (str):
     """

    contact: str
    escalate_via: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        contact = self.contact

        escalate_via = self.escalate_via


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contact": contact,
            "escalate_via": escalate_via,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact = d.pop("contact")

        escalate_via = d.pop("escalate_via")

        terms_response_support = cls(
            contact=contact,
            escalate_via=escalate_via,
        )


        terms_response_support.additional_properties = d
        return terms_response_support

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
