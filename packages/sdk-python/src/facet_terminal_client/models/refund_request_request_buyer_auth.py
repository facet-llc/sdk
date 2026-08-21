from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RefundRequestRequestBuyerAuth")



@_attrs_define
class RefundRequestRequestBuyerAuth:
    """ Optional buyer wallet attestation that authorizes this refund request WITHOUT a platform co-signature, on stores
    that enable autonomous dual-key. The buyer signs an EIP-191 challenge binding the order and wallet; the Terminal
    recovers it and requires it to equal the wallet-bound KYA's payer_wallet, single-use and fresh. It is the refund-
    request analogue of the buyer-signed meta-tx on cancel / dispute, and is ignored when a platform signature is
    present. Opens the ticket only; no funds move until the merchant approves.

        Attributes:
            wallet (str): The paying wallet (0x, checksummed) that signs the attestation.
            issued_at (int): Unix-epoch seconds; the attestation is fresh within a 5-minute window.
            nonce (str): Single-use nonce; a replayed nonce is refused.
            signature (str): 0x EIP-191 personal_sign over the refund-request challenge.
     """

    wallet: str
    issued_at: int
    nonce: str
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        wallet = self.wallet

        issued_at = self.issued_at

        nonce = self.nonce

        signature = self.signature


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "wallet": wallet,
            "issued_at": issued_at,
            "nonce": nonce,
            "signature": signature,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wallet = d.pop("wallet")

        issued_at = d.pop("issued_at")

        nonce = d.pop("nonce")

        signature = d.pop("signature")

        refund_request_request_buyer_auth = cls(
            wallet=wallet,
            issued_at=issued_at,
            nonce=nonce,
            signature=signature,
        )


        refund_request_request_buyer_auth.additional_properties = d
        return refund_request_request_buyer_auth

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
