from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DiscoverProductResult")



@_attrs_define
class DiscoverProductResult:
    """ 
        Attributes:
            product_id (str): Agent-facing product id, unique within its merchant.
            name (str):
            category (str):
            price (float): Per-case price in the product's currency.
            currency (str):
            in_stock (bool): Whether the product has inventory available.
            merchant_name (str): The selling merchant's display name.
            terminal_url (None | str): The selling merchant's Terminal URL: point catalog + checkout calls here. Live ->
                https://<domain|terminal.facet.llc>/v1; pre-live -> https://<handle>.sandbox.facet.llc/v1.
     """

    product_id: str
    name: str
    category: str
    price: float
    currency: str
    in_stock: bool
    merchant_name: str
    terminal_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        name = self.name

        category = self.category

        price = self.price

        currency = self.currency

        in_stock = self.in_stock

        merchant_name = self.merchant_name

        terminal_url: None | str
        terminal_url = self.terminal_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "currency": currency,
            "in_stock": in_stock,
            "merchant_name": merchant_name,
            "terminal_url": terminal_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        name = d.pop("name")

        category = d.pop("category")

        price = d.pop("price")

        currency = d.pop("currency")

        in_stock = d.pop("in_stock")

        merchant_name = d.pop("merchant_name")

        def _parse_terminal_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        terminal_url = _parse_terminal_url(d.pop("terminal_url"))


        discover_product_result = cls(
            product_id=product_id,
            name=name,
            category=category,
            price=price,
            currency=currency,
            in_stock=in_stock,
            merchant_name=merchant_name,
            terminal_url=terminal_url,
        )


        discover_product_result.additional_properties = d
        return discover_product_result

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
