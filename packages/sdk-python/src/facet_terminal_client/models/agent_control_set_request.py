from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_control_set_request_mode import AgentControlSetRequestMode
from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentControlSetRequest")



@_attrs_define
class AgentControlSetRequest:
    """ Owner-gated (requireSiteRole owner): set a per-agent block/throttle/allow control on a site, independent of the
    agent's reputation. Moves no funds.

        Attributes:
            site_id (str): UUID of the site to set the control on. Trusted only after requireSiteRole(owner) binds the
                caller to it; a caller can only control agents on a site they own.
            agent_aid (str): The agent identity (KYA aid) to control. Free text, up to 512 chars.
            mode (AgentControlSetRequestMode): blocked = refused at authenticate with 403 FORBIDDEN; throttled = tighten the
                agent's rate-limit multiplier by throttle_multiplier; allowed = explicit no-op override (the default no-control
                state is also allowed).
            throttle_multiplier (float | Unset): Required and meaningful ONLY when mode is 'throttled': a factor in (0,1]
                folded into the agent's rate-limit multiplier. Omitted for other modes.
            note (str | Unset): Optional operator note, up to 500 chars.
     """

    site_id: str
    agent_aid: str
    mode: AgentControlSetRequestMode
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

        mode = AgentControlSetRequestMode(d.pop("mode"))




        throttle_multiplier = d.pop("throttle_multiplier", UNSET)

        note = d.pop("note", UNSET)

        agent_control_set_request = cls(
            site_id=site_id,
            agent_aid=agent_aid,
            mode=mode,
            throttle_multiplier=throttle_multiplier,
            note=note,
        )


        agent_control_set_request.additional_properties = d
        return agent_control_set_request

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
