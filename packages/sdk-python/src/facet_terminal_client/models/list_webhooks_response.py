from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.webhook_subscription import WebhookSubscription





T = TypeVar("T", bound="ListWebhooksResponse")



@_attrs_define
class ListWebhooksResponse:
    """ 
        Attributes:
            webhooks (list[WebhookSubscription]):
     """

    webhooks: list[WebhookSubscription]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_subscription import WebhookSubscription
        webhooks = []
        for webhooks_item_data in self.webhooks:
            webhooks_item = webhooks_item_data.to_dict()
            webhooks.append(webhooks_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "webhooks": webhooks,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_subscription import WebhookSubscription
        d = dict(src_dict)
        webhooks = []
        _webhooks = d.pop("webhooks")
        for webhooks_item_data in (_webhooks):
            webhooks_item = WebhookSubscription.from_dict(webhooks_item_data)



            webhooks.append(webhooks_item)


        list_webhooks_response = cls(
            webhooks=webhooks,
        )


        list_webhooks_response.additional_properties = d
        return list_webhooks_response

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
