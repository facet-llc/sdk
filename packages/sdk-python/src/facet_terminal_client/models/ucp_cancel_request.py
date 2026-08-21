from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ucp_cancel_request_cancel_line_items_item import UcpCancelRequestCancelLineItemsItem





T = TypeVar("T", bound="UcpCancelRequest")



@_attrs_define
class UcpCancelRequest:
    """ Cancel a committed-but-not-redeemed Boson exchange and refund the buyer (POST /ucp/v1/checkout-sessions/cancel). The
    buyer signs the cancel; a relayer sponsors the gas. Two modes, exactly one per request: SINGLE voucher via
    {exchange_id, signed_payload}, or PER-LINE (flag on) via {cancel_line_items} to cancel a selection of lines while
    the rest stays escrowed.

        Attributes:
            exchange_id (str | Unset): SINGLE-voucher mode: the committed-but-not-redeemed on-chain Boson exchange id to
                cancel.
            signed_payload (str | Unset): SINGLE-voucher mode: the buyer's signed boson-cancelVoucher meta-transaction. Only
                the voucher holder can produce it, so the cancel is buyer-authorized on-chain.
            cancel_line_items (list[UcpCancelRequestCancelLineItemsItem] | Unset): PER-LINE mode (requires
                FACET_BOSON_PER_LINE_ESCROW): a selection of committed cart lines to cancel and refund, each cancelled
                independently against its own exchange, leaving unselected siblings committed. Provide this INSTEAD OF the top-
                level exchange_id/signed_payload; the whole selection is authorized as a set before any relay, and a per-line
                failure is isolated on that line.
     """

    exchange_id: str | Unset = UNSET
    signed_payload: str | Unset = UNSET
    cancel_line_items: list[UcpCancelRequestCancelLineItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ucp_cancel_request_cancel_line_items_item import UcpCancelRequestCancelLineItemsItem
        exchange_id = self.exchange_id

        signed_payload = self.signed_payload

        cancel_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cancel_line_items, Unset):
            cancel_line_items = []
            for cancel_line_items_item_data in self.cancel_line_items:
                cancel_line_items_item = cancel_line_items_item_data.to_dict()
                cancel_line_items.append(cancel_line_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if signed_payload is not UNSET:
            field_dict["signed_payload"] = signed_payload
        if cancel_line_items is not UNSET:
            field_dict["cancel_line_items"] = cancel_line_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ucp_cancel_request_cancel_line_items_item import UcpCancelRequestCancelLineItemsItem
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        signed_payload = d.pop("signed_payload", UNSET)

        _cancel_line_items = d.pop("cancel_line_items", UNSET)
        cancel_line_items: list[UcpCancelRequestCancelLineItemsItem] | Unset = UNSET
        if _cancel_line_items is not UNSET:
            cancel_line_items = []
            for cancel_line_items_item_data in _cancel_line_items:
                cancel_line_items_item = UcpCancelRequestCancelLineItemsItem.from_dict(cancel_line_items_item_data)



                cancel_line_items.append(cancel_line_items_item)


        ucp_cancel_request = cls(
            exchange_id=exchange_id,
            signed_payload=signed_payload,
            cancel_line_items=cancel_line_items,
        )


        ucp_cancel_request.additional_properties = d
        return ucp_cancel_request

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
