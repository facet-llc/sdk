from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AcpCheckoutUpdateRequest")



@_attrs_define
class AcpCheckoutUpdateRequest:
    """ An ACP checkout update request (POST /checkout_sessions/{id}). v1 does not support item or address changes after
    CREATE (Facet's reservation seals its fulfillment reference and priced totals at create, the same constraint UCP
    already lives with); the response is the unchanged session with an explanatory message when a change was attempted.

        Attributes:
            line_items (Any | Unset): Same shape as AcpCheckoutCreateRequest.line_items.
            fulfillment_details (Any | Unset): Same shape as AcpCheckoutCreateRequest.fulfillment_details.
     """

    line_items: Any | Unset = UNSET
    fulfillment_details: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        line_items = self.line_items

        fulfillment_details = self.fulfillment_details


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if fulfillment_details is not UNSET:
            field_dict["fulfillment_details"] = fulfillment_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_items = d.pop("line_items", UNSET)

        fulfillment_details = d.pop("fulfillment_details", UNSET)

        acp_checkout_update_request = cls(
            line_items=line_items,
            fulfillment_details=fulfillment_details,
        )


        acp_checkout_update_request.additional_properties = d
        return acp_checkout_update_request

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
