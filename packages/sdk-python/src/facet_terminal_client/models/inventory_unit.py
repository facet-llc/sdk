from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.inventory_unit_attributes_jsonb import InventoryUnitAttributesJsonb





T = TypeVar("T", bound="InventoryUnit")



@_attrs_define
class InventoryUnit:
    """ 
        Attributes:
            id (str):
            resource_id (str):
            sku (str):
            name (str):
            description (None | str):
            available_from (None | str):
            available_until (None | str):
            quantity (int):
            unit_price_minor (int):
            currency (str):
            attributes_jsonb (InventoryUnitAttributesJsonb):
     """

    id: str
    resource_id: str
    sku: str
    name: str
    description: None | str
    available_from: None | str
    available_until: None | str
    quantity: int
    unit_price_minor: int
    currency: str
    attributes_jsonb: InventoryUnitAttributesJsonb
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inventory_unit_attributes_jsonb import InventoryUnitAttributesJsonb
        id = self.id

        resource_id = self.resource_id

        sku = self.sku

        name = self.name

        description: None | str
        description = self.description

        available_from: None | str
        available_from = self.available_from

        available_until: None | str
        available_until = self.available_until

        quantity = self.quantity

        unit_price_minor = self.unit_price_minor

        currency = self.currency

        attributes_jsonb = self.attributes_jsonb.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "resource_id": resource_id,
            "sku": sku,
            "name": name,
            "description": description,
            "available_from": available_from,
            "available_until": available_until,
            "quantity": quantity,
            "unit_price_minor": unit_price_minor,
            "currency": currency,
            "attributes_jsonb": attributes_jsonb,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_unit_attributes_jsonb import InventoryUnitAttributesJsonb
        d = dict(src_dict)
        id = d.pop("id")

        resource_id = d.pop("resource_id")

        sku = d.pop("sku")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        def _parse_available_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        available_from = _parse_available_from(d.pop("available_from"))


        def _parse_available_until(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        available_until = _parse_available_until(d.pop("available_until"))


        quantity = d.pop("quantity")

        unit_price_minor = d.pop("unit_price_minor")

        currency = d.pop("currency")

        attributes_jsonb = InventoryUnitAttributesJsonb.from_dict(d.pop("attributes_jsonb"))




        inventory_unit = cls(
            id=id,
            resource_id=resource_id,
            sku=sku,
            name=name,
            description=description,
            available_from=available_from,
            available_until=available_until,
            quantity=quantity,
            unit_price_minor=unit_price_minor,
            currency=currency,
            attributes_jsonb=attributes_jsonb,
        )


        inventory_unit.additional_properties = d
        return inventory_unit

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
