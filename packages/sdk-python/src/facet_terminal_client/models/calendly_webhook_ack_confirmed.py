from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.calendly_webhook_ack_confirmed_action import CalendlyWebhookAckConfirmedAction






T = TypeVar("T", bound="CalendlyWebhookAckConfirmed")



@_attrs_define
class CalendlyWebhookAckConfirmed:
    """ 
        Attributes:
            ok (bool):
            action (CalendlyWebhookAckConfirmedAction):
            booking_id (str):
     """

    ok: bool
    action: CalendlyWebhookAckConfirmedAction
    booking_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        action = self.action.value

        booking_id = self.booking_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ok": ok,
            "action": action,
            "booking_id": booking_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        action = CalendlyWebhookAckConfirmedAction(d.pop("action"))




        booking_id = d.pop("booking_id")

        calendly_webhook_ack_confirmed = cls(
            ok=ok,
            action=action,
            booking_id=booking_id,
        )


        calendly_webhook_ack_confirmed.additional_properties = d
        return calendly_webhook_ack_confirmed

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
