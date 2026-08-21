from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ReputationResponseCounters")



@_attrs_define
class ReputationResponseCounters:
    """ 
        Attributes:
            successes (int):
            rate_limited_count (int):
            error_count (int):
            signed_receipts_count (int):
            chargebacks_count (int):
     """

    successes: int
    rate_limited_count: int
    error_count: int
    signed_receipts_count: int
    chargebacks_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        successes = self.successes

        rate_limited_count = self.rate_limited_count

        error_count = self.error_count

        signed_receipts_count = self.signed_receipts_count

        chargebacks_count = self.chargebacks_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "successes": successes,
            "rate_limited_count": rate_limited_count,
            "error_count": error_count,
            "signed_receipts_count": signed_receipts_count,
            "chargebacks_count": chargebacks_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        successes = d.pop("successes")

        rate_limited_count = d.pop("rate_limited_count")

        error_count = d.pop("error_count")

        signed_receipts_count = d.pop("signed_receipts_count")

        chargebacks_count = d.pop("chargebacks_count")

        reputation_response_counters = cls(
            successes=successes,
            rate_limited_count=rate_limited_count,
            error_count=error_count,
            signed_receipts_count=signed_receipts_count,
            chargebacks_count=chargebacks_count,
        )


        reputation_response_counters.additional_properties = d
        return reputation_response_counters

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
