from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.public_auction_metadata_jsonb import PublicAuctionMetadataJsonb





T = TypeVar("T", bound="GetAuctionDetail")



@_attrs_define
class GetAuctionDetail:
    """ 
        Attributes:
            id (str):
            site_id (str):
            item_id (str):
            title (str):
            description (None | str):
            starts_at (str):
            ends_at (str):
            reserve_price_minor (int | None):
            starting_price_minor (int):
            bid_increment_minor (int):
            currency (str):
            auction_style (str):
            anti_sniping_extension_sec (int):
            current_price_minor (int):
            current_max_bid_minor (int | None):
            bid_count (int):
            status (str): Catalog: scheduled, live, ended_sold, ended_no_sale.
            winning_order_id (None | str):
            metadata_jsonb (PublicAuctionMetadataJsonb):
            created_at (str):
            ends_in_sec (int):
            has_high_bidder (bool):
            caller_is_high_bidder (bool):
     """

    id: str
    site_id: str
    item_id: str
    title: str
    description: None | str
    starts_at: str
    ends_at: str
    reserve_price_minor: int | None
    starting_price_minor: int
    bid_increment_minor: int
    currency: str
    auction_style: str
    anti_sniping_extension_sec: int
    current_price_minor: int
    current_max_bid_minor: int | None
    bid_count: int
    status: str
    winning_order_id: None | str
    metadata_jsonb: PublicAuctionMetadataJsonb
    created_at: str
    ends_in_sec: int
    has_high_bidder: bool
    caller_is_high_bidder: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_auction_metadata_jsonb import PublicAuctionMetadataJsonb
        id = self.id

        site_id = self.site_id

        item_id = self.item_id

        title = self.title

        description: None | str
        description = self.description

        starts_at = self.starts_at

        ends_at = self.ends_at

        reserve_price_minor: int | None
        reserve_price_minor = self.reserve_price_minor

        starting_price_minor = self.starting_price_minor

        bid_increment_minor = self.bid_increment_minor

        currency = self.currency

        auction_style = self.auction_style

        anti_sniping_extension_sec = self.anti_sniping_extension_sec

        current_price_minor = self.current_price_minor

        current_max_bid_minor: int | None
        current_max_bid_minor = self.current_max_bid_minor

        bid_count = self.bid_count

        status = self.status

        winning_order_id: None | str
        winning_order_id = self.winning_order_id

        metadata_jsonb = self.metadata_jsonb.to_dict()

        created_at = self.created_at

        ends_in_sec = self.ends_in_sec

        has_high_bidder = self.has_high_bidder

        caller_is_high_bidder = self.caller_is_high_bidder


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "site_id": site_id,
            "item_id": item_id,
            "title": title,
            "description": description,
            "starts_at": starts_at,
            "ends_at": ends_at,
            "reserve_price_minor": reserve_price_minor,
            "starting_price_minor": starting_price_minor,
            "bid_increment_minor": bid_increment_minor,
            "currency": currency,
            "auction_style": auction_style,
            "anti_sniping_extension_sec": anti_sniping_extension_sec,
            "current_price_minor": current_price_minor,
            "current_max_bid_minor": current_max_bid_minor,
            "bid_count": bid_count,
            "status": status,
            "winning_order_id": winning_order_id,
            "metadata_jsonb": metadata_jsonb,
            "created_at": created_at,
            "ends_in_sec": ends_in_sec,
            "has_high_bidder": has_high_bidder,
            "caller_is_high_bidder": caller_is_high_bidder,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_auction_metadata_jsonb import PublicAuctionMetadataJsonb
        d = dict(src_dict)
        id = d.pop("id")

        site_id = d.pop("site_id")

        item_id = d.pop("item_id")

        title = d.pop("title")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        def _parse_reserve_price_minor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        reserve_price_minor = _parse_reserve_price_minor(d.pop("reserve_price_minor"))


        starting_price_minor = d.pop("starting_price_minor")

        bid_increment_minor = d.pop("bid_increment_minor")

        currency = d.pop("currency")

        auction_style = d.pop("auction_style")

        anti_sniping_extension_sec = d.pop("anti_sniping_extension_sec")

        current_price_minor = d.pop("current_price_minor")

        def _parse_current_max_bid_minor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        current_max_bid_minor = _parse_current_max_bid_minor(d.pop("current_max_bid_minor"))


        bid_count = d.pop("bid_count")

        status = d.pop("status")

        def _parse_winning_order_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        winning_order_id = _parse_winning_order_id(d.pop("winning_order_id"))


        metadata_jsonb = PublicAuctionMetadataJsonb.from_dict(d.pop("metadata_jsonb"))




        created_at = d.pop("created_at")

        ends_in_sec = d.pop("ends_in_sec")

        has_high_bidder = d.pop("has_high_bidder")

        caller_is_high_bidder = d.pop("caller_is_high_bidder")

        get_auction_detail = cls(
            id=id,
            site_id=site_id,
            item_id=item_id,
            title=title,
            description=description,
            starts_at=starts_at,
            ends_at=ends_at,
            reserve_price_minor=reserve_price_minor,
            starting_price_minor=starting_price_minor,
            bid_increment_minor=bid_increment_minor,
            currency=currency,
            auction_style=auction_style,
            anti_sniping_extension_sec=anti_sniping_extension_sec,
            current_price_minor=current_price_minor,
            current_max_bid_minor=current_max_bid_minor,
            bid_count=bid_count,
            status=status,
            winning_order_id=winning_order_id,
            metadata_jsonb=metadata_jsonb,
            created_at=created_at,
            ends_in_sec=ends_in_sec,
            has_high_bidder=has_high_bidder,
            caller_is_high_bidder=caller_is_high_bidder,
        )


        get_auction_detail.additional_properties = d
        return get_auction_detail

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
