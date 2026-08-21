from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.refund_decide_request_authority import RefundDecideRequestAuthority
  from ..models.refund_decide_request_settlement import RefundDecideRequestSettlement
  from ..models.refund_line_item import RefundLineItem





T = TypeVar("T", bound="RefundDecideRequest")



@_attrs_define
class RefundDecideRequest:
    """ Internal: a merchant/owner approves or rejects an agent-opened refund ticket, or previews the amount (preview: true,
    no decision). `decision` is required unless preview is set. site_id is derived from the refunds row (looked up by
    refund_id) and gated via requireSiteRole admin (or, for the WooCommerce plugin relay, the per-site OMS signature);
    it is NOT taken from the body. Approving dispatches the on-chain send-back; the response is the updated Refund.

        Attributes:
            refund_id (str):
            decision (str | Unset): Merchant verdict on the ticket: "approved" | "rejected". Required for a real decide;
                OMITTED for a preview (preview: true is a read-only dry run of an approval).
            preview (bool | Unset): Dry run: when true, returns the server-derived { amount_minor, currency, refund_to,
                chain } for the caller to sign against, WITHOUT persisting or dispatching anything (the ticket stays
                'requested'). A preview needs no `decision`.
            note (str | Unset): Optional merchant note recorded with the decision.
            refund_line_items (list[RefundLineItem] | Unset): Optional PARTIAL selection the merchant confirms/adjusts on
                approve; it overrides the agent's advisory selection. Omitted keeps whatever the ticket carries. The taxed
                amount is derived server-side; the body carries no amount.
            authority (RefundDecideRequestAuthority | Unset): Optional NON-CUSTODIAL x402 refund on approve. The merchant
                signs the ERC-3009 reversal out of its OWN payTo and Facet only relays it (holds no key). Omitted falls back to
                a Facet-managed refund signer whose address equals payTo. The rail adapter binds the send-back's sender to the
                merchant payTo, its recipient to the buyer, and its value to the server-derived refund amount, and the
                facilitator re-verifies the signature before a cent moves.
            settlement (RefundDecideRequestSettlement | Unset): Optional NON-CUSTODIAL x402 refund the merchant settled
                THEMSELVES. Use when the merchant's wallet does not hand Facet the ERC-3009 signature `authority` carries; the
                merchant instead broadcasts a plain USDC.transfer from their own wallet and posts the hash here. Facet neither
                signs nor relays: it VERIFIES the transaction on-chain (emitted by the network's USDC contract, sent from the
                merchant payTo, received by the buyer, for at least the server-derived amount, mined at or after the capture)
                and only then fulfils the ticket, recording the hash as settlement_ref. One transaction settles at most one
                ticket. Mutually exclusive with `authority`; supplying both is a 400.
     """

    refund_id: str
    decision: str | Unset = UNSET
    preview: bool | Unset = UNSET
    note: str | Unset = UNSET
    refund_line_items: list[RefundLineItem] | Unset = UNSET
    authority: RefundDecideRequestAuthority | Unset = UNSET
    settlement: RefundDecideRequestSettlement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refund_decide_request_authority import RefundDecideRequestAuthority
        from ..models.refund_decide_request_settlement import RefundDecideRequestSettlement
        from ..models.refund_line_item import RefundLineItem
        refund_id = self.refund_id

        decision = self.decision

        preview = self.preview

        note = self.note

        refund_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.refund_line_items, Unset):
            refund_line_items = []
            for refund_line_items_item_data in self.refund_line_items:
                refund_line_items_item = refund_line_items_item_data.to_dict()
                refund_line_items.append(refund_line_items_item)



        authority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authority, Unset):
            authority = self.authority.to_dict()

        settlement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settlement, Unset):
            settlement = self.settlement.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refund_id": refund_id,
        })
        if decision is not UNSET:
            field_dict["decision"] = decision
        if preview is not UNSET:
            field_dict["preview"] = preview
        if note is not UNSET:
            field_dict["note"] = note
        if refund_line_items is not UNSET:
            field_dict["refund_line_items"] = refund_line_items
        if authority is not UNSET:
            field_dict["authority"] = authority
        if settlement is not UNSET:
            field_dict["settlement"] = settlement

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refund_decide_request_authority import RefundDecideRequestAuthority
        from ..models.refund_decide_request_settlement import RefundDecideRequestSettlement
        from ..models.refund_line_item import RefundLineItem
        d = dict(src_dict)
        refund_id = d.pop("refund_id")

        decision = d.pop("decision", UNSET)

        preview = d.pop("preview", UNSET)

        note = d.pop("note", UNSET)

        _refund_line_items = d.pop("refund_line_items", UNSET)
        refund_line_items: list[RefundLineItem] | Unset = UNSET
        if _refund_line_items is not UNSET:
            refund_line_items = []
            for refund_line_items_item_data in _refund_line_items:
                refund_line_items_item = RefundLineItem.from_dict(refund_line_items_item_data)



                refund_line_items.append(refund_line_items_item)


        _authority = d.pop("authority", UNSET)
        authority: RefundDecideRequestAuthority | Unset
        if isinstance(_authority,  Unset):
            authority = UNSET
        else:
            authority = RefundDecideRequestAuthority.from_dict(_authority)




        _settlement = d.pop("settlement", UNSET)
        settlement: RefundDecideRequestSettlement | Unset
        if isinstance(_settlement,  Unset):
            settlement = UNSET
        else:
            settlement = RefundDecideRequestSettlement.from_dict(_settlement)




        refund_decide_request = cls(
            refund_id=refund_id,
            decision=decision,
            preview=preview,
            note=note,
            refund_line_items=refund_line_items,
            authority=authority,
            settlement=settlement,
        )


        refund_decide_request.additional_properties = d
        return refund_decide_request

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
