from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.quote_amount_in_uom import QuoteAmountInUom





T = TypeVar("T", bound="QuoteRequestLineItemsItem")



@_attrs_define
class QuoteRequestLineItemsItem:
    """ 
        Attributes:
            product_id (str):
            qty (int | Unset):
            qty_in_uom (QuoteAmountInUom | Unset):
     """

    product_id: str
    qty: int | Unset = UNSET
    qty_in_uom: QuoteAmountInUom | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.quote_amount_in_uom import QuoteAmountInUom
        product_id = self.product_id

        qty = self.qty

        qty_in_uom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qty_in_uom, Unset):
            qty_in_uom = self.qty_in_uom.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
        })
        if qty is not UNSET:
            field_dict["qty"] = qty
        if qty_in_uom is not UNSET:
            field_dict["qty_in_uom"] = qty_in_uom

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quote_amount_in_uom import QuoteAmountInUom
        d = dict(src_dict)
        product_id = d.pop("product_id")

        qty = d.pop("qty", UNSET)

        _qty_in_uom = d.pop("qty_in_uom", UNSET)
        qty_in_uom: QuoteAmountInUom | Unset
        if isinstance(_qty_in_uom,  Unset):
            qty_in_uom = UNSET
        else:
            qty_in_uom = QuoteAmountInUom.from_dict(_qty_in_uom)




        quote_request_line_items_item = cls(
            product_id=product_id,
            qty=qty,
            qty_in_uom=qty_in_uom,
        )


        quote_request_line_items_item.additional_properties = d
        return quote_request_line_items_item

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
