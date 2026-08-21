from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.fulfillment_input_mode import FulfillmentInputMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shipping_target import ShippingTarget





T = TypeVar("T", bound="FulfillmentInput")



@_attrs_define
class FulfillmentInput:
    """ 
        Attributes:
            mode (FulfillmentInputMode):
            address (ShippingTarget | Unset):
            fulfillment_ref (str | Unset):
            ciphertext (str | Unset): Blind-courier: address sealed to the merchant fulfillment key.
            kid (str | Unset): Merchant fulfillment key id (ciphertext mode).
     """

    mode: FulfillmentInputMode
    address: ShippingTarget | Unset = UNSET
    fulfillment_ref: str | Unset = UNSET
    ciphertext: str | Unset = UNSET
    kid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shipping_target import ShippingTarget
        mode = self.mode.value

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        fulfillment_ref = self.fulfillment_ref

        ciphertext = self.ciphertext

        kid = self.kid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mode": mode,
        })
        if address is not UNSET:
            field_dict["address"] = address
        if fulfillment_ref is not UNSET:
            field_dict["fulfillment_ref"] = fulfillment_ref
        if ciphertext is not UNSET:
            field_dict["ciphertext"] = ciphertext
        if kid is not UNSET:
            field_dict["kid"] = kid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shipping_target import ShippingTarget
        d = dict(src_dict)
        mode = FulfillmentInputMode(d.pop("mode"))




        _address = d.pop("address", UNSET)
        address: ShippingTarget | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = ShippingTarget.from_dict(_address)




        fulfillment_ref = d.pop("fulfillment_ref", UNSET)

        ciphertext = d.pop("ciphertext", UNSET)

        kid = d.pop("kid", UNSET)

        fulfillment_input = cls(
            mode=mode,
            address=address,
            fulfillment_ref=fulfillment_ref,
            ciphertext=ciphertext,
            kid=kid,
        )


        fulfillment_input.additional_properties = d
        return fulfillment_input

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
