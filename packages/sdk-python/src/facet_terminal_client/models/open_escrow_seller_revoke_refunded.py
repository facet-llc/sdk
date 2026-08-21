from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_escrow_seller_revoke_refunded_status import OpenEscrowSellerRevokeRefundedStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.open_escrow_seller_revoke_refunded_revoke import OpenEscrowSellerRevokeRefundedRevoke





T = TypeVar("T", bound="OpenEscrowSellerRevokeRefunded")



@_attrs_define
class OpenEscrowSellerRevokeRefunded:
    """ 
        Attributes:
            field_status (OpenEscrowSellerRevokeRefundedStatus):
            revoke (OpenEscrowSellerRevokeRefundedRevoke):
     """

    field_status: OpenEscrowSellerRevokeRefundedStatus
    revoke: OpenEscrowSellerRevokeRefundedRevoke
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_escrow_seller_revoke_refunded_revoke import OpenEscrowSellerRevokeRefundedRevoke
        field_status = self.field_status.value

        revoke = self.revoke.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "_status": field_status,
            "revoke": revoke,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_escrow_seller_revoke_refunded_revoke import OpenEscrowSellerRevokeRefundedRevoke
        d = dict(src_dict)
        field_status = OpenEscrowSellerRevokeRefundedStatus(d.pop("_status"))




        revoke = OpenEscrowSellerRevokeRefundedRevoke.from_dict(d.pop("revoke"))




        open_escrow_seller_revoke_refunded = cls(
            field_status=field_status,
            revoke=revoke,
        )


        open_escrow_seller_revoke_refunded.additional_properties = d
        return open_escrow_seller_revoke_refunded

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
