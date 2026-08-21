from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UcpOriginatedCheckoutRedeemRequest")



@_attrs_define
class UcpOriginatedCheckoutRedeemRequest:
    """ An originated UCP deferred-redeem store (POST /ucp/v1/originated-checkouts/redeem). Forwards the buyer's pre-signed
    boson-redeem to the target merchant's redeem store under this platform's RFC 9421 ES256 signature plus the forwarded
    buyer KYA, so a platform-originated checkout can arm release-on-fulfillment. Non-custodial: the platform key is auth
    and provenance only and never touches funds; the merchant stores the redeem and the on-chain release fires later
    from its fulfillment webhook.

        Attributes:
            target (str): The same target merchant Terminal base URL used for the create / complete legs (absolute https,
                first-party allowed).
            exchange_id (str): The committed on-chain Boson exchange id from the complete leg's escrow_state. The buyer's
                redeem voucher self-binds to it.
            signed_payload (str): The buyer's boson-redeem meta-tx, signed CLIENT-side against exchange_id. No buyer key
                reaches this server; the platform re-signs only the outbound envelope and forwards the buyer KYA.
     """

    target: str
    exchange_id: str
    signed_payload: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        target = self.target

        exchange_id = self.exchange_id

        signed_payload = self.signed_payload


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "target": target,
            "exchange_id": exchange_id,
            "signed_payload": signed_payload,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target = d.pop("target")

        exchange_id = d.pop("exchange_id")

        signed_payload = d.pop("signed_payload")

        ucp_originated_checkout_redeem_request = cls(
            target=target,
            exchange_id=exchange_id,
            signed_payload=signed_payload,
        )


        ucp_originated_checkout_redeem_request.additional_properties = d
        return ucp_originated_checkout_redeem_request

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
