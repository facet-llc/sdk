from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.handle_webhook_dispatch_op import HandleWebhookDispatchOp
from ..types import UNSET, Unset






T = TypeVar("T", bound="HandleWebhookDispatch")



@_attrs_define
class HandleWebhookDispatch:
    """ 
        Attributes:
            op (HandleWebhookDispatchOp):
            site_id (str):
            rail_id (str | Unset): Stable rail identifier — namespaces match /v1/terms.settlement_rails (e.g. 'coin/usdc-
                base', 'card/stripe', 'voucher/skyfire').
            idempotency_key (str | Unset):
            merchant_id (str | Unset):
     """

    op: HandleWebhookDispatchOp
    site_id: str
    rail_id: str | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    merchant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        op = self.op.value

        site_id = self.site_id

        rail_id = self.rail_id

        idempotency_key = self.idempotency_key

        merchant_id = self.merchant_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "op": op,
            "site_id": site_id,
        })
        if rail_id is not UNSET:
            field_dict["rail_id"] = rail_id
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if merchant_id is not UNSET:
            field_dict["merchant_id"] = merchant_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        op = HandleWebhookDispatchOp(d.pop("op"))




        site_id = d.pop("site_id")

        rail_id = d.pop("rail_id", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        merchant_id = d.pop("merchant_id", UNSET)

        handle_webhook_dispatch = cls(
            op=op,
            site_id=site_id,
            rail_id=rail_id,
            idempotency_key=idempotency_key,
            merchant_id=merchant_id,
        )


        handle_webhook_dispatch.additional_properties = d
        return handle_webhook_dispatch

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
