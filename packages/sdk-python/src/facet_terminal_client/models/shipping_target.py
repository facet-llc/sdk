from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ShippingTarget")



@_attrs_define
class ShippingTarget:
    """ 
        Attributes:
            recipient (str):
            line1 (str):
            locality (str):
            region (str): ISO 3166-2.
            postal_code (str):
            country (str): ISO 3166-1 alpha-2.
            line2 (str | Unset):
            phone (str | Unset): Carrier delivery notification only.
     """

    recipient: str
    line1: str
    locality: str
    region: str
    postal_code: str
    country: str
    line2: str | Unset = UNSET
    phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        recipient = self.recipient

        line1 = self.line1

        locality = self.locality

        region = self.region

        postal_code = self.postal_code

        country = self.country

        line2 = self.line2

        phone = self.phone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "recipient": recipient,
            "line1": line1,
            "locality": locality,
            "region": region,
            "postal_code": postal_code,
            "country": country,
        })
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipient = d.pop("recipient")

        line1 = d.pop("line1")

        locality = d.pop("locality")

        region = d.pop("region")

        postal_code = d.pop("postal_code")

        country = d.pop("country")

        line2 = d.pop("line2", UNSET)

        phone = d.pop("phone", UNSET)

        shipping_target = cls(
            recipient=recipient,
            line1=line1,
            locality=locality,
            region=region,
            postal_code=postal_code,
            country=country,
            line2=line2,
            phone=phone,
        )


        shipping_target.additional_properties = d
        return shipping_target

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
