from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.refund import Refund





T = TypeVar("T", bound="ListRefundsResponse")



@_attrs_define
class ListRefundsResponse:
    """ 
        Attributes:
            refunds (list[Refund]):
            next_cursor (None | str):
     """

    refunds: list[Refund]
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refund import Refund
        refunds = []
        for refunds_item_data in self.refunds:
            refunds_item = refunds_item_data.to_dict()
            refunds.append(refunds_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refunds": refunds,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refund import Refund
        d = dict(src_dict)
        refunds = []
        _refunds = d.pop("refunds")
        for refunds_item_data in (_refunds):
            refunds_item = Refund.from_dict(refunds_item_data)



            refunds.append(refunds_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        list_refunds_response = cls(
            refunds=refunds,
            next_cursor=next_cursor,
        )


        list_refunds_response.additional_properties = d
        return list_refunds_response

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
