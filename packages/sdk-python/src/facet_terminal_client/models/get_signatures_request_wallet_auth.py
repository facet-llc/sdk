from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetSignaturesRequestWalletAuth")



@_attrs_define
class GetSignaturesRequestWalletAuth:
    r""" 
        Attributes:
            wallet (str): The payer wallet, a 0x-prefixed EVM address.
            issued_at (int): Unix seconds when the challenge was signed; must be within the freshness window.
            nonce (str): A caller-generated single-use nonce, consumed server-side to bar replay.
            signature (str): The 0x-prefixed EIP-191 signature over `Facet signatures refetch\norder: <order_id>\nwallet:
                <wallet>\nissued_at: <issued_at>\nnonce: <nonce>`. A DISTINCT challenge from the receipt re-fetch, so a proof
                for one read cannot be replayed onto the other.
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

        get_signatures_request_wallet_auth = cls(
            wallet=wallet,
            issued_at=issued_at,
            nonce=nonce,
            signature=signature,
        )


        get_signatures_request_wallet_auth.additional_properties = d
        return get_signatures_request_wallet_auth

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
