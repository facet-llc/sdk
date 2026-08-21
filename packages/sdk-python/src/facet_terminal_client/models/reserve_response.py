from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reserve_response_status import ReserveResponseStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReserveResponse")



@_attrs_define
class ReserveResponse:
    """ 
        Attributes:
            reservation_id (str):
            product_id (str):
            qty (int):
            unit_price (float):
            total (float):
            currency (str):
            status (ReserveResponseStatus):
            expires_at (str):
            kya_charge_url (None | str):
            pay_to (str | Unset): Present ONLY on a stripe_deposit settlement-venue site: the per-order Stripe deposit
                address the agent pays the x402 (ERC-3009) to for this reservation, instead of the site's statically advertised
                pay_to. A per-order address cannot be advertised statically, so it rides here. Absent for a normal on-chain site
                (pay_to comes from discovery); optional and additive.
     """

    reservation_id: str
    product_id: str
    qty: int
    unit_price: float
    total: float
    currency: str
    status: ReserveResponseStatus
    expires_at: str
    kya_charge_url: None | str
    pay_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_id = self.reservation_id

        product_id = self.product_id

        qty = self.qty

        unit_price = self.unit_price

        total = self.total

        currency = self.currency

        status = self.status.value

        expires_at = self.expires_at

        kya_charge_url: None | str
        kya_charge_url = self.kya_charge_url

        pay_to = self.pay_to


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
            "expires_at": expires_at,
            "kya_charge_url": kya_charge_url,
        })
        if pay_to is not UNSET:
            field_dict["pay_to"] = pay_to

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

        status = ReserveResponseStatus(d.pop("status"))




        expires_at = d.pop("expires_at")

        def _parse_kya_charge_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        kya_charge_url = _parse_kya_charge_url(d.pop("kya_charge_url"))


        pay_to = d.pop("pay_to", UNSET)

        reserve_response = cls(
            reservation_id=reservation_id,
            product_id=product_id,
            qty=qty,
            unit_price=unit_price,
            total=total,
            currency=currency,
            status=status,
            expires_at=expires_at,
            kya_charge_url=kya_charge_url,
            pay_to=pay_to,
        )


        reserve_response.additional_properties = d
        return reserve_response

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
