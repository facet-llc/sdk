from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DiscoverResultReputation")



@_attrs_define
class DiscoverResultReputation:
    """ 
        Attributes:
            avg_score (float | None):
            total_interactions (int):
     """

    avg_score: float | None
    total_interactions: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        avg_score: float | None
        avg_score = self.avg_score

        total_interactions = self.total_interactions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "avg_score": avg_score,
            "total_interactions": total_interactions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_avg_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        avg_score = _parse_avg_score(d.pop("avg_score"))


        total_interactions = d.pop("total_interactions")

        discover_result_reputation = cls(
            avg_score=avg_score,
            total_interactions=total_interactions,
        )


        discover_result_reputation.additional_properties = d
        return discover_result_reputation

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
