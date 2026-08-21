from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpCheckoutCreateResponse")



@_attrs_define
class UcpCheckoutCreateResponse:
    """ A UCP checkout session. The llc.facet.x402 handler carries the SERVER-resolved pay_to and amount the platform must
    satisfy; both come from the reservation + the merchant's sites row, never the request.

        Attributes:
            id (str | Unset): The checkout session id (the Terminal reservation id).
            status (str | Unset): Checkout status, e.g. "ready_for_complete".
            currency (str | Unset): ISO 4217 currency of the priced line item.
            default_rail (str | Unset): HINT: the site's default settlement rail handler id (llc.facet.x402 for a Shopify
                store, llc.facet.boson_escrow for WooCommerce), derived from the site's per-platform default arm. Always one of
                the advertised payment_handlers. Advisory only: the rail is still chosen at COMPLETE by which credential the
                buyer presents, and pay_to stays server-bound.
            payment_handlers (Any | Unset): Server-resolved payment requirements keyed by handler id (llc.facet.x402):
                network, USDC asset, pay_to, and the server-derived amount.
     """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    currency: str | Unset = UNSET
    default_rail: str | Unset = UNSET
    payment_handlers: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        currency = self.currency

        default_rail = self.default_rail

        payment_handlers = self.payment_handlers


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
        if default_rail is not UNSET:
            field_dict["default_rail"] = default_rail
        if payment_handlers is not UNSET:
            field_dict["payment_handlers"] = payment_handlers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        currency = d.pop("currency", UNSET)

        default_rail = d.pop("default_rail", UNSET)

        payment_handlers = d.pop("payment_handlers", UNSET)

        ucp_checkout_create_response = cls(
            id=id,
            status=status,
            currency=currency,
            default_rail=default_rail,
            payment_handlers=payment_handlers,
        )


        ucp_checkout_create_response.additional_properties = d
        return ucp_checkout_create_response

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
