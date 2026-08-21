from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpCartCreateRequest")



@_attrs_define
class UcpCartCreateRequest:
    """ A UCP cart create request (POST /ucp/v1/carts). Prices a set of DISTINCT line items server-side and stores a pre-
    checkout, MUTABLE cart. Estimated pricing only (goods-only, no ship-to); the cart moves no money and holds no
    inventory.

        Attributes:
            line_items (Any): The UCP line items: [{ item: { id }, quantity }]. A cart of DISTINCT product_ids (up to 20
                lines); each SKU may appear at most once, and every price is server-derived from the catalog.
            buyer (Any | Unset): Optional UCP buyer object, stored and echoed back verbatim on read. Does not price.
            attribution (Any | Unset): Optional UCP attribution object, stored and echoed back verbatim on read. Does not
                price.
            context (Any | Unset): Optional UCP context object, stored and echoed back verbatim on read. Does not price.
     """

    line_items: Any
    buyer: Any | Unset = UNSET
    attribution: Any | Unset = UNSET
    context: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        line_items = self.line_items

        buyer = self.buyer

        attribution = self.attribution

        context = self.context


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "line_items": line_items,
        })
        if buyer is not UNSET:
            field_dict["buyer"] = buyer
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_items = d.pop("line_items")

        buyer = d.pop("buyer", UNSET)

        attribution = d.pop("attribution", UNSET)

        context = d.pop("context", UNSET)

        ucp_cart_create_request = cls(
            line_items=line_items,
            buyer=buyer,
            attribution=attribution,
            context=context,
        )


        ucp_cart_create_request.additional_properties = d
        return ucp_cart_create_request

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
