from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UcpCheckoutSessionCancelRequest")



@_attrs_define
class UcpCheckoutSessionCancelRequest:
    """ A UCP checkout SESSION-cancel request (POST /ucp/v1/checkout-sessions/:id/cancel). The body is empty; the checkout
    id comes from the path. Releases the reservation's inventory hold pre-completion (idempotent). Distinct from POST
    /ucp/v1/checkout-sessions/cancel, which is the post-commit Boson escrow cancel of a committed exchange.

     """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ucp_checkout_session_cancel_request = cls(
        )


        ucp_checkout_session_cancel_request.additional_properties = d
        return ucp_checkout_session_cancel_request

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
