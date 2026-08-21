from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rfq_quote_status import RfqQuoteStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.rfq_quote_terms_jsonb import RfqQuoteTermsJsonb





T = TypeVar("T", bound="RfqQuote")



@_attrs_define
class RfqQuote:
    """ 
        Attributes:
            id (str):
            request_id (str):
            site_id (str):
            issued_by_user (str):
            price_minor (int):
            currency (str):
            lead_time_days (int | None):
            terms_jsonb (RfqQuoteTermsJsonb):
            valid_until (str):
            status (RfqQuoteStatus):
            notes (None | str):
            created_at (str):
            updated_at (str):
     """

    id: str
    request_id: str
    site_id: str
    issued_by_user: str
    price_minor: int
    currency: str
    lead_time_days: int | None
    terms_jsonb: RfqQuoteTermsJsonb
    valid_until: str
    status: RfqQuoteStatus
    notes: None | str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rfq_quote_terms_jsonb import RfqQuoteTermsJsonb
        id = self.id

        request_id = self.request_id

        site_id = self.site_id

        issued_by_user = self.issued_by_user

        price_minor = self.price_minor

        currency = self.currency

        lead_time_days: int | None
        lead_time_days = self.lead_time_days

        terms_jsonb = self.terms_jsonb.to_dict()

        valid_until = self.valid_until

        status = self.status.value

        notes: None | str
        notes = self.notes

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "request_id": request_id,
            "site_id": site_id,
            "issued_by_user": issued_by_user,
            "price_minor": price_minor,
            "currency": currency,
            "lead_time_days": lead_time_days,
            "terms_jsonb": terms_jsonb,
            "valid_until": valid_until,
            "status": status,
            "notes": notes,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rfq_quote_terms_jsonb import RfqQuoteTermsJsonb
        d = dict(src_dict)
        id = d.pop("id")

        request_id = d.pop("request_id")

        site_id = d.pop("site_id")

        issued_by_user = d.pop("issued_by_user")

        price_minor = d.pop("price_minor")

        currency = d.pop("currency")

        def _parse_lead_time_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        lead_time_days = _parse_lead_time_days(d.pop("lead_time_days"))


        terms_jsonb = RfqQuoteTermsJsonb.from_dict(d.pop("terms_jsonb"))




        valid_until = d.pop("valid_until")

        status = RfqQuoteStatus(d.pop("status"))




        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))


        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        rfq_quote = cls(
            id=id,
            request_id=request_id,
            site_id=site_id,
            issued_by_user=issued_by_user,
            price_minor=price_minor,
            currency=currency,
            lead_time_days=lead_time_days,
            terms_jsonb=terms_jsonb,
            valid_until=valid_until,
            status=status,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
        )


        rfq_quote.additional_properties = d
        return rfq_quote

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
