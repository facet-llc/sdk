from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_escrow_seller_revoke_refunded_revoke_status import OpenEscrowSellerRevokeRefundedRevokeStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="OpenEscrowSellerRevokeRefundedRevoke")



@_attrs_define
class OpenEscrowSellerRevokeRefundedRevoke:
    """ 
        Attributes:
            escrow_id (str):
            status (OpenEscrowSellerRevokeRefundedRevokeStatus):
            refund_amount_minor (int): Full refund in USD cents.
            refund_amount_base_units (str): Full refund in USDC base units, decimal string.
            arbiter_address (str):
            open_tx (str | Unset): openDispute tx hash; present only when the relayer broadcast it.
            resolve_tx (str | Unset): resolveDispute tx hash; present only when broadcast.
     """

    escrow_id: str
    status: OpenEscrowSellerRevokeRefundedRevokeStatus
    refund_amount_minor: int
    refund_amount_base_units: str
    arbiter_address: str
    open_tx: str | Unset = UNSET
    resolve_tx: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        escrow_id = self.escrow_id

        status = self.status.value

        refund_amount_minor = self.refund_amount_minor

        refund_amount_base_units = self.refund_amount_base_units

        arbiter_address = self.arbiter_address

        open_tx = self.open_tx

        resolve_tx = self.resolve_tx


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "escrowId": escrow_id,
            "status": status,
            "refundAmountMinor": refund_amount_minor,
            "refundAmountBaseUnits": refund_amount_base_units,
            "arbiterAddress": arbiter_address,
        })
        if open_tx is not UNSET:
            field_dict["openTx"] = open_tx
        if resolve_tx is not UNSET:
            field_dict["resolveTx"] = resolve_tx

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escrow_id = d.pop("escrowId")

        status = OpenEscrowSellerRevokeRefundedRevokeStatus(d.pop("status"))




        refund_amount_minor = d.pop("refundAmountMinor")

        refund_amount_base_units = d.pop("refundAmountBaseUnits")

        arbiter_address = d.pop("arbiterAddress")

        open_tx = d.pop("openTx", UNSET)

        resolve_tx = d.pop("resolveTx", UNSET)

        open_escrow_seller_revoke_refunded_revoke = cls(
            escrow_id=escrow_id,
            status=status,
            refund_amount_minor=refund_amount_minor,
            refund_amount_base_units=refund_amount_base_units,
            arbiter_address=arbiter_address,
            open_tx=open_tx,
            resolve_tx=resolve_tx,
        )


        open_escrow_seller_revoke_refunded_revoke.additional_properties = d
        return open_escrow_seller_revoke_refunded_revoke

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
