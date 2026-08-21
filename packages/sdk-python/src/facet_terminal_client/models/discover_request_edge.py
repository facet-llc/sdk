from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DiscoverRequestEdge")



@_attrs_define
class DiscoverRequestEdge:
    """ One-hop knowledge-graph relationship filter.

        Attributes:
            connected_to (str): A ubi_id; return businesses one kg_edges hop away.
            relation (str | Unset): Optional kg_edges.relation filter for the edge hop.
     """

    connected_to: str
    relation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        connected_to = self.connected_to

        relation = self.relation


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connected_to": connected_to,
        })
        if relation is not UNSET:
            field_dict["relation"] = relation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected_to = d.pop("connected_to")

        relation = d.pop("relation", UNSET)

        discover_request_edge = cls(
            connected_to=connected_to,
            relation=relation,
        )


        discover_request_edge.additional_properties = d
        return discover_request_edge

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
