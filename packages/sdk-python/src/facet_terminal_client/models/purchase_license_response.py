from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.purchase_license_response_stripe_status import PurchaseLicenseResponseStripeStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PurchaseLicenseResponse")



@_attrs_define
class PurchaseLicenseResponse:
    """ 
        Attributes:
            license_id (str):
            scope (str):
            price_minor (int):
            currency (str):
            rail (str):
            kya_charge_id (None | str):
            purchased_at (str):
            expires_at (str):
            usage_count (int):
            usage_limit (int | None):
            revoked_at (None | str | Unset):
            stripe_payment_intent_id (None | str | Unset):
            stripe_client_secret (None | str | Unset):
            stripe_application_fee_minor (int | None | Unset):
            stripe_status (PurchaseLicenseResponseStripeStatus | Unset):
     """

    license_id: str
    scope: str
    price_minor: int
    currency: str
    rail: str
    kya_charge_id: None | str
    purchased_at: str
    expires_at: str
    usage_count: int
    usage_limit: int | None
    revoked_at: None | str | Unset = UNSET
    stripe_payment_intent_id: None | str | Unset = UNSET
    stripe_client_secret: None | str | Unset = UNSET
    stripe_application_fee_minor: int | None | Unset = UNSET
    stripe_status: PurchaseLicenseResponseStripeStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        license_id = self.license_id

        scope = self.scope

        price_minor = self.price_minor

        currency = self.currency

        rail = self.rail

        kya_charge_id: None | str
        kya_charge_id = self.kya_charge_id

        purchased_at = self.purchased_at

        expires_at = self.expires_at

        usage_count = self.usage_count

        usage_limit: int | None
        usage_limit = self.usage_limit

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        else:
            revoked_at = self.revoked_at

        stripe_payment_intent_id: None | str | Unset
        if isinstance(self.stripe_payment_intent_id, Unset):
            stripe_payment_intent_id = UNSET
        else:
            stripe_payment_intent_id = self.stripe_payment_intent_id

        stripe_client_secret: None | str | Unset
        if isinstance(self.stripe_client_secret, Unset):
            stripe_client_secret = UNSET
        else:
            stripe_client_secret = self.stripe_client_secret

        stripe_application_fee_minor: int | None | Unset
        if isinstance(self.stripe_application_fee_minor, Unset):
            stripe_application_fee_minor = UNSET
        else:
            stripe_application_fee_minor = self.stripe_application_fee_minor

        stripe_status: str | Unset = UNSET
        if not isinstance(self.stripe_status, Unset):
            stripe_status = self.stripe_status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "license_id": license_id,
            "scope": scope,
            "price_minor": price_minor,
            "currency": currency,
            "rail": rail,
            "kya_charge_id": kya_charge_id,
            "purchased_at": purchased_at,
            "expires_at": expires_at,
            "usage_count": usage_count,
            "usage_limit": usage_limit,
        })
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at
        if stripe_payment_intent_id is not UNSET:
            field_dict["stripe_payment_intent_id"] = stripe_payment_intent_id
        if stripe_client_secret is not UNSET:
            field_dict["stripe_client_secret"] = stripe_client_secret
        if stripe_application_fee_minor is not UNSET:
            field_dict["stripe_application_fee_minor"] = stripe_application_fee_minor
        if stripe_status is not UNSET:
            field_dict["stripe_status"] = stripe_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_id = d.pop("license_id")

        scope = d.pop("scope")

        price_minor = d.pop("price_minor")

        currency = d.pop("currency")

        rail = d.pop("rail")

        def _parse_kya_charge_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        kya_charge_id = _parse_kya_charge_id(d.pop("kya_charge_id"))


        purchased_at = d.pop("purchased_at")

        expires_at = d.pop("expires_at")

        usage_count = d.pop("usage_count")

        def _parse_usage_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        usage_limit = _parse_usage_limit(d.pop("usage_limit"))


        def _parse_revoked_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))


        def _parse_stripe_payment_intent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_payment_intent_id = _parse_stripe_payment_intent_id(d.pop("stripe_payment_intent_id", UNSET))


        def _parse_stripe_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_client_secret = _parse_stripe_client_secret(d.pop("stripe_client_secret", UNSET))


        def _parse_stripe_application_fee_minor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stripe_application_fee_minor = _parse_stripe_application_fee_minor(d.pop("stripe_application_fee_minor", UNSET))


        _stripe_status = d.pop("stripe_status", UNSET)
        stripe_status: PurchaseLicenseResponseStripeStatus | Unset
        if isinstance(_stripe_status,  Unset):
            stripe_status = UNSET
        else:
            stripe_status = PurchaseLicenseResponseStripeStatus(_stripe_status)




        purchase_license_response = cls(
            license_id=license_id,
            scope=scope,
            price_minor=price_minor,
            currency=currency,
            rail=rail,
            kya_charge_id=kya_charge_id,
            purchased_at=purchased_at,
            expires_at=expires_at,
            usage_count=usage_count,
            usage_limit=usage_limit,
            revoked_at=revoked_at,
            stripe_payment_intent_id=stripe_payment_intent_id,
            stripe_client_secret=stripe_client_secret,
            stripe_application_fee_minor=stripe_application_fee_minor,
            stripe_status=stripe_status,
        )


        purchase_license_response.additional_properties = d
        return purchase_license_response

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
