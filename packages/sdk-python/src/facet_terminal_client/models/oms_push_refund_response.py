from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OmsPushRefundResponse")



@_attrs_define
class OmsPushRefundResponse:
    """ 
        Attributes:
            provider (str): OMS adapter identifier (e.g. 'shopify').
            external_id (str):
            already_pushed (bool):
     """

    provider: str
    external_id: str
    already_pushed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        external_id = self.external_id

        already_pushed = self.already_pushed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "provider": provider,
            "external_id": external_id,
            "already_pushed": already_pushed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        external_id = d.pop("external_id")

        already_pushed = d.pop("already_pushed")

        oms_push_refund_response = cls(
            provider=provider,
            external_id=external_id,
            already_pushed=already_pushed,
        )


        oms_push_refund_response.additional_properties = d
        return oms_push_refund_response

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
