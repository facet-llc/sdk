from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PersonaWebhookAck")



@_attrs_define
class PersonaWebhookAck:
    """ 
        Attributes:
            received (bool):
            ignored (str | Unset): Why an authentic event was not acted on (unhandled_event|unmapped_status…).
            site_id (str | Unset): Site resolved from the transaction's reference-id.
            kyb_status (str | Unset): kyb_status written (verified|pending|rejected).
     """

    received: bool
    ignored: str | Unset = UNSET
    site_id: str | Unset = UNSET
    kyb_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        received = self.received

        ignored = self.ignored

        site_id = self.site_id

        kyb_status = self.kyb_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "received": received,
        })
        if ignored is not UNSET:
            field_dict["ignored"] = ignored
        if site_id is not UNSET:
            field_dict["site_id"] = site_id
        if kyb_status is not UNSET:
            field_dict["kyb_status"] = kyb_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        received = d.pop("received")

        ignored = d.pop("ignored", UNSET)

        site_id = d.pop("site_id", UNSET)

        kyb_status = d.pop("kyb_status", UNSET)

        persona_webhook_ack = cls(
            received=received,
            ignored=ignored,
            site_id=site_id,
            kyb_status=kyb_status,
        )


        persona_webhook_ack.additional_properties = d
        return persona_webhook_ack

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
