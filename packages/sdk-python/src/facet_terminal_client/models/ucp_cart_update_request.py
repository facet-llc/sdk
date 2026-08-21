from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UcpCartUpdateRequest")



@_attrs_define
class UcpCartUpdateRequest:
    """ A UCP cart update request (POST /ucp/v1/carts/:id). Full replacement of the cart's line items, re-priced server-
    side. Keeps the same cart id.

        Attributes:
            line_items (Any): The FULL replacement set of UCP line items: [{ item: { id }, quantity }]. Replaces the cart's
                lines wholesale and re-prices; DISTINCT product_ids, up to 20 lines, every price server-derived from the
                catalog.
     """

    line_items: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        line_items = self.line_items


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "line_items": line_items,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_items = d.pop("line_items")

        ucp_cart_update_request = cls(
            line_items=line_items,
        )


        ucp_cart_update_request.additional_properties = d
        return ucp_cart_update_request

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
