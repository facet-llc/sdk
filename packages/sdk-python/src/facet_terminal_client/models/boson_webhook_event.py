from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BosonWebhookEvent")



@_attrs_define
class BosonWebhookEvent:
    """ Boson exchange-state webhook body. The exchange-state schema is owned by Boson; mirrored here for the receiver,
    which verifies the HMAC signature before consuming.

        Attributes:
            exchange_id (str | Unset): Boson exchange id (uint256 decimal string).
            state (str | Unset): Exchange state (COMMITTED|REDEEMED|COMPLETED|REVOKED|DISPUTED…).
            dispute_state (str | Unset):
     """

    exchange_id: str | Unset = UNSET
    state: str | Unset = UNSET
    dispute_state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        state = self.state

        dispute_state = self.dispute_state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exchange_id is not UNSET:
            field_dict["exchangeId"] = exchange_id
        if state is not UNSET:
            field_dict["state"] = state
        if dispute_state is not UNSET:
            field_dict["disputeState"] = dispute_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchangeId", UNSET)

        state = d.pop("state", UNSET)

        dispute_state = d.pop("disputeState", UNSET)

        boson_webhook_event = cls(
            exchange_id=exchange_id,
            state=state,
            dispute_state=dispute_state,
        )


        boson_webhook_event.additional_properties = d
        return boson_webhook_event

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
