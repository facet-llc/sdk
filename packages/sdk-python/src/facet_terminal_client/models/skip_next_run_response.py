from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.subscription_profile import SubscriptionProfile





T = TypeVar("T", bound="SkipNextRunResponse")



@_attrs_define
class SkipNextRunResponse:
    """ 
        Attributes:
            profile (SubscriptionProfile):
     """

    profile: SubscriptionProfile
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_profile import SubscriptionProfile
        profile = self.profile.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "profile": profile,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_profile import SubscriptionProfile
        d = dict(src_dict)
        profile = SubscriptionProfile.from_dict(d.pop("profile"))




        skip_next_run_response = cls(
            profile=profile,
        )


        skip_next_run_response.additional_properties = d
        return skip_next_run_response

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
