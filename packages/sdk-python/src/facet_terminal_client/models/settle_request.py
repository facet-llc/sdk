from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.settle_request_authority import SettleRequestAuthority





T = TypeVar("T", bound="SettleRequest")



@_attrs_define
class SettleRequest:
    """ 
        Attributes:
            reservation_id (str):
            kya_charge_token (str | Unset):
            rail (str | Unset):
            authority (SettleRequestAuthority | Unset): Optional rail-specific settlement authority artifact, captured via
                the configured payment rail. x402: { x_payment } (base64 X-PAYMENT EIP-3009 USDC authorization). Boson escrow: {
                exchange_id, signed_payload } (the buyer's redeem meta-tx). The charge AMOUNT is never read from here — it is
                derived server-side from the reservation. Absent → dev placeholder charge id.
     """

    reservation_id: str
    kya_charge_token: str | Unset = UNSET
    rail: str | Unset = UNSET
    authority: SettleRequestAuthority | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.settle_request_authority import SettleRequestAuthority
        reservation_id = self.reservation_id

        kya_charge_token = self.kya_charge_token

        rail = self.rail

        authority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authority, Unset):
            authority = self.authority.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reservation_id": reservation_id,
        })
        if kya_charge_token is not UNSET:
            field_dict["kya_charge_token"] = kya_charge_token
        if rail is not UNSET:
            field_dict["rail"] = rail
        if authority is not UNSET:
            field_dict["authority"] = authority

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settle_request_authority import SettleRequestAuthority
        d = dict(src_dict)
        reservation_id = d.pop("reservation_id")

        kya_charge_token = d.pop("kya_charge_token", UNSET)

        rail = d.pop("rail", UNSET)

        _authority = d.pop("authority", UNSET)
        authority: SettleRequestAuthority | Unset
        if isinstance(_authority,  Unset):
            authority = UNSET
        else:
            authority = SettleRequestAuthority.from_dict(_authority)




        settle_request = cls(
            reservation_id=reservation_id,
            kya_charge_token=kya_charge_token,
            rail=rail,
            authority=authority,
        )


        settle_request.additional_properties = d
        return settle_request

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
