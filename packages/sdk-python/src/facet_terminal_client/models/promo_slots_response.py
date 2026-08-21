from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PromoSlotsResponse")



@_attrs_define
class PromoSlotsResponse:
    """ 
        Attributes:
            tier1_claimed (int): Sites claimed under Tier 1 (any platform, free Pro + 0% Facet fee, 12 months).
            tier1_cap (int): Tier 1 cap.
            tier2_claimed (int): Sites claimed under Tier 2 (WooCommerce, 0% Facet fee, 12 months).
            tier2_cap (int): Tier 2 cap.
            live (bool): False when the counts are placeholder zeros (no database configured).
     """

    tier1_claimed: int
    tier1_cap: int
    tier2_claimed: int
    tier2_cap: int
    live: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tier1_claimed = self.tier1_claimed

        tier1_cap = self.tier1_cap

        tier2_claimed = self.tier2_claimed

        tier2_cap = self.tier2_cap

        live = self.live


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tier1_claimed": tier1_claimed,
            "tier1_cap": tier1_cap,
            "tier2_claimed": tier2_claimed,
            "tier2_cap": tier2_cap,
            "live": live,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier1_claimed = d.pop("tier1_claimed")

        tier1_cap = d.pop("tier1_cap")

        tier2_claimed = d.pop("tier2_claimed")

        tier2_cap = d.pop("tier2_cap")

        live = d.pop("live")

        promo_slots_response = cls(
            tier1_claimed=tier1_claimed,
            tier1_cap=tier1_cap,
            tier2_claimed=tier2_claimed,
            tier2_cap=tier2_cap,
            live=live,
        )


        promo_slots_response.additional_properties = d
        return promo_slots_response

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
