from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.terms_response_buyer_protection import TermsResponseBuyerProtection
  from ..models.terms_response_data_use import TermsResponseDataUse
  from ..models.terms_response_pricing import TermsResponsePricing
  from ..models.terms_response_rate_limits import TermsResponseRateLimits
  from ..models.terms_response_sla import TermsResponseSla
  from ..models.terms_response_support import TermsResponseSupport





T = TypeVar("T", bound="TermsResponse")



@_attrs_define
class TermsResponse:
    """ 
        Attributes:
            facet (str):
            pricing (TermsResponsePricing):
            rate_limits (TermsResponseRateLimits):
            sla (TermsResponseSla):
            data_use (TermsResponseDataUse):
            support (TermsResponseSupport):
            buyer_protection (TermsResponseBuyerProtection | Unset):
     """

    facet: str
    pricing: TermsResponsePricing
    rate_limits: TermsResponseRateLimits
    sla: TermsResponseSla
    data_use: TermsResponseDataUse
    support: TermsResponseSupport
    buyer_protection: TermsResponseBuyerProtection | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.terms_response_buyer_protection import TermsResponseBuyerProtection
        from ..models.terms_response_data_use import TermsResponseDataUse
        from ..models.terms_response_pricing import TermsResponsePricing
        from ..models.terms_response_rate_limits import TermsResponseRateLimits
        from ..models.terms_response_sla import TermsResponseSla
        from ..models.terms_response_support import TermsResponseSupport
        facet = self.facet

        pricing = self.pricing.to_dict()

        rate_limits = self.rate_limits.to_dict()

        sla = self.sla.to_dict()

        data_use = self.data_use.to_dict()

        support = self.support.to_dict()

        buyer_protection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buyer_protection, Unset):
            buyer_protection = self.buyer_protection.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "facet": facet,
            "pricing": pricing,
            "rate_limits": rate_limits,
            "sla": sla,
            "data_use": data_use,
            "support": support,
        })
        if buyer_protection is not UNSET:
            field_dict["buyer_protection"] = buyer_protection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.terms_response_buyer_protection import TermsResponseBuyerProtection
        from ..models.terms_response_data_use import TermsResponseDataUse
        from ..models.terms_response_pricing import TermsResponsePricing
        from ..models.terms_response_rate_limits import TermsResponseRateLimits
        from ..models.terms_response_sla import TermsResponseSla
        from ..models.terms_response_support import TermsResponseSupport
        d = dict(src_dict)
        facet = d.pop("facet")

        pricing = TermsResponsePricing.from_dict(d.pop("pricing"))




        rate_limits = TermsResponseRateLimits.from_dict(d.pop("rate_limits"))




        sla = TermsResponseSla.from_dict(d.pop("sla"))




        data_use = TermsResponseDataUse.from_dict(d.pop("data_use"))




        support = TermsResponseSupport.from_dict(d.pop("support"))




        _buyer_protection = d.pop("buyer_protection", UNSET)
        buyer_protection: TermsResponseBuyerProtection | Unset
        if isinstance(_buyer_protection,  Unset):
            buyer_protection = UNSET
        else:
            buyer_protection = TermsResponseBuyerProtection.from_dict(_buyer_protection)




        terms_response = cls(
            facet=facet,
            pricing=pricing,
            rate_limits=rate_limits,
            sla=sla,
            data_use=data_use,
            support=support,
            buyer_protection=buyer_protection,
        )


        terms_response.additional_properties = d
        return terms_response

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
