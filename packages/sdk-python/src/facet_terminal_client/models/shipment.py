from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Shipment")



@_attrs_define
class Shipment:
    """ 
        Attributes:
            carrier (str):
            tracking_number (str):
            eta (str | Unset): ISO 8601.
     """

    carrier: str
    tracking_number: str
    eta: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier

        tracking_number = self.tracking_number

        eta = self.eta


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "carrier": carrier,
            "tracking_number": tracking_number,
        })
        if eta is not UNSET:
            field_dict["eta"] = eta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier = d.pop("carrier")

        tracking_number = d.pop("tracking_number")

        eta = d.pop("eta", UNSET)

        shipment = cls(
            carrier=carrier,
            tracking_number=tracking_number,
            eta=eta,
        )


        shipment.additional_properties = d
        return shipment

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
