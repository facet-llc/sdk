from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UcpOriginatedCheckoutCreateRequest")



@_attrs_define
class UcpOriginatedCheckoutCreateRequest:
    """ An originated UCP checkout create (POST /ucp/v1/originated-checkouts). This platform Terminal forwards the buyer's
    checkout to the `target` merchant Terminal and adds the RFC 9421 ES256 platform signature server-side, so the buyer
    never holds the platform key. The buyer authenticates to this Terminal with its own KYA (Authorization: Bearer),
    which is forwarded to the merchant as the second auth factor. Moves no funds; the merchant response (including its
    402/offer body) relays verbatim.

        Attributes:
            target (str): The target merchant Terminal base URL (absolute https). Must match a configured first-party
                allowed suffix; an originated checkout is first-party only and fails closed otherwise.
            checkout (Any): The buyer's UCP checkout create body, forwarded verbatim to the target merchant's POST
                /ucp/v1/checkout-sessions. Same shape as UcpCheckoutCreateRequest (line_items, optional fulfillment); the
                platform never rewrites it.
     """

    target: str
    checkout: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        target = self.target

        checkout = self.checkout


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "target": target,
            "checkout": checkout,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target = d.pop("target")

        checkout = d.pop("checkout")

        ucp_originated_checkout_create_request = cls(
            target=target,
            checkout=checkout,
        )


        ucp_originated_checkout_create_request.additional_properties = d
        return ucp_originated_checkout_create_request

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
