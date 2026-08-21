from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ucp_dispute_request_dispute_line_items_item_action import UcpDisputeRequestDisputeLineItemsItemAction






T = TypeVar("T", bound="UcpDisputeRequestDisputeLineItemsItem")



@_attrs_define
class UcpDisputeRequestDisputeLineItemsItem:
    """ 
        Attributes:
            exchange_id (str): This line's redeemed on-chain Boson exchange id.
            action (UcpDisputeRequestDisputeLineItemsItemAction): This line's dispute action. Per-line supports the buyer-
                only actions raise/retract/escalate; resolve is single-voucher only (it carries the seller's counter-signature
                and is a mutual flow).
            signed_payload (str): The buyer's signed boson dispute meta-transaction for THIS line and action.
     """

    exchange_id: str
    action: UcpDisputeRequestDisputeLineItemsItemAction
    signed_payload: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        action = self.action.value

        signed_payload = self.signed_payload


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "exchange_id": exchange_id,
            "action": action,
            "signed_payload": signed_payload,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id")

        action = UcpDisputeRequestDisputeLineItemsItemAction(d.pop("action"))




        signed_payload = d.pop("signed_payload")

        ucp_dispute_request_dispute_line_items_item = cls(
            exchange_id=exchange_id,
            action=action,
            signed_payload=signed_payload,
        )


        ucp_dispute_request_dispute_line_items_item.additional_properties = d
        return ucp_dispute_request_dispute_line_items_item

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
