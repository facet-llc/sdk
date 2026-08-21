from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TermsResponsePricing")



@_attrs_define
class TermsResponsePricing:
    """ 
        Attributes:
            query_usdc (float):
            transactional_usdc (float):
            settlement_rails (list[str]):
     """

    query_usdc: float
    transactional_usdc: float
    settlement_rails: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        query_usdc = self.query_usdc

        transactional_usdc = self.transactional_usdc

        settlement_rails = self.settlement_rails




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "query_usdc": query_usdc,
            "transactional_usdc": transactional_usdc,
            "settlement_rails": settlement_rails,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_usdc = d.pop("query_usdc")

        transactional_usdc = d.pop("transactional_usdc")

        settlement_rails = cast(list[str], d.pop("settlement_rails"))


        terms_response_pricing = cls(
            query_usdc=query_usdc,
            transactional_usdc=transactional_usdc,
            settlement_rails=settlement_rails,
        )


        terms_response_pricing.additional_properties = d
        return terms_response_pricing

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
