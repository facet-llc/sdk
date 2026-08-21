from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpCheckoutCompleteRequest")



@_attrs_define
class UcpCheckoutCompleteRequest:
    """ A UCP checkout complete request (POST /ucp/v1/checkout-sessions/complete, or the spec-correct /{id}/complete).
    Bridges the buyer's credential to the Terminal dispatcher authority. x402 captures; a boson_commit_authorization
    COMMITS the escrow with the buyer's own x402B signature (funds escrow into the Diamond) and the redeem is deferred
    to the merchant fulfillment webhook. Money movement reuses the non-custodial settle path: the amount is re-derived
    server-side from the reservation and the rail adapter re-verifies the signature, seller, escrow, asset and amount
    before a cent moves.

        Attributes:
            payment (Any): The selected payment payload. The instruments array holds one entry whose credential is either
                type x402_authorization with a token (the buyer signed x402 credential), or type boson_commit_authorization with
                x_payment (the buyer's x402B COMMIT authorization) plus requirements (the seller-signed offer echoed from
                CREATE).
            checkout_id (str | Unset): The checkout session id to complete (the reservation id). OPTIONAL when the spec-
                correct /ucp/v1/checkout-sessions/{id}/complete path form is used (the id is taken from the path); required on
                the legacy body form.
     """

    payment: Any
    checkout_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        payment = self.payment

        checkout_id = self.checkout_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "payment": payment,
        })
        if checkout_id is not UNSET:
            field_dict["checkout_id"] = checkout_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment = d.pop("payment")

        checkout_id = d.pop("checkout_id", UNSET)

        ucp_checkout_complete_request = cls(
            payment=payment,
            checkout_id=checkout_id,
        )


        ucp_checkout_complete_request.additional_properties = d
        return ucp_checkout_complete_request

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
