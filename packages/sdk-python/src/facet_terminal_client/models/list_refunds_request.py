from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.refund_status import RefundStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListRefundsRequest")



@_attrs_define
class ListRefundsRequest:
    """ 
        Attributes:
            status (RefundStatus | Unset):
            limit (int | Unset):
            cursor (str | Unset):
     """

    status: RefundStatus | Unset = UNSET
    limit: int | Unset = UNSET
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        limit = self.limit

        cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: RefundStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RefundStatus(_status)




        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        list_refunds_request = cls(
            status=status,
            limit=limit,
            cursor=cursor,
        )


        list_refunds_request.additional_properties = d
        return list_refunds_request

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
