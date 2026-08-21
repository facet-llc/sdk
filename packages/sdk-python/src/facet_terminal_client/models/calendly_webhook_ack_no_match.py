from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.calendly_webhook_ack_no_match_action import CalendlyWebhookAckNoMatchAction






T = TypeVar("T", bound="CalendlyWebhookAckNoMatch")



@_attrs_define
class CalendlyWebhookAckNoMatch:
    """ 
        Attributes:
            ok (bool):
            action (CalendlyWebhookAckNoMatchAction):
            scheduling_link_uri (str):
     """

    ok: bool
    action: CalendlyWebhookAckNoMatchAction
    scheduling_link_uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        action = self.action.value

        scheduling_link_uri = self.scheduling_link_uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ok": ok,
            "action": action,
            "scheduling_link_uri": scheduling_link_uri,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        action = CalendlyWebhookAckNoMatchAction(d.pop("action"))




        scheduling_link_uri = d.pop("scheduling_link_uri")

        calendly_webhook_ack_no_match = cls(
            ok=ok,
            action=action,
            scheduling_link_uri=scheduling_link_uri,
        )


        calendly_webhook_ack_no_match.additional_properties = d
        return calendly_webhook_ack_no_match

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
