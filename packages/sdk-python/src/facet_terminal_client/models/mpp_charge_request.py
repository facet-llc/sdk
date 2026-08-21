from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MppChargeRequest")



@_attrs_define
class MppChargeRequest:
    """ Charge an existing reservation over the Machine Payments Protocol. Send it with no `Authorization: Payment`
    credential to receive the 402 challenge, then re-send with the signed credential.

        Attributes:
            reservation_id (str): The Facet reservation to charge. Obtained from POST /v1/reserve or a UCP checkout CREATE.
                The unguessable id is the capability on this route: a caller who does not hold one receives 404, and the
                settlement runs as the reservation's OWN agent, never one asserted by this request.
     """

    reservation_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_id = self.reservation_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reservation_id": reservation_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reservation_id = d.pop("reservation_id")

        mpp_charge_request = cls(
            reservation_id=reservation_id,
        )


        mpp_charge_request.additional_properties = d
        return mpp_charge_request

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
