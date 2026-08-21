from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.calendly_webhook_rate_limited_error import CalendlyWebhookRateLimitedError






T = TypeVar("T", bound="CalendlyWebhookRateLimited")



@_attrs_define
class CalendlyWebhookRateLimited:
    """ Rate-limited response. Uses an `{ error, message }` shape distinct from FacetErrorEnvelope; clients should accept
    both shapes.

        Attributes:
            error (CalendlyWebhookRateLimitedError):
            message (str):
     """

    error: CalendlyWebhookRateLimitedError
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "error": error,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = CalendlyWebhookRateLimitedError(d.pop("error"))




        message = d.pop("message")

        calendly_webhook_rate_limited = cls(
            error=error,
            message=message,
        )


        calendly_webhook_rate_limited.additional_properties = d
        return calendly_webhook_rate_limited

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
