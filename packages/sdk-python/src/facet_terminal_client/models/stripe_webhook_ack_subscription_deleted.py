from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subscription_tier import SubscriptionTier
from typing import cast






T = TypeVar("T", bound="StripeWebhookAckSubscriptionDeleted")



@_attrs_define
class StripeWebhookAckSubscriptionDeleted:
    """ 
        Attributes:
            received (bool):
            subscription_id (str):
            site_id (None | str):
            tier (SubscriptionTier):
     """

    received: bool
    subscription_id: str
    site_id: None | str
    tier: SubscriptionTier
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        received = self.received

        subscription_id = self.subscription_id

        site_id: None | str
        site_id = self.site_id

        tier = self.tier.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "received": received,
            "subscription_id": subscription_id,
            "site_id": site_id,
            "tier": tier,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        received = d.pop("received")

        subscription_id = d.pop("subscription_id")

        def _parse_site_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        site_id = _parse_site_id(d.pop("site_id"))


        tier = SubscriptionTier(d.pop("tier"))




        stripe_webhook_ack_subscription_deleted = cls(
            received=received,
            subscription_id=subscription_id,
            site_id=site_id,
            tier=tier,
        )


        stripe_webhook_ack_subscription_deleted.additional_properties = d
        return stripe_webhook_ack_subscription_deleted

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
