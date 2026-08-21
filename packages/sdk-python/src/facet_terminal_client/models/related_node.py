from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.related_node_properties import RelatedNodeProperties





T = TypeVar("T", bound="RelatedNode")



@_attrs_define
class RelatedNode:
    """ 
        Attributes:
            id (str):
            ubi_id (None | str):
            label (str):
            node_type (str):
            properties (RelatedNodeProperties):
     """

    id: str
    ubi_id: None | str
    label: str
    node_type: str
    properties: RelatedNodeProperties
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.related_node_properties import RelatedNodeProperties
        id = self.id

        ubi_id: None | str
        ubi_id = self.ubi_id

        label = self.label

        node_type = self.node_type

        properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "ubi_id": ubi_id,
            "label": label,
            "node_type": node_type,
            "properties": properties,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.related_node_properties import RelatedNodeProperties
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_ubi_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ubi_id = _parse_ubi_id(d.pop("ubi_id"))


        label = d.pop("label")

        node_type = d.pop("node_type")

        properties = RelatedNodeProperties.from_dict(d.pop("properties"))




        related_node = cls(
            id=id,
            ubi_id=ubi_id,
            label=label,
            node_type=node_type,
            properties=properties,
        )


        related_node.additional_properties = d
        return related_node

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
