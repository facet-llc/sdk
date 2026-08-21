from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RefundDecideRequestAuthority")



@_attrs_define
class RefundDecideRequestAuthority:
    """ Optional NON-CUSTODIAL x402 refund on approve. The merchant signs the ERC-3009 reversal out of its OWN payTo and
    Facet only relays it (holds no key). Omitted falls back to a Facet-managed refund signer whose address equals payTo.
    The rail adapter binds the send-back's sender to the merchant payTo, its recipient to the buyer, and its value to
    the server-derived refund amount, and the facilitator re-verifies the signature before a cent moves.

        Attributes:
            x_payment (str): Base64 X-PAYMENT header carrying the merchant-signed ERC-3009 send-back
                (transferWithAuthorization out of the merchant payTo).
     """

    x_payment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        x_payment = self.x_payment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "x_payment": x_payment,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x_payment = d.pop("x_payment")

        refund_decide_request_authority = cls(
            x_payment=x_payment,
        )


        refund_decide_request_authority.additional_properties = d
        return refund_decide_request_authority

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
