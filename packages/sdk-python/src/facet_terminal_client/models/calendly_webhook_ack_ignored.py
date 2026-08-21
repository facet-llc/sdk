from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.calendly_webhook_ack_ignored_action import CalendlyWebhookAckIgnoredAction






T = TypeVar("T", bound="CalendlyWebhookAckIgnored")



@_attrs_define
class CalendlyWebhookAckIgnored:
    """ 
        Attributes:
            ok (bool):
            event (str):
            action (CalendlyWebhookAckIgnoredAction):
     """

    ok: bool
    event: str
    action: CalendlyWebhookAckIgnoredAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        event = self.event

        action = self.action.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ok": ok,
            "event": event,
            "action": action,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        event = d.pop("event")

        action = CalendlyWebhookAckIgnoredAction(d.pop("action"))




        calendly_webhook_ack_ignored = cls(
            ok=ok,
            event=event,
            action=action,
        )


        calendly_webhook_ack_ignored.additional_properties = d
        return calendly_webhook_ack_ignored

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
