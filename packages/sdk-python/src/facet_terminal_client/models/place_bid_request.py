from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PlaceBidRequest")



@_attrs_define
class PlaceBidRequest:
    """ 
        Attributes:
            auction_id (str):
            max_bid_minor (int):
     """

    auction_id: str
    max_bid_minor: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        auction_id = self.auction_id

        max_bid_minor = self.max_bid_minor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "auction_id": auction_id,
            "max_bid_minor": max_bid_minor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auction_id = d.pop("auction_id")

        max_bid_minor = d.pop("max_bid_minor")

        place_bid_request = cls(
            auction_id=auction_id,
            max_bid_minor=max_bid_minor,
        )


        place_bid_request.additional_properties = d
        return place_bid_request

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
