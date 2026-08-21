from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cancel_reservation_response_status import CancelReservationResponseStatus






T = TypeVar("T", bound="CancelReservationResponse")



@_attrs_define
class CancelReservationResponse:
    """ 
        Attributes:
            reservation_id (str):
            status (CancelReservationResponseStatus):
            cancelled_at (str):
     """

    reservation_id: str
    status: CancelReservationResponseStatus
    cancelled_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_id = self.reservation_id

        status = self.status.value

        cancelled_at = self.cancelled_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reservation_id": reservation_id,
            "status": status,
            "cancelled_at": cancelled_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reservation_id = d.pop("reservation_id")

        status = CancelReservationResponseStatus(d.pop("status"))




        cancelled_at = d.pop("cancelled_at")

        cancel_reservation_response = cls(
            reservation_id=reservation_id,
            status=status,
            cancelled_at=cancelled_at,
        )


        cancel_reservation_response.additional_properties = d
        return cancel_reservation_response

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
