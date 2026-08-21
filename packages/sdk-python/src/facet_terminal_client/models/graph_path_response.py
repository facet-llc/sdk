from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.related_edge import RelatedEdge
  from ..models.related_node import RelatedNode





T = TypeVar("T", bound="GraphPathResponse")



@_attrs_define
class GraphPathResponse:
    """ 
        Attributes:
            found (bool):
            hops (int):
            path (list[RelatedNode]):
            edges (list[RelatedEdge]):
     """

    found: bool
    hops: int
    path: list[RelatedNode]
    edges: list[RelatedEdge]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.related_edge import RelatedEdge
        from ..models.related_node import RelatedNode
        found = self.found

        hops = self.hops

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)



        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "found": found,
            "hops": hops,
            "path": path,
            "edges": edges,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.related_edge import RelatedEdge
        from ..models.related_node import RelatedNode
        d = dict(src_dict)
        found = d.pop("found")

        hops = d.pop("hops")

        path = []
        _path = d.pop("path")
        for path_item_data in (_path):
            path_item = RelatedNode.from_dict(path_item_data)



            path.append(path_item)


        edges = []
        _edges = d.pop("edges")
        for edges_item_data in (_edges):
            edges_item = RelatedEdge.from_dict(edges_item_data)



            edges.append(edges_item)


        graph_path_response = cls(
            found=found,
            hops=hops,
            path=path,
            edges=edges,
        )


        graph_path_response.additional_properties = d
        return graph_path_response

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
