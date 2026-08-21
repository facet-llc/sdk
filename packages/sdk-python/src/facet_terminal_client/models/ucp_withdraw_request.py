from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UcpWithdrawRequest")



@_attrs_define
class UcpWithdrawRequest:
    """ Gaslessly cash out a Boson refund (POST /ucp/v1/checkout-sessions/withdraw): the buyer signs a withdrawFunds meta-tx
    locally and the Terminal's gas-only relayer submits it and pays the gas, moving the buyer's protocol available-funds
    to the buyer's own wallet. Non-custodial.

        Attributes:
            exchange_id (str): A settled Boson exchange on THIS site. It authorises the gasless relay (the site bind,
                server-derived); it is not the source of the funds, which is the buyer's entity.
            from_ (str): The buyer wallet that signed the withdraw meta-tx (0x + 40 hex).
            entity_id (str): The buyer's Boson entity id whose available-funds are withdrawn (decimal).
            token (str): The withdraw token address (the rail USDC, 0x + 40 hex).
            amount_atomic (str): The atomic amount to withdraw (decimal).
            nonce (str): The Boson meta-transaction nonce (decimal).
            signature (str): The buyer's MetaTxFund EIP-712 signature over (entity, token, amount, nonce). Only the entity's
                own signer can produce it, and Boson sends the funds to that entity's own wallet, so the withdraw is self-
                binding on-chain.
     """

    exchange_id: str
    from_: str
    entity_id: str
    token: str
    amount_atomic: str
    nonce: str
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        from_ = self.from_

        entity_id = self.entity_id

        token = self.token

        amount_atomic = self.amount_atomic

        nonce = self.nonce

        signature = self.signature


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "exchange_id": exchange_id,
            "from": from_,
            "entity_id": entity_id,
            "token": token,
            "amount_atomic": amount_atomic,
            "nonce": nonce,
            "signature": signature,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id")

        from_ = d.pop("from")

        entity_id = d.pop("entity_id")

        token = d.pop("token")

        amount_atomic = d.pop("amount_atomic")

        nonce = d.pop("nonce")

        signature = d.pop("signature")

        ucp_withdraw_request = cls(
            exchange_id=exchange_id,
            from_=from_,
            entity_id=entity_id,
            token=token,
            amount_atomic=amount_atomic,
            nonce=nonce,
            signature=signature,
        )


        ucp_withdraw_request.additional_properties = d
        return ucp_withdraw_request

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
