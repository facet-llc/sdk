from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OrderLineItem")



@_attrs_define
class OrderLineItem:
    """ 
        Attributes:
            product_id (str):
            qty (int):
            unit_price (float):
            subtotal (float):
     """

    product_id: str
    qty: int
    unit_price: float
    subtotal: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        qty = self.qty

        unit_price = self.unit_price

        subtotal = self.subtotal


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
            "qty": qty,
            "unit_price": unit_price,
            "subtotal": subtotal,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        qty = d.pop("qty")

        unit_price = d.pop("unit_price")

        subtotal = d.pop("subtotal")

        order_line_item = cls(
            product_id=product_id,
            qty=qty,
            unit_price=unit_price,
            subtotal=subtotal,
        )


        order_line_item.additional_properties = d
        return order_line_item

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
