from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_control_list_item import AgentControlListItem





T = TypeVar("T", bound="AgentControlListResponse")



@_attrs_define
class AgentControlListResponse:
    """ Owner-gated: every per-agent control on a site, newest first.

        Attributes:
            site_id (str):
            controls (list[AgentControlListItem]):
     """

    site_id: str
    controls: list[AgentControlListItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_control_list_item import AgentControlListItem
        site_id = self.site_id

        controls = []
        for controls_item_data in self.controls:
            controls_item = controls_item_data.to_dict()
            controls.append(controls_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "controls": controls,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_control_list_item import AgentControlListItem
        d = dict(src_dict)
        site_id = d.pop("site_id")

        controls = []
        _controls = d.pop("controls")
        for controls_item_data in (_controls):
            controls_item = AgentControlListItem.from_dict(controls_item_data)



            controls.append(controls_item)


        agent_control_list_response = cls(
            site_id=site_id,
            controls=controls,
        )


        agent_control_list_response.additional_properties = d
        return agent_control_list_response

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
