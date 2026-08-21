from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UcpCheckoutUpdateRequest")



@_attrs_define
class UcpCheckoutUpdateRequest:
    """ A UCP checkout update request (POST /ucp/v1/checkout-sessions/:id). The body is effectively ignored: a reservation-
    backed checkout seals its priced totals and fulfillment reference at CREATE, so it cannot be mutated in place. The
    handler returns the CURRENT session unchanged plus a messages[] note; to change line items, update the cart (POST
    /ucp/v1/carts/:id) and start a new checkout with create_checkout(cart_id).

     """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ucp_checkout_update_request = cls(
        )


        ucp_checkout_update_request.additional_properties = d
        return ucp_checkout_update_request

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
