from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AcpCheckoutCompleteRequest")



@_attrs_define
class AcpCheckoutCompleteRequest:
    """ An ACP checkout complete request (POST /checkout_sessions/{id}/complete). Bridges the buyer's Stripe Shared Payment
    Token to the Terminal dispatcher authority and delegates to settleReservation, which captures straight to the
    merchant's own Stripe account (Connect direct charge). Facet is never a payable party.

        Attributes:
            payment_data (Any): The authoritative nested shape is { instrument: { credential: { type, token } } }, gated by
                handler_id (CheckoutSessionCompleteRequest.payment_data per the formal schema). A flat { type, token } shape is
                also accepted as a compatibility fallback (the formal schema embedded example uses this shape instead, a
                confirmed authoring defect in the vendored spec). token is the Stripe Shared Payment Token (spt_...); Facet
                redeems it via stripe.paymentIntents.create({payment_method_data:{shared_payment_granted_token}, capture_method:
                manual}), the manual-capture leg of the existing two-phase reserve-then-capture Stripe rail.
     """

    payment_data: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        payment_data = self.payment_data


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "payment_data": payment_data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_data = d.pop("payment_data")

        acp_checkout_complete_request = cls(
            payment_data=payment_data,
        )


        acp_checkout_complete_request.additional_properties = d
        return acp_checkout_complete_request

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
