from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="WooCommerceWebhookAck")



@_attrs_define
class WooCommerceWebhookAck:
    """ 
        Attributes:
            received (bool):
            topic (None | str): The X-WC-Webhook-Topic that was processed (or null).
     """

    received: bool
    topic: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        received = self.received

        topic: None | str
        topic = self.topic


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "received": received,
            "topic": topic,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        received = d.pop("received")

        def _parse_topic(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        topic = _parse_topic(d.pop("topic"))


        woo_commerce_webhook_ack = cls(
            received=received,
            topic=topic,
        )


        woo_commerce_webhook_ack.additional_properties = d
        return woo_commerce_webhook_ack

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
