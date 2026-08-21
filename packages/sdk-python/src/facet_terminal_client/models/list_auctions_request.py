from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.auction_status import AuctionStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListAuctionsRequest")



@_attrs_define
class ListAuctionsRequest:
    """ 
        Attributes:
            site_id (str | Unset):
            status (AuctionStatus | Unset):
            ends_within_hours (int | Unset):
            limit (int | Unset):
     """

    site_id: str | Unset = UNSET
    status: AuctionStatus | Unset = UNSET
    ends_within_hours: int | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        ends_within_hours = self.ends_within_hours

        limit = self.limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if site_id is not UNSET:
            field_dict["site_id"] = site_id
        if status is not UNSET:
            field_dict["status"] = status
        if ends_within_hours is not UNSET:
            field_dict["ends_within_hours"] = ends_within_hours
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AuctionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AuctionStatus(_status)




        ends_within_hours = d.pop("ends_within_hours", UNSET)

        limit = d.pop("limit", UNSET)

        list_auctions_request = cls(
            site_id=site_id,
            status=status,
            ends_within_hours=ends_within_hours,
            limit=limit,
        )


        list_auctions_request.additional_properties = d
        return list_auctions_request

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
