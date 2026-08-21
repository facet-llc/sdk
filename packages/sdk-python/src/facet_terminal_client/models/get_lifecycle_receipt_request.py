from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_lifecycle_receipt_request_kind import GetLifecycleReceiptRequestKind
from ..types import UNSET, Unset






T = TypeVar("T", bound="GetLifecycleReceiptRequest")



@_attrs_define
class GetLifecycleReceiptRequest:
    """ Looked up by the caller-held handle plus the kind. Exactly one of `order_id` (refund) or `exchange_id` (cancel /
    withdraw / dispute) is required; supplying neither returns INVALID_REQUEST. Owner-scoped exactly like get_receipt:
    an event owned by a different agent and one that does not exist BOTH read back as the same NOT_FOUND, so a reference
    can never be probed for existence.

        Attributes:
            kind (GetLifecycleReceiptRequestKind): Which agent-initiated reversal to mint a receipt for.
            order_id (str | Unset): The Facet order UUID. The handle for a refund (the reversal that carries an order id).
            exchange_id (str | Unset): The Boson exchange id. The handle for a cancel / withdraw / dispute (which carry no
                Facet order uuid).
     """

    kind: GetLifecycleReceiptRequestKind
    order_id: str | Unset = UNSET
    exchange_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        order_id = self.order_id

        exchange_id = self.exchange_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = GetLifecycleReceiptRequestKind(d.pop("kind"))




        order_id = d.pop("order_id", UNSET)

        exchange_id = d.pop("exchange_id", UNSET)

        get_lifecycle_receipt_request = cls(
            kind=kind,
            order_id=order_id,
            exchange_id=exchange_id,
        )


        get_lifecycle_receipt_request.additional_properties = d
        return get_lifecycle_receipt_request

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
