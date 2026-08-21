from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AgentControlDeleteRequest")



@_attrs_define
class AgentControlDeleteRequest:
    """ Owner-gated: clear a per-agent control, reverting the agent to the default allowed state.

        Attributes:
            site_id (str): UUID of the site. Trusted only after requireSiteRole(owner) binds the caller.
            agent_aid (str): The agent identity (KYA aid) whose control to clear.
     """

    site_id: str
    agent_aid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        agent_aid = self.agent_aid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "agent_aid": agent_aid,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        agent_aid = d.pop("agent_aid")

        agent_control_delete_request = cls(
            site_id=site_id,
            agent_aid=agent_aid,
        )


        agent_control_delete_request.additional_properties = d
        return agent_control_delete_request

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
