from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.fulfillment_input import FulfillmentInput
  from ..models.quote_amount_in_uom import QuoteAmountInUom
  from ..models.quote_request_line_items_item import QuoteRequestLineItemsItem





T = TypeVar("T", bound="QuoteRequest")



@_attrs_define
class QuoteRequest:
    """ 
        Attributes:
            product_id (str):
            qty (int | Unset):
            qty_in_uom (QuoteAmountInUom | Unset):
            line_items (list[QuoteRequestLineItemsItem] | Unset): Optional multi-line cart of DISTINCT product_ids (max 20).
                When present, the quote prices EVERY line server-side and returns one summed subtotal, one shipping, and tax on
                the summed goods; the scalar product_id names the first line for back-compat. Each entry carries its own qty OR
                qty_in_uom.
            exclude_allergens (list[str] | Unset):
            fulfillment (FulfillmentInput | Unset):
     """

    product_id: str
    qty: int | Unset = UNSET
    qty_in_uom: QuoteAmountInUom | Unset = UNSET
    line_items: list[QuoteRequestLineItemsItem] | Unset = UNSET
    exclude_allergens: list[str] | Unset = UNSET
    fulfillment: FulfillmentInput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.fulfillment_input import FulfillmentInput
        from ..models.quote_amount_in_uom import QuoteAmountInUom
        from ..models.quote_request_line_items_item import QuoteRequestLineItemsItem
        product_id = self.product_id

        qty = self.qty

        qty_in_uom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qty_in_uom, Unset):
            qty_in_uom = self.qty_in_uom.to_dict()

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)



        exclude_allergens: list[str] | Unset = UNSET
        if not isinstance(self.exclude_allergens, Unset):
            exclude_allergens = self.exclude_allergens



        fulfillment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fulfillment, Unset):
            fulfillment = self.fulfillment.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
        })
        if qty is not UNSET:
            field_dict["qty"] = qty
        if qty_in_uom is not UNSET:
            field_dict["qty_in_uom"] = qty_in_uom
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if exclude_allergens is not UNSET:
            field_dict["exclude_allergens"] = exclude_allergens
        if fulfillment is not UNSET:
            field_dict["fulfillment"] = fulfillment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fulfillment_input import FulfillmentInput
        from ..models.quote_amount_in_uom import QuoteAmountInUom
        from ..models.quote_request_line_items_item import QuoteRequestLineItemsItem
        d = dict(src_dict)
        product_id = d.pop("product_id")

        qty = d.pop("qty", UNSET)

        _qty_in_uom = d.pop("qty_in_uom", UNSET)
        qty_in_uom: QuoteAmountInUom | Unset
        if isinstance(_qty_in_uom,  Unset):
            qty_in_uom = UNSET
        else:
            qty_in_uom = QuoteAmountInUom.from_dict(_qty_in_uom)




        _line_items = d.pop("line_items", UNSET)
        line_items: list[QuoteRequestLineItemsItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = QuoteRequestLineItemsItem.from_dict(line_items_item_data)



                line_items.append(line_items_item)


        exclude_allergens = cast(list[str], d.pop("exclude_allergens", UNSET))


        _fulfillment = d.pop("fulfillment", UNSET)
        fulfillment: FulfillmentInput | Unset
        if isinstance(_fulfillment,  Unset):
            fulfillment = UNSET
        else:
            fulfillment = FulfillmentInput.from_dict(_fulfillment)




        quote_request = cls(
            product_id=product_id,
            qty=qty,
            qty_in_uom=qty_in_uom,
            line_items=line_items,
            exclude_allergens=exclude_allergens,
            fulfillment=fulfillment,
        )


        quote_request.additional_properties = d
        return quote_request

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
