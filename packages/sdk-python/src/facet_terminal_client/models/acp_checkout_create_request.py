from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AcpCheckoutCreateRequest")



@_attrs_define
class AcpCheckoutCreateRequest:
    """ An ACP checkout create request (POST /checkout_sessions). v1 reserves a cart of server-priced DISTINCT line items
    and advertises card-only Stripe Shared Payment Token payment requirements. Every price is resolved from this
    merchant's catalog, never the request body.

        Attributes:
            line_items (Any): The authoritative ACP line items: [{ id, quantity }] (CheckoutSessionCreateRequest.line_items
                per the formal schema). A flat `items` key with the same shape is also accepted as a compatibility fallback. v1
                supports a cart of DISTINCT ids (up to 20 lines); every price is server-derived from the catalog, never trusted
                from the request.
            currency (str): ISO 4217 currency code.
            fulfillment_details (Any | Unset): Optional. { phone_number, address: { name, line_one, line_two, city, state,
                country, postal_code } }. When present, the destination is vaulted and the session is priced LANDED: goods plus
                shipping plus tax. Omit for a goods-only checkout.
     """

    line_items: Any
    currency: str
    fulfillment_details: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        line_items = self.line_items

        currency = self.currency

        fulfillment_details = self.fulfillment_details


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "line_items": line_items,
            "currency": currency,
        })
        if fulfillment_details is not UNSET:
            field_dict["fulfillment_details"] = fulfillment_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_items = d.pop("line_items")

        currency = d.pop("currency")

        fulfillment_details = d.pop("fulfillment_details", UNSET)

        acp_checkout_create_request = cls(
            line_items=line_items,
            currency=currency,
            fulfillment_details=fulfillment_details,
        )


        acp_checkout_create_request.additional_properties = d
        return acp_checkout_create_request

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
