from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_event import WebhookEvent
from typing import cast






T = TypeVar("T", bound="GetWebhookResponse")



@_attrs_define
class GetWebhookResponse:
    """ 
        Attributes:
            webhook_id (str):
            events (list[WebhookEvent]):
            callback_url (str):
            active (bool):
            created_at (str):
     """

    webhook_id: str
    events: list[WebhookEvent]
    callback_url: str
    active: bool
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        webhook_id = self.webhook_id

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)



        callback_url = self.callback_url

        active = self.active

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "webhook_id": webhook_id,
            "events": events,
            "callback_url": callback_url,
            "active": active,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_id = d.pop("webhook_id")

        events = []
        _events = d.pop("events")
        for events_item_data in (_events):
            events_item = WebhookEvent(events_item_data)



            events.append(events_item)


        callback_url = d.pop("callback_url")

        active = d.pop("active")

        created_at = d.pop("created_at")

        get_webhook_response = cls(
            webhook_id=webhook_id,
            events=events,
            callback_url=callback_url,
            active=active,
            created_at=created_at,
        )


        get_webhook_response.additional_properties = d
        return get_webhook_response

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
