from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SettleRequestAuthority")



@_attrs_define
class SettleRequestAuthority:
    """ Optional rail-specific settlement authority artifact, captured via the configured payment rail. x402: { x_payment }
    (base64 X-PAYMENT EIP-3009 USDC authorization). Boson escrow: { exchange_id, signed_payload } (the buyer's redeem
    meta-tx). The charge AMOUNT is never read from here — it is derived server-side from the reservation. Absent → dev
    placeholder charge id.

     """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        settle_request_authority = cls(
        )


        settle_request_authority.additional_properties = d
        return settle_request_authority

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
