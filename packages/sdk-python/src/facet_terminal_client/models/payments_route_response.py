from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PaymentsRouteResponse")



@_attrs_define
class PaymentsRouteResponse:
    """ 
        Attributes:
            rail_id (None | str):
            origination_id (str):
            dispatcher_configured (bool):
     """

    rail_id: None | str
    origination_id: str
    dispatcher_configured: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rail_id: None | str
        rail_id = self.rail_id

        origination_id = self.origination_id

        dispatcher_configured = self.dispatcher_configured


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rail_id": rail_id,
            "origination_id": origination_id,
            "dispatcher_configured": dispatcher_configured,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_rail_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rail_id = _parse_rail_id(d.pop("rail_id"))


        origination_id = d.pop("origination_id")

        dispatcher_configured = d.pop("dispatcher_configured")

        payments_route_response = cls(
            rail_id=rail_id,
            origination_id=origination_id,
            dispatcher_configured=dispatcher_configured,
        )


        payments_route_response.additional_properties = d
        return payments_route_response

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
