from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stripe_webhook_ack_mode_mismatch_ignored import StripeWebhookAckModeMismatchIgnored






T = TypeVar("T", bound="StripeWebhookAckModeMismatch")



@_attrs_define
class StripeWebhookAckModeMismatch:
    """ 
        Attributes:
            received (bool):
            ignored (StripeWebhookAckModeMismatchIgnored):
            event_livemode (bool):
            terminal_livemode (bool):
     """

    received: bool
    ignored: StripeWebhookAckModeMismatchIgnored
    event_livemode: bool
    terminal_livemode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        received = self.received

        ignored = self.ignored.value

        event_livemode = self.event_livemode

        terminal_livemode = self.terminal_livemode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "received": received,
            "ignored": ignored,
            "event_livemode": event_livemode,
            "terminal_livemode": terminal_livemode,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        received = d.pop("received")

        ignored = StripeWebhookAckModeMismatchIgnored(d.pop("ignored"))




        event_livemode = d.pop("event_livemode")

        terminal_livemode = d.pop("terminal_livemode")

        stripe_webhook_ack_mode_mismatch = cls(
            received=received,
            ignored=ignored,
            event_livemode=event_livemode,
            terminal_livemode=terminal_livemode,
        )


        stripe_webhook_ack_mode_mismatch.additional_properties = d
        return stripe_webhook_ack_mode_mismatch

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
