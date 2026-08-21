from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.graph_related_response_seed import GraphRelatedResponseSeed
  from ..models.related_edge import RelatedEdge
  from ..models.related_node import RelatedNode





T = TypeVar("T", bound="GraphRelatedResponse")



@_attrs_define
class GraphRelatedResponse:
    """ 
        Attributes:
            seed (GraphRelatedResponseSeed):
            nodes (list[RelatedNode]):
            edges (list[RelatedEdge]):
            node_count (int):
            edge_count (int):
     """

    seed: GraphRelatedResponseSeed
    nodes: list[RelatedNode]
    edges: list[RelatedEdge]
    node_count: int
    edge_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.graph_related_response_seed import GraphRelatedResponseSeed
        from ..models.related_edge import RelatedEdge
        from ..models.related_node import RelatedNode
        seed = self.seed.to_dict()

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)



        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)



        node_count = self.node_count

        edge_count = self.edge_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "seed": seed,
            "nodes": nodes,
            "edges": edges,
            "node_count": node_count,
            "edge_count": edge_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_related_response_seed import GraphRelatedResponseSeed
        from ..models.related_edge import RelatedEdge
        from ..models.related_node import RelatedNode
        d = dict(src_dict)
        seed = GraphRelatedResponseSeed.from_dict(d.pop("seed"))




        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in (_nodes):
            nodes_item = RelatedNode.from_dict(nodes_item_data)



            nodes.append(nodes_item)


        edges = []
        _edges = d.pop("edges")
        for edges_item_data in (_edges):
            edges_item = RelatedEdge.from_dict(edges_item_data)



            edges.append(edges_item)


        node_count = d.pop("node_count")

        edge_count = d.pop("edge_count")

        graph_related_response = cls(
            seed=seed,
            nodes=nodes,
            edges=edges,
            node_count=node_count,
            edge_count=edge_count,
        )


        graph_related_response.additional_properties = d
        return graph_related_response

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
