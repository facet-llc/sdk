from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.payments_quote_request_amount import PaymentsQuoteRequestAmount





T = TypeVar("T", bound="PaymentsQuoteRequest")



@_attrs_define
class PaymentsQuoteRequest:
    """ 
        Attributes:
            site_id (str): Merchant site UUID the agent is buying from.
            amount (PaymentsQuoteRequestAmount):
            rail_id (str | Unset): Payment rail id (default coin/usdc-base; coin/usdc-base-sepolia on the sandbox plane).
     """

    site_id: str
    amount: PaymentsQuoteRequestAmount
    rail_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.payments_quote_request_amount import PaymentsQuoteRequestAmount
        site_id = self.site_id

        amount = self.amount.to_dict()

        rail_id = self.rail_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "amount": amount,
        })
        if rail_id is not UNSET:
            field_dict["rail_id"] = rail_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payments_quote_request_amount import PaymentsQuoteRequestAmount
        d = dict(src_dict)
        site_id = d.pop("site_id")

        amount = PaymentsQuoteRequestAmount.from_dict(d.pop("amount"))




        rail_id = d.pop("rail_id", UNSET)

        payments_quote_request = cls(
            site_id=site_id,
            amount=amount,
            rail_id=rail_id,
        )


        payments_quote_request.additional_properties = d
        return payments_quote_request

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
