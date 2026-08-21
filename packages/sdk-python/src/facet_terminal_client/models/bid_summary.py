from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BidSummary")



@_attrs_define
class BidSummary:
    """ 
        Attributes:
            id (int): Database serial — see B3 caveat on PlaceBidResponse.bid_id.
            amount_minor (int):
            max_bid_minor (int):
            was_winning (bool):
            placed_at (str):
     """

    id: int
    amount_minor: int
    max_bid_minor: int
    was_winning: bool
    placed_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount_minor = self.amount_minor

        max_bid_minor = self.max_bid_minor

        was_winning = self.was_winning

        placed_at = self.placed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "amount_minor": amount_minor,
            "max_bid_minor": max_bid_minor,
            "was_winning": was_winning,
            "placed_at": placed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        amount_minor = d.pop("amount_minor")

        max_bid_minor = d.pop("max_bid_minor")

        was_winning = d.pop("was_winning")

        placed_at = d.pop("placed_at")

        bid_summary = cls(
            id=id,
            amount_minor=amount_minor,
            max_bid_minor=max_bid_minor,
            was_winning=was_winning,
            placed_at=placed_at,
        )


        bid_summary.additional_properties = d
        return bid_summary

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
