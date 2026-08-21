from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpWithdrawResponse")



@_attrs_define
class UcpWithdrawResponse:
    """ Acknowledges the on-chain gasless withdraw. The buyer's available-funds moved to their own wallet; the buyer paid no
    gas.

        Attributes:
            status (str | Unset): Withdraw status, e.g. "withdrawn".
            exchange_id (str | Unset): The exchange whose site authorised the relay.
            tx (str | Unset): The on-chain withdraw transaction hash.
            entity_id (str | Unset): The entity whose available-funds were withdrawn.
            token (str | Unset): The withdrawn token address.
            amount_atomic (str | Unset): The atomic amount withdrawn.
     """

    status: str | Unset = UNSET
    exchange_id: str | Unset = UNSET
    tx: str | Unset = UNSET
    entity_id: str | Unset = UNSET
    token: str | Unset = UNSET
    amount_atomic: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status

        exchange_id = self.exchange_id

        tx = self.tx

        entity_id = self.entity_id

        token = self.token

        amount_atomic = self.amount_atomic


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if tx is not UNSET:
            field_dict["tx"] = tx
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if token is not UNSET:
            field_dict["token"] = token
        if amount_atomic is not UNSET:
            field_dict["amount_atomic"] = amount_atomic

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        exchange_id = d.pop("exchange_id", UNSET)

        tx = d.pop("tx", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        token = d.pop("token", UNSET)

        amount_atomic = d.pop("amount_atomic", UNSET)

        ucp_withdraw_response = cls(
            status=status,
            exchange_id=exchange_id,
            tx=tx,
            entity_id=entity_id,
            token=token,
            amount_atomic=amount_atomic,
        )


        ucp_withdraw_response.additional_properties = d
        return ucp_withdraw_response

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
