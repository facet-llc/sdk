from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PlaceBidResponse")



@_attrs_define
class PlaceBidResponse:
    """ 
        Attributes:
            bid_id (int): Numeric bid identifier. May move to a string-encoded form in a future revision to avoid JS safe-
                integer issues.
            amount_minor (int):
            was_outbid_immediately (bool):
            is_high_bidder (bool):
     """

    bid_id: int
    amount_minor: int
    was_outbid_immediately: bool
    is_high_bidder: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bid_id = self.bid_id

        amount_minor = self.amount_minor

        was_outbid_immediately = self.was_outbid_immediately

        is_high_bidder = self.is_high_bidder


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "bid_id": bid_id,
            "amount_minor": amount_minor,
            "was_outbid_immediately": was_outbid_immediately,
            "is_high_bidder": is_high_bidder,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bid_id = d.pop("bid_id")

        amount_minor = d.pop("amount_minor")

        was_outbid_immediately = d.pop("was_outbid_immediately")

        is_high_bidder = d.pop("is_high_bidder")

        place_bid_response = cls(
            bid_id=bid_id,
            amount_minor=amount_minor,
            was_outbid_immediately=was_outbid_immediately,
            is_high_bidder=is_high_bidder,
        )


        place_bid_response.additional_properties = d
        return place_bid_response

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
