from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_control_list_item_mode import AgentControlListItemMode
from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentControlListItem")



@_attrs_define
class AgentControlListItem:
    """ 
        Attributes:
            agent_aid (str):
            mode (AgentControlListItemMode):
            throttle_multiplier (float | Unset): Factor in (0,1] for 'throttled'; null otherwise.
            note (str | Unset): Operator note, or null.
            updated_at (str | Unset): ISO 8601 timestamp of the last change, or null.
     """

    agent_aid: str
    mode: AgentControlListItemMode
    throttle_multiplier: float | Unset = UNSET
    note: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        agent_aid = self.agent_aid

        mode = self.mode.value

        throttle_multiplier = self.throttle_multiplier

        note = self.note

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "agent_aid": agent_aid,
            "mode": mode,
        })
        if throttle_multiplier is not UNSET:
            field_dict["throttle_multiplier"] = throttle_multiplier
        if note is not UNSET:
            field_dict["note"] = note
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_aid = d.pop("agent_aid")

        mode = AgentControlListItemMode(d.pop("mode"))




        throttle_multiplier = d.pop("throttle_multiplier", UNSET)

        note = d.pop("note", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        agent_control_list_item = cls(
            agent_aid=agent_aid,
            mode=mode,
            throttle_multiplier=throttle_multiplier,
            note=note,
            updated_at=updated_at,
        )


        agent_control_list_item.additional_properties = d
        return agent_control_list_item

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
