from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.terms_response_rate_limits_default import TermsResponseRateLimitsDefault





T = TypeVar("T", bound="TermsResponseRateLimits")



@_attrs_define
class TermsResponseRateLimits:
    """ 
        Attributes:
            default (TermsResponseRateLimitsDefault):
            burst_policy (str):
     """

    default: TermsResponseRateLimitsDefault
    burst_policy: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.terms_response_rate_limits_default import TermsResponseRateLimitsDefault
        default = self.default.to_dict()

        burst_policy = self.burst_policy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "default": default,
            "burst_policy": burst_policy,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.terms_response_rate_limits_default import TermsResponseRateLimitsDefault
        d = dict(src_dict)
        default = TermsResponseRateLimitsDefault.from_dict(d.pop("default"))




        burst_policy = d.pop("burst_policy")

        terms_response_rate_limits = cls(
            default=default,
            burst_policy=burst_policy,
        )


        terms_response_rate_limits.additional_properties = d
        return terms_response_rate_limits

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
