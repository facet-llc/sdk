from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="WooCommerceWebhookEvent")



@_attrs_define
class WooCommerceWebhookEvent:
    """ Vendor-frozen WooCommerce webhook body (e.g. order.updated / product.updated). Shape is owned by WooCommerce and
    treated as a black box — the Terminal verifies the X-WC-Webhook-Signature (base64 HMAC-SHA256 over the raw body,
    against the PER-SITE webhook secret resolved from X-WC-Webhook-Source) + dispatches on X-WC-Webhook-Topic before
    consuming.

     """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        woo_commerce_webhook_event = cls(
        )


        woo_commerce_webhook_event.additional_properties = d
        return woo_commerce_webhook_event

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
