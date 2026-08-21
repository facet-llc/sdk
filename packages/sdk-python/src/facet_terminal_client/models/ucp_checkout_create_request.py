from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpCheckoutCreateRequest")



@_attrs_define
class UcpCheckoutCreateRequest:
    """ A UCP checkout create request (POST /ucp/v1/checkout-sessions). v1 reserves a cart of server-priced DISTINCT line
    items and advertises the llc.facet.x402 payment requirements. Every price is resolved from this merchant's catalog,
    never the request body.

        Attributes:
            line_items (Any): The UCP line items: [{ item: { id }, quantity }]. v1 supports a cart of DISTINCT product_ids
                (up to 20 lines); each SKU may appear at most once, and every price is server-derived from the catalog. Ignored
                when `cart_id` is present.
            cart_id (str | Unset): OPTIONAL promote: the id of a UCP cart (POST /ucp/v1/carts) to check out. When present,
                the cart's stored line items drive the checkout and ANY line_items in this body are IGNORED (the two-resource
                model: the business uses the cart contents). The cart must be owned by the caller and still active; the lines
                are re-priced server-side. The checkout id is a NEW id (the reservation id), distinct from the cart id, and the
                cart is marked converted.
            fulfillment (Any | Unset): Optional UCP fulfillment. When it carries a shipping method with a destination
                (methods[].type=shipping, destinations[], selected_destination_id when several), the destination is vaulted and
                the session is priced LANDED: goods plus shipping plus tax. Omit it for a goods-only checkout. This is the ONLY
                point a destination is accepted: complete carries none, so the amount the buyer authorizes always matches what
                ships.
     """

    line_items: Any
    cart_id: str | Unset = UNSET
    fulfillment: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        line_items = self.line_items

        cart_id = self.cart_id

        fulfillment = self.fulfillment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "line_items": line_items,
        })
        if cart_id is not UNSET:
            field_dict["cart_id"] = cart_id
        if fulfillment is not UNSET:
            field_dict["fulfillment"] = fulfillment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_items = d.pop("line_items")

        cart_id = d.pop("cart_id", UNSET)

        fulfillment = d.pop("fulfillment", UNSET)

        ucp_checkout_create_request = cls(
            line_items=line_items,
            cart_id=cart_id,
            fulfillment=fulfillment,
        )


        ucp_checkout_create_request.additional_properties = d
        return ucp_checkout_create_request

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
