from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subscription_tier import SubscriptionTier






T = TypeVar("T", bound="StripeCheckoutSessionResponse")



@_attrs_define
class StripeCheckoutSessionResponse:
    """ 
        Attributes:
            session_id (str):
            url (str):
            tier (SubscriptionTier):
            site_id (str):
     """

    session_id: str
    url: str
    tier: SubscriptionTier
    site_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        url = self.url

        tier = self.tier.value

        site_id = self.site_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "session_id": session_id,
            "url": url,
            "tier": tier,
            "site_id": site_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("session_id")

        url = d.pop("url")

        tier = SubscriptionTier(d.pop("tier"))




        site_id = d.pop("site_id")

        stripe_checkout_session_response = cls(
            session_id=session_id,
            url=url,
            tier=tier,
            site_id=site_id,
        )


        stripe_checkout_session_response.additional_properties = d
        return stripe_checkout_session_response

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
