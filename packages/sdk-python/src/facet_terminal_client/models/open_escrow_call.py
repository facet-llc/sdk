from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OpenEscrowCall")



@_attrs_define
class OpenEscrowCall:
    """ 
        Attributes:
            to (str): OpenEscrow contract address to send the transaction to.
            data (str): ABI-encoded calldata (0x hex).
            value (str): Native value; always the literal string "0x0".
            chain_id (int): EVM chain id the caller must broadcast on.
     """

    to: str
    data: str
    value: str
    chain_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        to = self.to

        data = self.data

        value = self.value

        chain_id = self.chain_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "to": to,
            "data": data,
            "value": value,
            "chainId": chain_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to = d.pop("to")

        data = d.pop("data")

        value = d.pop("value")

        chain_id = d.pop("chainId")

        open_escrow_call = cls(
            to=to,
            data=data,
            value=value,
            chain_id=chain_id,
        )


        open_escrow_call.additional_properties = d
        return open_escrow_call

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
