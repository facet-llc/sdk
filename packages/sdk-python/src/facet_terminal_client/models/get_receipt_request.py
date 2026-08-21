from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_receipt_request_wallet_auth import GetReceiptRequestWalletAuth





T = TypeVar("T", bound="GetReceiptRequest")



@_attrs_define
class GetReceiptRequest:
    """ 
        Attributes:
            order_id (str):
            wallet_auth (GetReceiptRequestWalletAuth | Unset):
     """

    order_id: str
    wallet_auth: GetReceiptRequestWalletAuth | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_receipt_request_wallet_auth import GetReceiptRequestWalletAuth
        order_id = self.order_id

        wallet_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wallet_auth, Unset):
            wallet_auth = self.wallet_auth.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
        })
        if wallet_auth is not UNSET:
            field_dict["wallet_auth"] = wallet_auth

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_receipt_request_wallet_auth import GetReceiptRequestWalletAuth
        d = dict(src_dict)
        order_id = d.pop("order_id")

        _wallet_auth = d.pop("wallet_auth", UNSET)
        wallet_auth: GetReceiptRequestWalletAuth | Unset
        if isinstance(_wallet_auth,  Unset):
            wallet_auth = UNSET
        else:
            wallet_auth = GetReceiptRequestWalletAuth.from_dict(_wallet_auth)




        get_receipt_request = cls(
            order_id=order_id,
            wallet_auth=wallet_auth,
        )


        get_receipt_request.additional_properties = d
        return get_receipt_request

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
