from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.match_hit_properties import MatchHitProperties





T = TypeVar("T", bound="MatchHit")



@_attrs_define
class MatchHit:
    """ 
        Attributes:
            id (str):
            ubi_id (None | str):
            label (str):
            node_type (str): KgNodeType OR a free-form string when the DB outpaces the union.
            similarity (float):
            properties (MatchHitProperties):
     """

    id: str
    ubi_id: None | str
    label: str
    node_type: str
    similarity: float
    properties: MatchHitProperties
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.match_hit_properties import MatchHitProperties
        id = self.id

        ubi_id: None | str
        ubi_id = self.ubi_id

        label = self.label

        node_type = self.node_type

        similarity = self.similarity

        properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "ubi_id": ubi_id,
            "label": label,
            "node_type": node_type,
            "similarity": similarity,
            "properties": properties,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_hit_properties import MatchHitProperties
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_ubi_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ubi_id = _parse_ubi_id(d.pop("ubi_id"))


        label = d.pop("label")

        node_type = d.pop("node_type")

        similarity = d.pop("similarity")

        properties = MatchHitProperties.from_dict(d.pop("properties"))




        match_hit = cls(
            id=id,
            ubi_id=ubi_id,
            label=label,
            node_type=node_type,
            similarity=similarity,
            properties=properties,
        )


        match_hit.additional_properties = d
        return match_hit

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
