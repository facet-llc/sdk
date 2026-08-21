from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_status import ReservationStatus






T = TypeVar("T", bound="Reservation")



@_attrs_define
class Reservation:
    """ 
        Attributes:
            reservation_id (str):
            product_id (str):
            qty (int):
            unit_price (float):
            total (float):
            currency (str):
            status (ReservationStatus):
            created_at (str): ISO 8601.
            expires_at (str): ISO 8601.
     """

    reservation_id: str
    product_id: str
    qty: int
    unit_price: float
    total: float
    currency: str
    status: ReservationStatus
    created_at: str
    expires_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_id = self.reservation_id

        product_id = self.product_id

        qty = self.qty

        unit_price = self.unit_price

        total = self.total

        currency = self.currency

        status = self.status.value

        created_at = self.created_at

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reservation_id": reservation_id,
            "product_id": product_id,
            "qty": qty,
            "unit_price": unit_price,
            "total": total,
            "currency": currency,
            "status": status,
            "created_at": created_at,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reservation_id = d.pop("reservation_id")

        product_id = d.pop("product_id")

        qty = d.pop("qty")

        unit_price = d.pop("unit_price")

        total = d.pop("total")

        currency = d.pop("currency")

        status = ReservationStatus(d.pop("status"))




        created_at = d.pop("created_at")

        expires_at = d.pop("expires_at")

        reservation = cls(
            reservation_id=reservation_id,
            product_id=product_id,
            qty=qty,
            unit_price=unit_price,
            total=total,
            currency=currency,
            status=status,
            created_at=created_at,
            expires_at=expires_at,
        )


        reservation.additional_properties = d
        return reservation

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
