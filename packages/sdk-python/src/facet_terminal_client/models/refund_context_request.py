from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RefundContextRequest")



@_attrs_define
class RefundContextRequest:
    """ Internal (OMS relay): everything a merchant's storefront plugin needs to settle a refund it is about to create
    itself, BEFORE any Facet ticket exists. A native WooCommerce refund originates in wp-admin, so there is no refund_id
    to preview at the moment the merchant's wallet must sign or broadcast. Authenticated by the per-site OMS signature
    (X-Facet-OMS-*), not a KYA bearer or session; scoped to the signed site.

        Attributes:
            facet_order_id (str): The Facet order id (UUID) the merchant is about to refund.
     """

    facet_order_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        facet_order_id = self.facet_order_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "facet_order_id": facet_order_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        facet_order_id = d.pop("facet_order_id")

        refund_context_request = cls(
            facet_order_id=facet_order_id,
        )


        refund_context_request.additional_properties = d
        return refund_context_request

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
