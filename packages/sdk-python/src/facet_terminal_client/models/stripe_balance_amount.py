from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.stripe_balance_amount_source_types import StripeBalanceAmountSourceTypes





T = TypeVar("T", bound="StripeBalanceAmount")



@_attrs_define
class StripeBalanceAmount:
    """ 
        Attributes:
            amount (int):
            currency (str):
            source_types (StripeBalanceAmountSourceTypes | Unset): Map of source-type → minor-units amount (card / bank /
                fpx / …).
     """

    amount: int
    currency: str
    source_types: StripeBalanceAmountSourceTypes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stripe_balance_amount_source_types import StripeBalanceAmountSourceTypes
        amount = self.amount

        currency = self.currency

        source_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_types, Unset):
            source_types = self.source_types.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amount": amount,
            "currency": currency,
        })
        if source_types is not UNSET:
            field_dict["source_types"] = source_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stripe_balance_amount_source_types import StripeBalanceAmountSourceTypes
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = d.pop("currency")

        _source_types = d.pop("source_types", UNSET)
        source_types: StripeBalanceAmountSourceTypes | Unset
        if isinstance(_source_types,  Unset):
            source_types = UNSET
        else:
            source_types = StripeBalanceAmountSourceTypes.from_dict(_source_types)




        stripe_balance_amount = cls(
            amount=amount,
            currency=currency,
            source_types=source_types,
        )


        stripe_balance_amount.additional_properties = d
        return stripe_balance_amount

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
