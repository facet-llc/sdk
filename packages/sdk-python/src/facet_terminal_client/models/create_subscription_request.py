from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.subscription_line_item import SubscriptionLineItem





T = TypeVar("T", bound="CreateSubscriptionRequest")



@_attrs_define
class CreateSubscriptionRequest:
    """ 
        Attributes:
            site_id (str):
            cadence_iso8601 (str):
            line_items (list[SubscriptionLineItem]):
            settlement_rail (str | Unset):
            currency (str | Unset):
            notes (str | Unset):
     """

    site_id: str
    cadence_iso8601: str
    line_items: list[SubscriptionLineItem]
    settlement_rail: str | Unset = UNSET
    currency: str | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_line_item import SubscriptionLineItem
        site_id = self.site_id

        cadence_iso8601 = self.cadence_iso8601

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)



        settlement_rail = self.settlement_rail

        currency = self.currency

        notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "cadence_iso8601": cadence_iso8601,
            "line_items": line_items,
        })
        if settlement_rail is not UNSET:
            field_dict["settlement_rail"] = settlement_rail
        if currency is not UNSET:
            field_dict["currency"] = currency
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_line_item import SubscriptionLineItem
        d = dict(src_dict)
        site_id = d.pop("site_id")

        cadence_iso8601 = d.pop("cadence_iso8601")

        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in (_line_items):
            line_items_item = SubscriptionLineItem.from_dict(line_items_item_data)



            line_items.append(line_items_item)


        settlement_rail = d.pop("settlement_rail", UNSET)

        currency = d.pop("currency", UNSET)

        notes = d.pop("notes", UNSET)

        create_subscription_request = cls(
            site_id=site_id,
            cadence_iso8601=cadence_iso8601,
            line_items=line_items,
            settlement_rail=settlement_rail,
            currency=currency,
            notes=notes,
        )


        create_subscription_request.additional_properties = d
        return create_subscription_request

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
