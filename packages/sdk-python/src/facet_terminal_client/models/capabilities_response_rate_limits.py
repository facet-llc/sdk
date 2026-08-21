from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.capabilities_response_rate_limits_default import CapabilitiesResponseRateLimitsDefault





T = TypeVar("T", bound="CapabilitiesResponseRateLimits")



@_attrs_define
class CapabilitiesResponseRateLimits:
    """ 
        Attributes:
            default (CapabilitiesResponseRateLimitsDefault):
     """

    default: CapabilitiesResponseRateLimitsDefault
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.capabilities_response_rate_limits_default import CapabilitiesResponseRateLimitsDefault
        default = self.default.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "default": default,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capabilities_response_rate_limits_default import CapabilitiesResponseRateLimitsDefault
        d = dict(src_dict)
        default = CapabilitiesResponseRateLimitsDefault.from_dict(d.pop("default"))




        capabilities_response_rate_limits = cls(
            default=default,
        )


        capabilities_response_rate_limits.additional_properties = d
        return capabilities_response_rate_limits

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
