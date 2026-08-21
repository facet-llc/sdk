from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_event import WebhookEvent
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.capabilities_response_commerce import CapabilitiesResponseCommerce
  from ..models.capabilities_response_fulfillment import CapabilitiesResponseFulfillment
  from ..models.capabilities_response_rate_limits import CapabilitiesResponseRateLimits
  from ..models.capability_disabled_entry import CapabilityDisabledEntry





T = TypeVar("T", bound="CapabilitiesResponse")



@_attrs_define
class CapabilitiesResponse:
    """ 
        Attributes:
            facet (str):
            tools (list[str]):
            commerce (CapabilitiesResponseCommerce):
            webhooks (bool):
            content_licensing (bool):
            response_signing (bool):
            rate_limits (CapabilitiesResponseRateLimits):
            disabled_tools (list[CapabilityDisabledEntry] | Unset):
            webhook_events (list[WebhookEvent] | Unset):
            fulfillment (CapabilitiesResponseFulfillment | Unset):
     """

    facet: str
    tools: list[str]
    commerce: CapabilitiesResponseCommerce
    webhooks: bool
    content_licensing: bool
    response_signing: bool
    rate_limits: CapabilitiesResponseRateLimits
    disabled_tools: list[CapabilityDisabledEntry] | Unset = UNSET
    webhook_events: list[WebhookEvent] | Unset = UNSET
    fulfillment: CapabilitiesResponseFulfillment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.capabilities_response_commerce import CapabilitiesResponseCommerce
        from ..models.capabilities_response_fulfillment import CapabilitiesResponseFulfillment
        from ..models.capabilities_response_rate_limits import CapabilitiesResponseRateLimits
        from ..models.capability_disabled_entry import CapabilityDisabledEntry
        facet = self.facet

        tools = self.tools



        commerce = self.commerce.to_dict()

        webhooks = self.webhooks

        content_licensing = self.content_licensing

        response_signing = self.response_signing

        rate_limits = self.rate_limits.to_dict()

        disabled_tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disabled_tools, Unset):
            disabled_tools = []
            for disabled_tools_item_data in self.disabled_tools:
                disabled_tools_item = disabled_tools_item_data.to_dict()
                disabled_tools.append(disabled_tools_item)



        webhook_events: list[str] | Unset = UNSET
        if not isinstance(self.webhook_events, Unset):
            webhook_events = []
            for webhook_events_item_data in self.webhook_events:
                webhook_events_item = webhook_events_item_data.value
                webhook_events.append(webhook_events_item)



        fulfillment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fulfillment, Unset):
            fulfillment = self.fulfillment.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "facet": facet,
            "tools": tools,
            "commerce": commerce,
            "webhooks": webhooks,
            "content_licensing": content_licensing,
            "response_signing": response_signing,
            "rate_limits": rate_limits,
        })
        if disabled_tools is not UNSET:
            field_dict["disabled_tools"] = disabled_tools
        if webhook_events is not UNSET:
            field_dict["webhook_events"] = webhook_events
        if fulfillment is not UNSET:
            field_dict["fulfillment"] = fulfillment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capabilities_response_commerce import CapabilitiesResponseCommerce
        from ..models.capabilities_response_fulfillment import CapabilitiesResponseFulfillment
        from ..models.capabilities_response_rate_limits import CapabilitiesResponseRateLimits
        from ..models.capability_disabled_entry import CapabilityDisabledEntry
        d = dict(src_dict)
        facet = d.pop("facet")

        tools = cast(list[str], d.pop("tools"))


        commerce = CapabilitiesResponseCommerce.from_dict(d.pop("commerce"))




        webhooks = d.pop("webhooks")

        content_licensing = d.pop("content_licensing")

        response_signing = d.pop("response_signing")

        rate_limits = CapabilitiesResponseRateLimits.from_dict(d.pop("rate_limits"))




        _disabled_tools = d.pop("disabled_tools", UNSET)
        disabled_tools: list[CapabilityDisabledEntry] | Unset = UNSET
        if _disabled_tools is not UNSET:
            disabled_tools = []
            for disabled_tools_item_data in _disabled_tools:
                disabled_tools_item = CapabilityDisabledEntry.from_dict(disabled_tools_item_data)



                disabled_tools.append(disabled_tools_item)


        _webhook_events = d.pop("webhook_events", UNSET)
        webhook_events: list[WebhookEvent] | Unset = UNSET
        if _webhook_events is not UNSET:
            webhook_events = []
            for webhook_events_item_data in _webhook_events:
                webhook_events_item = WebhookEvent(webhook_events_item_data)



                webhook_events.append(webhook_events_item)


        _fulfillment = d.pop("fulfillment", UNSET)
        fulfillment: CapabilitiesResponseFulfillment | Unset
        if isinstance(_fulfillment,  Unset):
            fulfillment = UNSET
        else:
            fulfillment = CapabilitiesResponseFulfillment.from_dict(_fulfillment)




        capabilities_response = cls(
            facet=facet,
            tools=tools,
            commerce=commerce,
            webhooks=webhooks,
            content_licensing=content_licensing,
            response_signing=response_signing,
            rate_limits=rate_limits,
            disabled_tools=disabled_tools,
            webhook_events=webhook_events,
            fulfillment=fulfillment,
        )


        capabilities_response.additional_properties = d
        return capabilities_response

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
