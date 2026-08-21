from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.related_edge_properties import RelatedEdgeProperties





T = TypeVar("T", bound="RelatedEdge")



@_attrs_define
class RelatedEdge:
    """ 
        Attributes:
            id (str):
            src_node_id (str):
            dst_node_id (str):
            relation (str):
            weight (float):
            properties (RelatedEdgeProperties):
     """

    id: str
    src_node_id: str
    dst_node_id: str
    relation: str
    weight: float
    properties: RelatedEdgeProperties
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.related_edge_properties import RelatedEdgeProperties
        id = self.id

        src_node_id = self.src_node_id

        dst_node_id = self.dst_node_id

        relation = self.relation

        weight = self.weight

        properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "src_node_id": src_node_id,
            "dst_node_id": dst_node_id,
            "relation": relation,
            "weight": weight,
            "properties": properties,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.related_edge_properties import RelatedEdgeProperties
        d = dict(src_dict)
        id = d.pop("id")

        src_node_id = d.pop("src_node_id")

        dst_node_id = d.pop("dst_node_id")

        relation = d.pop("relation")

        weight = d.pop("weight")

        properties = RelatedEdgeProperties.from_dict(d.pop("properties"))




        related_edge = cls(
            id=id,
            src_node_id=src_node_id,
            dst_node_id=dst_node_id,
            relation=relation,
            weight=weight,
            properties=properties,
        )


        related_edge.additional_properties = d
        return related_edge

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
