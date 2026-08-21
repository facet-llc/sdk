from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.license_offer import LicenseOffer





T = TypeVar("T", bound="QuoteLicenseResponse")



@_attrs_define
class QuoteLicenseResponse:
    """ 
        Attributes:
            offer (LicenseOffer): Per-scope license offer. additionalProperties is intentional — the resolver MAY add
                forward-compat fields ahead of the protocol; treat unknown fields as informational.
     """

    offer: LicenseOffer
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.license_offer import LicenseOffer
        offer = self.offer.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "offer": offer,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_offer import LicenseOffer
        d = dict(src_dict)
        offer = LicenseOffer.from_dict(d.pop("offer"))




        quote_license_response = cls(
            offer=offer,
        )


        quote_license_response.additional_properties = d
        return quote_license_response

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
