from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AcpCheckoutSession")



@_attrs_define
class AcpCheckoutSession:
    """ An ACP checkout session, returned by CREATE, UPDATE, and GET. Amount and payee are always server-resolved from the
    reservation, never trusted from the platform request.

        Attributes:
            id (str | Unset): The checkout session id (the Terminal reservation id).
            status (str | Unset): ACP status enum: not_ready_for_payment | ready_for_payment | completed | canceled. A
                distinct FSM from UCP's own status lifecycle.
            currency (str | Unset): ISO 4217 currency of the priced cart.
            line_items (Any | Unset): Server-priced line items: [{ id, item, quantity, base_amount, subtotal, tax, total }],
                per the formal CheckoutSession.line_items schema.
            totals (Any | Unset): [{ type, display_text, amount }], the array-of-entries totals shape the vendored spec's
                own CheckoutSession.example uses (not a single Totals object).
     """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    currency: str | Unset = UNSET
    line_items: Any | Unset = UNSET
    totals: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        currency = self.currency

        line_items = self.line_items

        totals = self.totals


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        currency = d.pop("currency", UNSET)

        line_items = d.pop("line_items", UNSET)

        totals = d.pop("totals", UNSET)

        acp_checkout_session = cls(
            id=id,
            status=status,
            currency=currency,
            line_items=line_items,
            totals=totals,
        )


        acp_checkout_session.additional_properties = d
        return acp_checkout_session

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
