from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.order_line_item import OrderLineItem
  from ..models.pricing_tier import PricingTier
  from ..models.quote_response_delivered_in_uom import QuoteResponseDeliveredInUom





T = TypeVar("T", bound="QuoteResponse")



@_attrs_define
class QuoteResponse:
    """ 
        Attributes:
            quote_token (str):
            product_id (str):
            qty (int):
            unit_price (float):
            subtotal (float):
            currency (str):
            expires_at (str): ISO 8601.
            line_items (list[OrderLineItem] | Unset): The priced cart lines (product_id, qty, unit_price, subtotal). One
                element for a single-line quote; N for a multi-line cart. Every price is server-derived.
            applied_tier (PricingTier | Unset):
            delivered_in_uom (QuoteResponseDeliveredInUom | Unset):
            shipping (float | Unset):
            tax (float | Unset):
            duty (float | Unset):
            total_landed (float | Unset):
            delivery_estimate (str | Unset): ISO 8601 date or window.
            fulfillment_ref (str | Unset):
     """

    quote_token: str
    product_id: str
    qty: int
    unit_price: float
    subtotal: float
    currency: str
    expires_at: str
    line_items: list[OrderLineItem] | Unset = UNSET
    applied_tier: PricingTier | Unset = UNSET
    delivered_in_uom: QuoteResponseDeliveredInUom | Unset = UNSET
    shipping: float | Unset = UNSET
    tax: float | Unset = UNSET
    duty: float | Unset = UNSET
    total_landed: float | Unset = UNSET
    delivery_estimate: str | Unset = UNSET
    fulfillment_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_line_item import OrderLineItem
        from ..models.pricing_tier import PricingTier
        from ..models.quote_response_delivered_in_uom import QuoteResponseDeliveredInUom
        quote_token = self.quote_token

        product_id = self.product_id

        qty = self.qty

        unit_price = self.unit_price

        subtotal = self.subtotal

        currency = self.currency

        expires_at = self.expires_at

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)



        applied_tier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applied_tier, Unset):
            applied_tier = self.applied_tier.to_dict()

        delivered_in_uom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delivered_in_uom, Unset):
            delivered_in_uom = self.delivered_in_uom.to_dict()

        shipping = self.shipping

        tax = self.tax

        duty = self.duty

        total_landed = self.total_landed

        delivery_estimate = self.delivery_estimate

        fulfillment_ref = self.fulfillment_ref


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "quote_token": quote_token,
            "product_id": product_id,
            "qty": qty,
            "unit_price": unit_price,
            "subtotal": subtotal,
            "currency": currency,
            "expires_at": expires_at,
        })
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if applied_tier is not UNSET:
            field_dict["applied_tier"] = applied_tier
        if delivered_in_uom is not UNSET:
            field_dict["delivered_in_uom"] = delivered_in_uom
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if tax is not UNSET:
            field_dict["tax"] = tax
        if duty is not UNSET:
            field_dict["duty"] = duty
        if total_landed is not UNSET:
            field_dict["total_landed"] = total_landed
        if delivery_estimate is not UNSET:
            field_dict["delivery_estimate"] = delivery_estimate
        if fulfillment_ref is not UNSET:
            field_dict["fulfillment_ref"] = fulfillment_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_line_item import OrderLineItem
        from ..models.pricing_tier import PricingTier
        from ..models.quote_response_delivered_in_uom import QuoteResponseDeliveredInUom
        d = dict(src_dict)
        quote_token = d.pop("quote_token")

        product_id = d.pop("product_id")

        qty = d.pop("qty")

        unit_price = d.pop("unit_price")

        subtotal = d.pop("subtotal")

        currency = d.pop("currency")

        expires_at = d.pop("expires_at")

        _line_items = d.pop("line_items", UNSET)
        line_items: list[OrderLineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = OrderLineItem.from_dict(line_items_item_data)



                line_items.append(line_items_item)


        _applied_tier = d.pop("applied_tier", UNSET)
        applied_tier: PricingTier | Unset
        if isinstance(_applied_tier,  Unset):
            applied_tier = UNSET
        else:
            applied_tier = PricingTier.from_dict(_applied_tier)




        _delivered_in_uom = d.pop("delivered_in_uom", UNSET)
        delivered_in_uom: QuoteResponseDeliveredInUom | Unset
        if isinstance(_delivered_in_uom,  Unset):
            delivered_in_uom = UNSET
        else:
            delivered_in_uom = QuoteResponseDeliveredInUom.from_dict(_delivered_in_uom)




        shipping = d.pop("shipping", UNSET)

        tax = d.pop("tax", UNSET)

        duty = d.pop("duty", UNSET)

        total_landed = d.pop("total_landed", UNSET)

        delivery_estimate = d.pop("delivery_estimate", UNSET)

        fulfillment_ref = d.pop("fulfillment_ref", UNSET)

        quote_response = cls(
            quote_token=quote_token,
            product_id=product_id,
            qty=qty,
            unit_price=unit_price,
            subtotal=subtotal,
            currency=currency,
            expires_at=expires_at,
            line_items=line_items,
            applied_tier=applied_tier,
            delivered_in_uom=delivered_in_uom,
            shipping=shipping,
            tax=tax,
            duty=duty,
            total_landed=total_landed,
            delivery_estimate=delivery_estimate,
            fulfillment_ref=fulfillment_ref,
        )


        quote_response.additional_properties = d
        return quote_response

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
