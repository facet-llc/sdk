from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PaymentsCapabilitiesResponse")



@_attrs_define
class PaymentsCapabilitiesResponse:
    """ 
        Attributes:
            rails (list[str]):
            verifier_kinds (list[str]):
            configured (bool):
     """

    rails: list[str]
    verifier_kinds: list[str]
    configured: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rails = self.rails



        verifier_kinds = self.verifier_kinds



        configured = self.configured


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rails": rails,
            "verifier_kinds": verifier_kinds,
            "configured": configured,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rails = cast(list[str], d.pop("rails"))


        verifier_kinds = cast(list[str], d.pop("verifier_kinds"))


        configured = d.pop("configured")

        payments_capabilities_response = cls(
            rails=rails,
            verifier_kinds=verifier_kinds,
            configured=configured,
        )


        payments_capabilities_response.additional_properties = d
        return payments_capabilities_response

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
