from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpCartResponse")



@_attrs_define
class UcpCartResponse:
    """ A UCP cart resource. Unlike a checkout session it carries NO payment_handlers and NO status: a cart moves no money
    and holds no inventory. Promote it to a checkout by sending its id as `cart_id` to POST /ucp/v1/checkout-sessions.

        Attributes:
            id (str | Unset): The cart id (server-assigned, stable across updates).
            currency (str | Unset): ISO 4217 currency of the priced line items.
            line_items (Any | Unset): The cart line items: [{ item: { id }, quantity }].
            totals (Any | Unset): The UCP totals breakdown: exactly one subtotal and one total (ESTIMATED, in the currency's
                minor unit), plus a detail line per priced component. A pre-checkout cart is goods-only, so it normally carries
                just subtotal + total.
            expires_at (str | Unset): RFC 3339 cart expiry.
     """

    id: str | Unset = UNSET
    currency: str | Unset = UNSET
    line_items: Any | Unset = UNSET
    totals: Any | Unset = UNSET
    expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        currency = self.currency

        line_items = self.line_items

        totals = self.totals

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if totals is not UNSET:
            field_dict["totals"] = totals
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        currency = d.pop("currency", UNSET)

        line_items = d.pop("line_items", UNSET)

        totals = d.pop("totals", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        ucp_cart_response = cls(
            id=id,
            currency=currency,
            line_items=line_items,
            totals=totals,
            expires_at=expires_at,
        )


        ucp_cart_response.additional_properties = d
        return ucp_cart_response

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
