from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.terms_response_buyer_protection_tier import TermsResponseBuyerProtectionTier






T = TypeVar("T", bound="TermsResponseBuyerProtection")



@_attrs_define
class TermsResponseBuyerProtection:
    """ 
        Attributes:
            tier (TermsResponseBuyerProtectionTier):
            bond_address (str):
            network (str):
            coverage_available (str):
     """

    tier: TermsResponseBuyerProtectionTier
    bond_address: str
    network: str
    coverage_available: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tier = self.tier.value

        bond_address = self.bond_address

        network = self.network

        coverage_available = self.coverage_available


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tier": tier,
            "bond_address": bond_address,
            "network": network,
            "coverage_available": coverage_available,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier = TermsResponseBuyerProtectionTier(d.pop("tier"))




        bond_address = d.pop("bond_address")

        network = d.pop("network")

        coverage_available = d.pop("coverage_available")

        terms_response_buyer_protection = cls(
            tier=tier,
            bond_address=bond_address,
            network=network,
            coverage_available=coverage_available,
        )


        terms_response_buyer_protection.additional_properties = d
        return terms_response_buyer_protection

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
