from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RefundContextResponse")



@_attrs_define
class RefundContextResponse:
    """ 
        Attributes:
            order_id (str):
            pay_to (None | str): The wallet the refund must come OUT of, on the current plane. The plugin checks the
                connected wallet against it before a broadcast spends real USDC, and uses it to pick a settlement path: sign an
                ERC-3009 for Facet to relay, or broadcast a plain USDC.transfer directly from that wallet.
            chain (None | str): USDC chain slug: 'base' or 'base-sepolia'.
            facet_can_sign (bool): True when Facet holds a managed signer for pay_to, so a merchant-initiated refund settles
                server-side and the storefront must NOT prompt for a wallet. False means the payout wallet is the merchant's own
                and only they can move it.
            currency (str):
            captured_minor (int): The order's captured total, in cents.
            refundable_minor (int): Cents still refundable: captured minus everything already claimed on the shared ledger.
                ADVISORY pre-flight so the plugin can refuse before a merchant broadcasts USDC that could never be recorded; the
                authoritative over-refund cap is still the claim RPC at webhook time.
            refund_to (None | str | Unset): The buyer wallet the refund must go to, captured at settle. Server-derived,
                never accepted from the caller. null when the order has no captured buyer wallet, in which case no x402 refund
                can be targeted.
     """

    order_id: str
    pay_to: None | str
    chain: None | str
    facet_can_sign: bool
    currency: str
    captured_minor: int
    refundable_minor: int
    refund_to: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        pay_to: None | str
        pay_to = self.pay_to

        chain: None | str
        chain = self.chain

        facet_can_sign = self.facet_can_sign

        currency = self.currency

        captured_minor = self.captured_minor

        refundable_minor = self.refundable_minor

        refund_to: None | str | Unset
        if isinstance(self.refund_to, Unset):
            refund_to = UNSET
        else:
            refund_to = self.refund_to


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
            "pay_to": pay_to,
            "chain": chain,
            "facet_can_sign": facet_can_sign,
            "currency": currency,
            "captured_minor": captured_minor,
            "refundable_minor": refundable_minor,
        })
        if refund_to is not UNSET:
            field_dict["refund_to"] = refund_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id")

        def _parse_pay_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pay_to = _parse_pay_to(d.pop("pay_to"))


        def _parse_chain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        chain = _parse_chain(d.pop("chain"))


        facet_can_sign = d.pop("facet_can_sign")

        currency = d.pop("currency")

        captured_minor = d.pop("captured_minor")

        refundable_minor = d.pop("refundable_minor")

        def _parse_refund_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refund_to = _parse_refund_to(d.pop("refund_to", UNSET))


        refund_context_response = cls(
            order_id=order_id,
            pay_to=pay_to,
            chain=chain,
            facet_can_sign=facet_can_sign,
            currency=currency,
            captured_minor=captured_minor,
            refundable_minor=refundable_minor,
            refund_to=refund_to,
        )


        refund_context_response.additional_properties = d
        return refund_context_response

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
