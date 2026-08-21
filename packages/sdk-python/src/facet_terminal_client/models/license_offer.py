from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="LicenseOffer")



@_attrs_define
class LicenseOffer:
    """ Per-scope license offer. additionalProperties is intentional — the resolver MAY add forward-compat fields ahead of
    the protocol; treat unknown fields as informational.

        Attributes:
            site_id (str):
            scope (str):
            price_minor (int):
            currency (str):
            ttl_seconds (int):
            usage_limit (int | None):
            usage_limit_kind (None | str):
            rail (str):
     """

    site_id: str
    scope: str
    price_minor: int
    currency: str
    ttl_seconds: int
    usage_limit: int | None
    usage_limit_kind: None | str
    rail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        scope = self.scope

        price_minor = self.price_minor

        currency = self.currency

        ttl_seconds = self.ttl_seconds

        usage_limit: int | None
        usage_limit = self.usage_limit

        usage_limit_kind: None | str
        usage_limit_kind = self.usage_limit_kind

        rail = self.rail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "scope": scope,
            "price_minor": price_minor,
            "currency": currency,
            "ttl_seconds": ttl_seconds,
            "usage_limit": usage_limit,
            "usage_limit_kind": usage_limit_kind,
            "rail": rail,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        scope = d.pop("scope")

        price_minor = d.pop("price_minor")

        currency = d.pop("currency")

        ttl_seconds = d.pop("ttl_seconds")

        def _parse_usage_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        usage_limit = _parse_usage_limit(d.pop("usage_limit"))


        def _parse_usage_limit_kind(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        usage_limit_kind = _parse_usage_limit_kind(d.pop("usage_limit_kind"))


        rail = d.pop("rail")

        license_offer = cls(
            site_id=site_id,
            scope=scope,
            price_minor=price_minor,
            currency=currency,
            ttl_seconds=ttl_seconds,
            usage_limit=usage_limit,
            usage_limit_kind=usage_limit_kind,
            rail=rail,
        )


        license_offer.additional_properties = d
        return license_offer

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
