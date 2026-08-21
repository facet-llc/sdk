from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ucp_submit_redeem_request_redeem_line_items_item import UcpSubmitRedeemRequestRedeemLineItemsItem





T = TypeVar("T", bound="UcpSubmitRedeemRequest")



@_attrs_define
class UcpSubmitRedeemRequest:
    """ Redeem a committed Boson escrow (POST /ucp/v1/checkout-sessions/redeem). Two modes, exactly one per request. SINGLE
    voucher: provide {exchange_id, signed_payload}; the buyer's pre-signed redeem is STORED (the buyer cannot sign it
    until COMMIT assigns the exchange id) and fired later by the merchant fulfillment webhook. PER-LINE (flag on):
    provide {redeem_line_items}; each selected line's redeem fires immediately against its own exchange.

        Attributes:
            exchange_id (str | Unset): SINGLE-voucher mode: the committed on-chain Boson exchange id the redeem releases.
            signed_payload (str | Unset): SINGLE-voucher mode: the buyer's signed boson-redeem meta-transaction. Held until
                the merchant marks the order fulfilled, then submitted by the fulfillment webhook.
            redeem_line_items (list[UcpSubmitRedeemRequestRedeemLineItemsItem] | Unset): PER-LINE mode (requires
                FACET_BOSON_PER_LINE_ESCROW): a selection of committed cart lines to redeem. Each line's redeem fires
                IMMEDIATELY and independently against its own exchange, leaving unselected siblings committed. Provide this
                INSTEAD OF the top-level exchange_id/signed_payload; the whole selection is authorized as a set before any
                relay, and a per-line failure is isolated on that line.
     """

    exchange_id: str | Unset = UNSET
    signed_payload: str | Unset = UNSET
    redeem_line_items: list[UcpSubmitRedeemRequestRedeemLineItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ucp_submit_redeem_request_redeem_line_items_item import UcpSubmitRedeemRequestRedeemLineItemsItem
        exchange_id = self.exchange_id

        signed_payload = self.signed_payload

        redeem_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redeem_line_items, Unset):
            redeem_line_items = []
            for redeem_line_items_item_data in self.redeem_line_items:
                redeem_line_items_item = redeem_line_items_item_data.to_dict()
                redeem_line_items.append(redeem_line_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if signed_payload is not UNSET:
            field_dict["signed_payload"] = signed_payload
        if redeem_line_items is not UNSET:
            field_dict["redeem_line_items"] = redeem_line_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ucp_submit_redeem_request_redeem_line_items_item import UcpSubmitRedeemRequestRedeemLineItemsItem
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        signed_payload = d.pop("signed_payload", UNSET)

        _redeem_line_items = d.pop("redeem_line_items", UNSET)
        redeem_line_items: list[UcpSubmitRedeemRequestRedeemLineItemsItem] | Unset = UNSET
        if _redeem_line_items is not UNSET:
            redeem_line_items = []
            for redeem_line_items_item_data in _redeem_line_items:
                redeem_line_items_item = UcpSubmitRedeemRequestRedeemLineItemsItem.from_dict(redeem_line_items_item_data)



                redeem_line_items.append(redeem_line_items_item)


        ucp_submit_redeem_request = cls(
            exchange_id=exchange_id,
            signed_payload=signed_payload,
            redeem_line_items=redeem_line_items,
        )


        ucp_submit_redeem_request.additional_properties = d
        return ucp_submit_redeem_request

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
