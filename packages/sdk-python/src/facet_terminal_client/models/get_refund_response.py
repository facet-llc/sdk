from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.refund_status import RefundStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.refund_line_item import RefundLineItem





T = TypeVar("T", bound="GetRefundResponse")



@_attrs_define
class GetRefundResponse:
    """ 
        Attributes:
            refund_id (str):
            order_id (str):
            status (RefundStatus):
            reason (str):
            decision (None | str):
            created_at (str):
            resolved_at (None | str):
            settlement_ref (None | str): On-chain send-back tx hash once the refund is fulfilled; null until then.
            receipt_verified (bool): True when the agent presented a valid signed settlement receipt for the order.
            refund_line_items (list[RefundLineItem] | None | Unset): The partial-refund line selection, once set; null = a
                full-order refund.
            amount_minor (int | None | Unset): The derived partial amount in cents, once a partial is approved; null
                otherwise.
            seller_resolution_signature (None | str | Unset): Boson W2 resolveDispute split: the seller's offered EIP-712
                Resolution half, present once a partial on a Boson escrow order is approved. The order's buyer co-signs +
                submits the resolveDispute with it. null otherwise.
            buyer_percent_bps (int | None | Unset): The server-derived split in basis points (0..10000) for the
                resolveDispute; null otherwise.
            boson_exchange_id (None | str | Unset): The on-chain Boson exchange the resolveDispute split resolves; null
                otherwise.
     """

    refund_id: str
    order_id: str
    status: RefundStatus
    reason: str
    decision: None | str
    created_at: str
    resolved_at: None | str
    settlement_ref: None | str
    receipt_verified: bool
    refund_line_items: list[RefundLineItem] | None | Unset = UNSET
    amount_minor: int | None | Unset = UNSET
    seller_resolution_signature: None | str | Unset = UNSET
    buyer_percent_bps: int | None | Unset = UNSET
    boson_exchange_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refund_line_item import RefundLineItem
        refund_id = self.refund_id

        order_id = self.order_id

        status = self.status.value

        reason = self.reason

        decision: None | str
        decision = self.decision

        created_at = self.created_at

        resolved_at: None | str
        resolved_at = self.resolved_at

        settlement_ref: None | str
        settlement_ref = self.settlement_ref

        receipt_verified = self.receipt_verified

        refund_line_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.refund_line_items, Unset):
            refund_line_items = UNSET
        elif isinstance(self.refund_line_items, list):
            refund_line_items = []
            for refund_line_items_type_0_item_data in self.refund_line_items:
                refund_line_items_type_0_item = refund_line_items_type_0_item_data.to_dict()
                refund_line_items.append(refund_line_items_type_0_item)


        else:
            refund_line_items = self.refund_line_items

        amount_minor: int | None | Unset
        if isinstance(self.amount_minor, Unset):
            amount_minor = UNSET
        else:
            amount_minor = self.amount_minor

        seller_resolution_signature: None | str | Unset
        if isinstance(self.seller_resolution_signature, Unset):
            seller_resolution_signature = UNSET
        else:
            seller_resolution_signature = self.seller_resolution_signature

        buyer_percent_bps: int | None | Unset
        if isinstance(self.buyer_percent_bps, Unset):
            buyer_percent_bps = UNSET
        else:
            buyer_percent_bps = self.buyer_percent_bps

        boson_exchange_id: None | str | Unset
        if isinstance(self.boson_exchange_id, Unset):
            boson_exchange_id = UNSET
        else:
            boson_exchange_id = self.boson_exchange_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refund_id": refund_id,
            "order_id": order_id,
            "status": status,
            "reason": reason,
            "decision": decision,
            "created_at": created_at,
            "resolved_at": resolved_at,
            "settlement_ref": settlement_ref,
            "receipt_verified": receipt_verified,
        })
        if refund_line_items is not UNSET:
            field_dict["refund_line_items"] = refund_line_items
        if amount_minor is not UNSET:
            field_dict["amount_minor"] = amount_minor
        if seller_resolution_signature is not UNSET:
            field_dict["seller_resolution_signature"] = seller_resolution_signature
        if buyer_percent_bps is not UNSET:
            field_dict["buyer_percent_bps"] = buyer_percent_bps
        if boson_exchange_id is not UNSET:
            field_dict["boson_exchange_id"] = boson_exchange_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refund_line_item import RefundLineItem
        d = dict(src_dict)
        refund_id = d.pop("refund_id")

        order_id = d.pop("order_id")

        status = RefundStatus(d.pop("status"))




        reason = d.pop("reason")

        def _parse_decision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decision = _parse_decision(d.pop("decision"))


        created_at = d.pop("created_at")

        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))


        def _parse_settlement_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        settlement_ref = _parse_settlement_ref(d.pop("settlement_ref"))


        receipt_verified = d.pop("receipt_verified")

        def _parse_refund_line_items(data: object) -> list[RefundLineItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                refund_line_items_type_0 = []
                _refund_line_items_type_0 = data
                for refund_line_items_type_0_item_data in (_refund_line_items_type_0):
                    refund_line_items_type_0_item = RefundLineItem.from_dict(refund_line_items_type_0_item_data)



                    refund_line_items_type_0.append(refund_line_items_type_0_item)

                return refund_line_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RefundLineItem] | None | Unset, data)

        refund_line_items = _parse_refund_line_items(d.pop("refund_line_items", UNSET))


        def _parse_amount_minor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        amount_minor = _parse_amount_minor(d.pop("amount_minor", UNSET))


        def _parse_seller_resolution_signature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seller_resolution_signature = _parse_seller_resolution_signature(d.pop("seller_resolution_signature", UNSET))


        def _parse_buyer_percent_bps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        buyer_percent_bps = _parse_buyer_percent_bps(d.pop("buyer_percent_bps", UNSET))


        def _parse_boson_exchange_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boson_exchange_id = _parse_boson_exchange_id(d.pop("boson_exchange_id", UNSET))


        get_refund_response = cls(
            refund_id=refund_id,
            order_id=order_id,
            status=status,
            reason=reason,
            decision=decision,
            created_at=created_at,
            resolved_at=resolved_at,
            settlement_ref=settlement_ref,
            receipt_verified=receipt_verified,
            refund_line_items=refund_line_items,
            amount_minor=amount_minor,
            seller_resolution_signature=seller_resolution_signature,
            buyer_percent_bps=buyer_percent_bps,
            boson_exchange_id=boson_exchange_id,
        )


        get_refund_response.additional_properties = d
        return get_refund_response

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
