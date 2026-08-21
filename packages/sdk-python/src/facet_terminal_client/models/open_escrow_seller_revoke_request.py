from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OpenEscrowSellerRevokeRequest")



@_attrs_define
class OpenEscrowSellerRevokeRequest:
    """ Internal (site admin): revoke a Funded escrow and fully refund the buyer on-chain in one action. The merchant
    chooses neither amount nor recipient, only which Funded escrow to revoke. Non-custodial: server-derived full refund
    via the arbiter + gas-only relayer.

        Attributes:
            escrow_id (str): 32-byte 0x hex escrow id of the Funded escrow to revoke. site_id is read from the mirror row,
                never the body.
     """

    escrow_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        escrow_id = self.escrow_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "escrowId": escrow_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escrow_id = d.pop("escrowId")

        open_escrow_seller_revoke_request = cls(
            escrow_id=escrow_id,
        )


        open_escrow_seller_revoke_request.additional_properties = d
        return open_escrow_seller_revoke_request

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
