from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.subscription_line_item import SubscriptionLineItem





T = TypeVar("T", bound="ModifySubscriptionLinesRequest")



@_attrs_define
class ModifySubscriptionLinesRequest:
    """ 
        Attributes:
            profile_id (str):
            line_items (list[SubscriptionLineItem]):
     """

    profile_id: str
    line_items: list[SubscriptionLineItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_line_item import SubscriptionLineItem
        profile_id = self.profile_id

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "profile_id": profile_id,
            "line_items": line_items,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_line_item import SubscriptionLineItem
        d = dict(src_dict)
        profile_id = d.pop("profile_id")

        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in (_line_items):
            line_items_item = SubscriptionLineItem.from_dict(line_items_item_data)



            line_items.append(line_items_item)


        modify_subscription_lines_request = cls(
            profile_id=profile_id,
            line_items=line_items,
        )


        modify_subscription_lines_request.additional_properties = d
        return modify_subscription_lines_request

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
