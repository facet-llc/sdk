from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpCheckoutCompleteResponse")



@_attrs_define
class UcpCheckoutCompleteResponse:
    """ A UCP checkout completion mapped from a settled Terminal order. settlement_id is the on-chain capture id; the funds
    moved straight to the merchant's pay_to (non-custodial).

        Attributes:
            status (str | Unset): Completion status, e.g. "completed".
            order (Any | Unset): The settled order: { id, permalink_url }.
            settlement_id (str | Unset): The rail-native settlement id (x402 on-chain tx hash).
            settled_at (str | Unset): ISO 8601 settlement timestamp, when available.
     """

    status: str | Unset = UNSET
    order: Any | Unset = UNSET
    settlement_id: str | Unset = UNSET
    settled_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status

        order = self.order

        settlement_id = self.settlement_id

        settled_at = self.settled_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if order is not UNSET:
            field_dict["order"] = order
        if settlement_id is not UNSET:
            field_dict["settlement_id"] = settlement_id
        if settled_at is not UNSET:
            field_dict["settled_at"] = settled_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        order = d.pop("order", UNSET)

        settlement_id = d.pop("settlement_id", UNSET)

        settled_at = d.pop("settled_at", UNSET)

        ucp_checkout_complete_response = cls(
            status=status,
            order=order,
            settlement_id=settlement_id,
            settled_at=settled_at,
        )


        ucp_checkout_complete_response.additional_properties = d
        return ucp_checkout_complete_response

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
