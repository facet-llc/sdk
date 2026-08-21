from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_escrow_seller_revoke_already_refunded_revoke_status import OpenEscrowSellerRevokeAlreadyRefundedRevokeStatus






T = TypeVar("T", bound="OpenEscrowSellerRevokeAlreadyRefundedRevoke")



@_attrs_define
class OpenEscrowSellerRevokeAlreadyRefundedRevoke:
    """ 
        Attributes:
            escrow_id (str):
            status (OpenEscrowSellerRevokeAlreadyRefundedRevokeStatus):
     """

    escrow_id: str
    status: OpenEscrowSellerRevokeAlreadyRefundedRevokeStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        escrow_id = self.escrow_id

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "escrowId": escrow_id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escrow_id = d.pop("escrowId")

        status = OpenEscrowSellerRevokeAlreadyRefundedRevokeStatus(d.pop("status"))




        open_escrow_seller_revoke_already_refunded_revoke = cls(
            escrow_id=escrow_id,
            status=status,
        )


        open_escrow_seller_revoke_already_refunded_revoke.additional_properties = d
        return open_escrow_seller_revoke_already_refunded_revoke

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
