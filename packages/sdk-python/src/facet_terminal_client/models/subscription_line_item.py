from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubscriptionLineItem")



@_attrs_define
class SubscriptionLineItem:
    """ 
        Attributes:
            product_id (str):
            qty (int):
            max_unit_price_minor (int | Unset):
            currency (str | Unset):
     """

    product_id: str
    qty: int
    max_unit_price_minor: int | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        qty = self.qty

        max_unit_price_minor = self.max_unit_price_minor

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
            "qty": qty,
        })
        if max_unit_price_minor is not UNSET:
            field_dict["max_unit_price_minor"] = max_unit_price_minor
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        qty = d.pop("qty")

        max_unit_price_minor = d.pop("max_unit_price_minor", UNSET)

        currency = d.pop("currency", UNSET)

        subscription_line_item = cls(
            product_id=product_id,
            qty=qty,
            max_unit_price_minor=max_unit_price_minor,
            currency=currency,
        )


        subscription_line_item.additional_properties = d
        return subscription_line_item

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
