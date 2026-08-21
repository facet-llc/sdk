from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ucp_dispute_request_dispute_line_items_item import UcpDisputeRequestDisputeLineItemsItem





T = TypeVar("T", bound="UcpDisputeRequest")



@_attrs_define
class UcpDisputeRequest:
    """ Dispute a redeemed Boson exchange (POST /ucp/v1/checkout-sessions/dispute). Buyer-signed; a relayer sponsors the
    gas. Two modes, exactly one per request: SINGLE voucher via {exchange_id, action, signed_payload} (action
    raise/retract/escalate/resolve; resolve completes a partial-refund split against the merchant-offered seller half),
    or PER-LINE (flag on) via {dispute_line_items} to dispute a selection of lines (raise/retract/escalate).

        Attributes:
            exchange_id (str | Unset): SINGLE-voucher mode: the redeemed on-chain Boson exchange id to dispute.
            action (str | Unset): SINGLE-voucher mode: the dispute action: "raise", "retract", "escalate", or "resolve".
                resolve completes a partial-refund split: it carries the seller half the merchant offered at approve, and the
                Terminal validates the buyer's payload against the server-derived split before relaying it.
            signed_payload (str | Unset): SINGLE-voucher mode: the buyer's signed boson dispute meta-transaction for the
                chosen action.
            dispute_line_items (list[UcpDisputeRequestDisputeLineItemsItem] | Unset): PER-LINE mode (requires
                FACET_BOSON_PER_LINE_ESCROW): a selection of redeemed cart lines to dispute, each raised/retracted/escalated
                independently against its own exchange, leaving unselected siblings untouched. Provide this INSTEAD OF the top-
                level exchange_id/action/signed_payload; the whole selection is authorized as a set before any relay, and a per-
                line failure is isolated on that line.
     """

    exchange_id: str | Unset = UNSET
    action: str | Unset = UNSET
    signed_payload: str | Unset = UNSET
    dispute_line_items: list[UcpDisputeRequestDisputeLineItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ucp_dispute_request_dispute_line_items_item import UcpDisputeRequestDisputeLineItemsItem
        exchange_id = self.exchange_id

        action = self.action

        signed_payload = self.signed_payload

        dispute_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dispute_line_items, Unset):
            dispute_line_items = []
            for dispute_line_items_item_data in self.dispute_line_items:
                dispute_line_items_item = dispute_line_items_item_data.to_dict()
                dispute_line_items.append(dispute_line_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if action is not UNSET:
            field_dict["action"] = action
        if signed_payload is not UNSET:
            field_dict["signed_payload"] = signed_payload
        if dispute_line_items is not UNSET:
            field_dict["dispute_line_items"] = dispute_line_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ucp_dispute_request_dispute_line_items_item import UcpDisputeRequestDisputeLineItemsItem
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        action = d.pop("action", UNSET)

        signed_payload = d.pop("signed_payload", UNSET)

        _dispute_line_items = d.pop("dispute_line_items", UNSET)
        dispute_line_items: list[UcpDisputeRequestDisputeLineItemsItem] | Unset = UNSET
        if _dispute_line_items is not UNSET:
            dispute_line_items = []
            for dispute_line_items_item_data in _dispute_line_items:
                dispute_line_items_item = UcpDisputeRequestDisputeLineItemsItem.from_dict(dispute_line_items_item_data)



                dispute_line_items.append(dispute_line_items_item)


        ucp_dispute_request = cls(
            exchange_id=exchange_id,
            action=action,
            signed_payload=signed_payload,
            dispute_line_items=dispute_line_items,
        )


        ucp_dispute_request.additional_properties = d
        return ucp_dispute_request

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
