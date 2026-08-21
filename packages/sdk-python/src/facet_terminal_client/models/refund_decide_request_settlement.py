from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RefundDecideRequestSettlement")



@_attrs_define
class RefundDecideRequestSettlement:
    """ Optional NON-CUSTODIAL x402 refund the merchant settled THEMSELVES. Use when the merchant's wallet does not hand
    Facet the ERC-3009 signature `authority` carries; the merchant instead broadcasts a plain USDC.transfer from their
    own wallet and posts the hash here. Facet neither signs nor relays: it VERIFIES the transaction on-chain (emitted by
    the network's USDC contract, sent from the merchant payTo, received by the buyer, for at least the server-derived
    amount, mined at or after the capture) and only then fulfils the ticket, recording the hash as settlement_ref. One
    transaction settles at most one ticket. Mutually exclusive with `authority`; supplying both is a 400.

        Attributes:
            tx_hash (str): 0x-prefixed 32-byte hash of the USDC transfer the merchant already broadcast from their own
                wallet.
     """

    tx_hash: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tx_hash = self.tx_hash


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tx_hash": tx_hash,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tx_hash = d.pop("tx_hash")

        refund_decide_request_settlement = cls(
            tx_hash=tx_hash,
        )


        refund_decide_request_settlement.additional_properties = d
        return refund_decide_request_settlement

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
