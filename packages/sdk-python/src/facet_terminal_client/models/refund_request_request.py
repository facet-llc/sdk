from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.refund_line_item import RefundLineItem
  from ..models.refund_request_request_buyer_auth import RefundRequestRequestBuyerAuth
  from ..models.refund_request_request_receipt import RefundRequestRequestReceipt





T = TypeVar("T", bound="RefundRequestRequest")



@_attrs_define
class RefundRequestRequest:
    """ 
        Attributes:
            order_id (str):
            reason (str):
            refund_line_items (list[RefundLineItem] | Unset): Optional PARTIAL selection: refund only these lines instead of
                the whole order. Advisory at request time (the merchant is authoritative and may adjust it at decide); server-
                validated against the order. Omitted = a full-order refund.
            buyer_auth (RefundRequestRequestBuyerAuth | Unset): Optional buyer wallet attestation that authorizes this
                refund request WITHOUT a platform co-signature, on stores that enable autonomous dual-key. The buyer signs an
                EIP-191 challenge binding the order and wallet; the Terminal recovers it and requires it to equal the wallet-
                bound KYA's payer_wallet, single-use and fresh. It is the refund-request analogue of the buyer-signed meta-tx on
                cancel / dispute, and is ignored when a platform signature is present. Opens the ticket only; no funds move
                until the merchant approves.
            receipt (RefundRequestRequestReceipt | Unset): Optional Ed25519-signed settlement receipt (the signed settle
                response the agent received). When valid and bound to this order, sets receipt_verified on the ticket; it never
                gates the refund.
     """

    order_id: str
    reason: str
    refund_line_items: list[RefundLineItem] | Unset = UNSET
    buyer_auth: RefundRequestRequestBuyerAuth | Unset = UNSET
    receipt: RefundRequestRequestReceipt | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refund_line_item import RefundLineItem
        from ..models.refund_request_request_buyer_auth import RefundRequestRequestBuyerAuth
        from ..models.refund_request_request_receipt import RefundRequestRequestReceipt
        order_id = self.order_id

        reason = self.reason

        refund_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.refund_line_items, Unset):
            refund_line_items = []
            for refund_line_items_item_data in self.refund_line_items:
                refund_line_items_item = refund_line_items_item_data.to_dict()
                refund_line_items.append(refund_line_items_item)



        buyer_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buyer_auth, Unset):
            buyer_auth = self.buyer_auth.to_dict()

        receipt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.receipt, Unset):
            receipt = self.receipt.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
            "reason": reason,
        })
        if refund_line_items is not UNSET:
            field_dict["refund_line_items"] = refund_line_items
        if buyer_auth is not UNSET:
            field_dict["buyer_auth"] = buyer_auth
        if receipt is not UNSET:
            field_dict["receipt"] = receipt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refund_line_item import RefundLineItem
        from ..models.refund_request_request_buyer_auth import RefundRequestRequestBuyerAuth
        from ..models.refund_request_request_receipt import RefundRequestRequestReceipt
        d = dict(src_dict)
        order_id = d.pop("order_id")

        reason = d.pop("reason")

        _refund_line_items = d.pop("refund_line_items", UNSET)
        refund_line_items: list[RefundLineItem] | Unset = UNSET
        if _refund_line_items is not UNSET:
            refund_line_items = []
            for refund_line_items_item_data in _refund_line_items:
                refund_line_items_item = RefundLineItem.from_dict(refund_line_items_item_data)



                refund_line_items.append(refund_line_items_item)


        _buyer_auth = d.pop("buyer_auth", UNSET)
        buyer_auth: RefundRequestRequestBuyerAuth | Unset
        if isinstance(_buyer_auth,  Unset):
            buyer_auth = UNSET
        else:
            buyer_auth = RefundRequestRequestBuyerAuth.from_dict(_buyer_auth)




        _receipt = d.pop("receipt", UNSET)
        receipt: RefundRequestRequestReceipt | Unset
        if isinstance(_receipt,  Unset):
            receipt = UNSET
        else:
            receipt = RefundRequestRequestReceipt.from_dict(_receipt)




        refund_request_request = cls(
            order_id=order_id,
            reason=reason,
            refund_line_items=refund_line_items,
            buyer_auth=buyer_auth,
            receipt=receipt,
        )


        refund_request_request.additional_properties = d
        return refund_request_request

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
