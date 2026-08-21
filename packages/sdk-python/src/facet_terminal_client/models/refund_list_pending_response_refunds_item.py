from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RefundListPendingResponseRefundsItem")



@_attrs_define
class RefundListPendingResponseRefundsItem:
    """ 
        Attributes:
            refund_id (str):
            order_id (str):
            status (str): Ticket status; always 'requested' for this list.
            created_at (str): ISO-8601 timestamp the ticket was opened.
            reason (None | str | Unset): The agent's stated refund reason, if any.
     """

    refund_id: str
    order_id: str
    status: str
    created_at: str
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        refund_id = self.refund_id

        order_id = self.order_id

        status = self.status

        created_at = self.created_at

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refund_id": refund_id,
            "order_id": order_id,
            "status": status,
            "created_at": created_at,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refund_id = d.pop("refund_id")

        order_id = d.pop("order_id")

        status = d.pop("status")

        created_at = d.pop("created_at")

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        refund_list_pending_response_refunds_item = cls(
            refund_id=refund_id,
            order_id=order_id,
            status=status,
            created_at=created_at,
            reason=reason,
        )


        refund_list_pending_response_refunds_item.additional_properties = d
        return refund_list_pending_response_refunds_item

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
