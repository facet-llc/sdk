from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pricing_tier import PricingTier





T = TypeVar("T", bound="PricingSchedule")



@_attrs_define
class PricingSchedule:
    """ 
        Attributes:
            currency (str):
            per_case (float):
            tiers (list[PricingTier] | Unset):
     """

    currency: str
    per_case: float
    tiers: list[PricingTier] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pricing_tier import PricingTier
        currency = self.currency

        per_case = self.per_case

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "currency": currency,
            "per_case": per_case,
        })
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_tier import PricingTier
        d = dict(src_dict)
        currency = d.pop("currency")

        per_case = d.pop("per_case")

        _tiers = d.pop("tiers", UNSET)
        tiers: list[PricingTier] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = PricingTier.from_dict(tiers_item_data)



                tiers.append(tiers_item)


        pricing_schedule = cls(
            currency=currency,
            per_case=per_case,
            tiers=tiers,
        )


        pricing_schedule.additional_properties = d
        return pricing_schedule

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
