from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_event import WebhookEvent
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateWebhookRequest")



@_attrs_define
class UpdateWebhookRequest:
    """ 
        Attributes:
            webhook_id (str):
            events (list[WebhookEvent] | Unset): Replacement event set. The secret is immutable and cannot be changed here.
            callback_url (str | Unset):
     """

    webhook_id: str
    events: list[WebhookEvent] | Unset = UNSET
    callback_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        webhook_id = self.webhook_id

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)



        callback_url = self.callback_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "webhook_id": webhook_id,
        })
        if events is not UNSET:
            field_dict["events"] = events
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_id = d.pop("webhook_id")

        _events = d.pop("events", UNSET)
        events: list[WebhookEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebhookEvent(events_item_data)



                events.append(events_item)


        callback_url = d.pop("callback_url", UNSET)

        update_webhook_request = cls(
            webhook_id=webhook_id,
            events=events,
            callback_url=callback_url,
        )


        update_webhook_request.additional_properties = d
        return update_webhook_request

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
