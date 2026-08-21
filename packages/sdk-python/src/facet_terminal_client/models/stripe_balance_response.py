from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.stripe_balance_amount import StripeBalanceAmount





T = TypeVar("T", bound="StripeBalanceResponse")



@_attrs_define
class StripeBalanceResponse:
    """ 
        Attributes:
            connected (bool):
            account_id (None | str):
            charges_enabled (bool):
            payouts_enabled (bool):
            details_submitted (bool):
            available (list[StripeBalanceAmount]):
            pending (list[StripeBalanceAmount]):
     """

    connected: bool
    account_id: None | str
    charges_enabled: bool
    payouts_enabled: bool
    details_submitted: bool
    available: list[StripeBalanceAmount]
    pending: list[StripeBalanceAmount]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stripe_balance_amount import StripeBalanceAmount
        connected = self.connected

        account_id: None | str
        account_id = self.account_id

        charges_enabled = self.charges_enabled

        payouts_enabled = self.payouts_enabled

        details_submitted = self.details_submitted

        available = []
        for available_item_data in self.available:
            available_item = available_item_data.to_dict()
            available.append(available_item)



        pending = []
        for pending_item_data in self.pending:
            pending_item = pending_item_data.to_dict()
            pending.append(pending_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connected": connected,
            "account_id": account_id,
            "charges_enabled": charges_enabled,
            "payouts_enabled": payouts_enabled,
            "details_submitted": details_submitted,
            "available": available,
            "pending": pending,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stripe_balance_amount import StripeBalanceAmount
        d = dict(src_dict)
        connected = d.pop("connected")

        def _parse_account_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_id = _parse_account_id(d.pop("account_id"))


        charges_enabled = d.pop("charges_enabled")

        payouts_enabled = d.pop("payouts_enabled")

        details_submitted = d.pop("details_submitted")

        available = []
        _available = d.pop("available")
        for available_item_data in (_available):
            available_item = StripeBalanceAmount.from_dict(available_item_data)



            available.append(available_item)


        pending = []
        _pending = d.pop("pending")
        for pending_item_data in (_pending):
            pending_item = StripeBalanceAmount.from_dict(pending_item_data)



            pending.append(pending_item)


        stripe_balance_response = cls(
            connected=connected,
            account_id=account_id,
            charges_enabled=charges_enabled,
            payouts_enabled=payouts_enabled,
            details_submitted=details_submitted,
            available=available,
            pending=pending,
        )


        stripe_balance_response.additional_properties = d
        return stripe_balance_response

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
