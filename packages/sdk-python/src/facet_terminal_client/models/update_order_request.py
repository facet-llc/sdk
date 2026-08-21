from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_status import OrderStatus






T = TypeVar("T", bound="UpdateOrderRequest")



@_attrs_define
class UpdateOrderRequest:
    """ Advance an order's lifecycle status along a legal transition (settled → fulfilled | cancelled; fulfilled and
    cancelled are terminal). `refunded` is NOT reachable here — refunds are driven by refund_request and the adjudicated
    refund pipeline, which leaves the order settled. Re-asserting the current status is an idempotent no-op; an illegal
    or terminal→other transition returns IDEMPOTENCY_CONFLICT. Financial fields are immutable once settled — only status
    changes.

        Attributes:
            order_id (str):
            status (OrderStatus):
     """

    order_id: str
    status: OrderStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id")

        status = OrderStatus(d.pop("status"))




        update_order_request = cls(
            order_id=order_id,
            status=status,
        )


        update_order_request.additional_properties = d
        return update_order_request

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
