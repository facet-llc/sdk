from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UcpOriginatedCheckoutCompleteRequest")



@_attrs_define
class UcpOriginatedCheckoutCompleteRequest:
    """ An originated UCP checkout complete (POST /ucp/v1/originated-checkouts/complete). Forwards the buyer's client-signed
    payment to the target merchant's complete route under this platform's RFC 9421 ES256 signature plus the forwarded
    buyer KYA. Non-custodial: the platform key is auth and provenance only and never touches funds.

        Attributes:
            target (str): The same target merchant Terminal base URL used for the create leg (absolute https, first-party
                allowed).
            checkout_id (str): The checkout session id returned by the originated create leg.
            payment (Any): The buyer's payment instrument, signed CLIENT-side against the merchant offer from the create
                402. No buyer key ever reaches this server; the platform re-signs only the outbound envelope with its own key
                and forwards the buyer KYA.
     """

    target: str
    checkout_id: str
    payment: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        target = self.target

        checkout_id = self.checkout_id

        payment = self.payment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "target": target,
            "checkout_id": checkout_id,
            "payment": payment,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target = d.pop("target")

        checkout_id = d.pop("checkout_id")

        payment = d.pop("payment")

        ucp_originated_checkout_complete_request = cls(
            target=target,
            checkout_id=checkout_id,
            payment=payment,
        )


        ucp_originated_checkout_complete_request.additional_properties = d
        return ucp_originated_checkout_complete_request

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
