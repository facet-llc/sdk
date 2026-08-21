from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.refund_list_pending_response_refunds_item import RefundListPendingResponseRefundsItem





T = TypeVar("T", bound="RefundListPendingResponse")



@_attrs_define
class RefundListPendingResponse:
    """ 
        Attributes:
            refunds (list[RefundListPendingResponseRefundsItem]): Pending refund tickets for the order, newest first.
     """

    refunds: list[RefundListPendingResponseRefundsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refund_list_pending_response_refunds_item import RefundListPendingResponseRefundsItem
        refunds = []
        for refunds_item_data in self.refunds:
            refunds_item = refunds_item_data.to_dict()
            refunds.append(refunds_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refunds": refunds,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refund_list_pending_response_refunds_item import RefundListPendingResponseRefundsItem
        d = dict(src_dict)
        refunds = []
        _refunds = d.pop("refunds")
        for refunds_item_data in (_refunds):
            refunds_item = RefundListPendingResponseRefundsItem.from_dict(refunds_item_data)



            refunds.append(refunds_item)


        refund_list_pending_response = cls(
            refunds=refunds,
        )


        refund_list_pending_response.additional_properties = d
        return refund_list_pending_response

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
