from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mpp_charge_response_status import MppChargeResponseStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mpp_charge_response_order import MppChargeResponseOrder





T = TypeVar("T", bound="MppChargeResponse")



@_attrs_define
class MppChargeResponse:
    """ A settled MPP charge. The response also carries the protocol receipt on the `Payment-Receipt` header as unpadded
    base64url JSON.

        Attributes:
            status (MppChargeResponseStatus):
            order (MppChargeResponseOrder): The settled Facet order.
            settlement_id (str): Rail-native settlement reference. For evm/charge on Base, the on-chain tx hash.
            settled_at (str | Unset): RFC 3339 settlement timestamp.
     """

    status: MppChargeResponseStatus
    order: MppChargeResponseOrder
    settlement_id: str
    settled_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mpp_charge_response_order import MppChargeResponseOrder
        status = self.status.value

        order = self.order.to_dict()

        settlement_id = self.settlement_id

        settled_at = self.settled_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "order": order,
            "settlement_id": settlement_id,
        })
        if settled_at is not UNSET:
            field_dict["settled_at"] = settled_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mpp_charge_response_order import MppChargeResponseOrder
        d = dict(src_dict)
        status = MppChargeResponseStatus(d.pop("status"))




        order = MppChargeResponseOrder.from_dict(d.pop("order"))




        settlement_id = d.pop("settlement_id")

        settled_at = d.pop("settled_at", UNSET)

        mpp_charge_response = cls(
            status=status,
            order=order,
            settlement_id=settlement_id,
            settled_at=settled_at,
        )


        mpp_charge_response.additional_properties = d
        return mpp_charge_response

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
