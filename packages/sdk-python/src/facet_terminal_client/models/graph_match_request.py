from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GraphMatchRequest")



@_attrs_define
class GraphMatchRequest:
    """ 
        Attributes:
            query_text (str):
            node_types (list[str] | Unset):
            count (int | Unset):
            threshold (float | Unset):
     """

    query_text: str
    node_types: list[str] | Unset = UNSET
    count: int | Unset = UNSET
    threshold: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        query_text = self.query_text

        node_types: list[str] | Unset = UNSET
        if not isinstance(self.node_types, Unset):
            node_types = self.node_types



        count = self.count

        threshold = self.threshold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "query_text": query_text,
        })
        if node_types is not UNSET:
            field_dict["node_types"] = node_types
        if count is not UNSET:
            field_dict["count"] = count
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_text = d.pop("query_text")

        node_types = cast(list[str], d.pop("node_types", UNSET))


        count = d.pop("count", UNSET)

        threshold = d.pop("threshold", UNSET)

        graph_match_request = cls(
            query_text=query_text,
            node_types=node_types,
            count=count,
            threshold=threshold,
        )


        graph_match_request.additional_properties = d
        return graph_match_request

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
