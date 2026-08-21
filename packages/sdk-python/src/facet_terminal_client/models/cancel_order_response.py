from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_status import OrderStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.order_line_item import OrderLineItem
  from ..models.shipment import Shipment





T = TypeVar("T", bound="CancelOrderResponse")



@_attrs_define
class CancelOrderResponse:
    """ 
        Attributes:
            order_id (str):
            reservation_id (None | str):
            status (OrderStatus):
            amount (float):
            currency (str):
            rail (None | str):
            kya_charge_id (None | str):
            line_items (list[OrderLineItem]):
            created_at (str):
            settled_at (None | str):
            fulfillment_ref (str | Unset):
            shipments (list[Shipment] | Unset):
     """

    order_id: str
    reservation_id: None | str
    status: OrderStatus
    amount: float
    currency: str
    rail: None | str
    kya_charge_id: None | str
    line_items: list[OrderLineItem]
    created_at: str
    settled_at: None | str
    fulfillment_ref: str | Unset = UNSET
    shipments: list[Shipment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_line_item import OrderLineItem
        from ..models.shipment import Shipment
        order_id = self.order_id

        reservation_id: None | str
        reservation_id = self.reservation_id

        status = self.status.value

        amount = self.amount

        currency = self.currency

        rail: None | str
        rail = self.rail

        kya_charge_id: None | str
        kya_charge_id = self.kya_charge_id

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)



        created_at = self.created_at

        settled_at: None | str
        settled_at = self.settled_at

        fulfillment_ref = self.fulfillment_ref

        shipments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shipments, Unset):
            shipments = []
            for shipments_item_data in self.shipments:
                shipments_item = shipments_item_data.to_dict()
                shipments.append(shipments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
            "reservation_id": reservation_id,
            "status": status,
            "amount": amount,
            "currency": currency,
            "rail": rail,
            "kya_charge_id": kya_charge_id,
            "line_items": line_items,
            "created_at": created_at,
            "settled_at": settled_at,
        })
        if fulfillment_ref is not UNSET:
            field_dict["fulfillment_ref"] = fulfillment_ref
        if shipments is not UNSET:
            field_dict["shipments"] = shipments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_line_item import OrderLineItem
        from ..models.shipment import Shipment
        d = dict(src_dict)
        order_id = d.pop("order_id")

        def _parse_reservation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reservation_id = _parse_reservation_id(d.pop("reservation_id"))


        status = OrderStatus(d.pop("status"))




        amount = d.pop("amount")

        currency = d.pop("currency")

        def _parse_rail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rail = _parse_rail(d.pop("rail"))


        def _parse_kya_charge_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        kya_charge_id = _parse_kya_charge_id(d.pop("kya_charge_id"))


        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in (_line_items):
            line_items_item = OrderLineItem.from_dict(line_items_item_data)



            line_items.append(line_items_item)


        created_at = d.pop("created_at")

        def _parse_settled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        settled_at = _parse_settled_at(d.pop("settled_at"))


        fulfillment_ref = d.pop("fulfillment_ref", UNSET)

        _shipments = d.pop("shipments", UNSET)
        shipments: list[Shipment] | Unset = UNSET
        if _shipments is not UNSET:
            shipments = []
            for shipments_item_data in _shipments:
                shipments_item = Shipment.from_dict(shipments_item_data)



                shipments.append(shipments_item)


        cancel_order_response = cls(
            order_id=order_id,
            reservation_id=reservation_id,
            status=status,
            amount=amount,
            currency=currency,
            rail=rail,
            kya_charge_id=kya_charge_id,
            line_items=line_items,
            created_at=created_at,
            settled_at=settled_at,
            fulfillment_ref=fulfillment_ref,
            shipments=shipments,
        )


        cancel_order_response.additional_properties = d
        return cancel_order_response

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
