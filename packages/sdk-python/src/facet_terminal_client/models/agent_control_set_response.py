from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_control_set_response_mode import AgentControlSetResponseMode
from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentControlSetResponse")



@_attrs_define
class AgentControlSetResponse:
    """ 
        Attributes:
            site_id (str):
            agent_aid (str):
            mode (AgentControlSetResponseMode):
            throttle_multiplier (float | Unset): The stored factor in (0,1] for 'throttled'; null for other modes.
            note (str | Unset): The stored operator note, or null.
     """

    site_id: str
    agent_aid: str
    mode: AgentControlSetResponseMode
    throttle_multiplier: float | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        agent_aid = self.agent_aid

        mode = self.mode.value

        throttle_multiplier = self.throttle_multiplier

        note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "agent_aid": agent_aid,
            "mode": mode,
        })
        if throttle_multiplier is not UNSET:
            field_dict["throttle_multiplier"] = throttle_multiplier
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        agent_aid = d.pop("agent_aid")

        mode = AgentControlSetResponseMode(d.pop("mode"))




        throttle_multiplier = d.pop("throttle_multiplier", UNSET)

        note = d.pop("note", UNSET)

        agent_control_set_response = cls(
            site_id=site_id,
            agent_aid=agent_aid,
            mode=mode,
            throttle_multiplier=throttle_multiplier,
            note=note,
        )


        agent_control_set_response.additional_properties = d
        return agent_control_set_response

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
