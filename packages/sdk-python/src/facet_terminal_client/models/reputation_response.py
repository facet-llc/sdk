from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reputation_tier import ReputationTier
from typing import cast

if TYPE_CHECKING:
  from ..models.reputation_response_counters import ReputationResponseCounters





T = TypeVar("T", bound="ReputationResponse")



@_attrs_define
class ReputationResponse:
    """ 
        Attributes:
            aid (str):
            counters (ReputationResponseCounters):
            total_sites (int):
            score (float):
            tier (ReputationTier):
            first_seen_at (None | str):
            last_seen_at (None | str):
     """

    aid: str
    counters: ReputationResponseCounters
    total_sites: int
    score: float
    tier: ReputationTier
    first_seen_at: None | str
    last_seen_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reputation_response_counters import ReputationResponseCounters
        aid = self.aid

        counters = self.counters.to_dict()

        total_sites = self.total_sites

        score = self.score

        tier = self.tier.value

        first_seen_at: None | str
        first_seen_at = self.first_seen_at

        last_seen_at: None | str
        last_seen_at = self.last_seen_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "aid": aid,
            "counters": counters,
            "total_sites": total_sites,
            "score": score,
            "tier": tier,
            "first_seen_at": first_seen_at,
            "last_seen_at": last_seen_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reputation_response_counters import ReputationResponseCounters
        d = dict(src_dict)
        aid = d.pop("aid")

        counters = ReputationResponseCounters.from_dict(d.pop("counters"))




        total_sites = d.pop("total_sites")

        score = d.pop("score")

        tier = ReputationTier(d.pop("tier"))




        def _parse_first_seen_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_seen_at = _parse_first_seen_at(d.pop("first_seen_at"))


        def _parse_last_seen_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at"))


        reputation_response = cls(
            aid=aid,
            counters=counters,
            total_sites=total_sites,
            score=score,
            tier=tier,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
        )


        reputation_response.additional_properties = d
        return reputation_response

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
