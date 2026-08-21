from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RefundRequestRequestReceipt")



@_attrs_define
class RefundRequestRequestReceipt:
    """ Optional Ed25519-signed settlement receipt (the signed settle response the agent received). When valid and bound to
    this order, sets receipt_verified on the ticket; it never gates the refund.

        Attributes:
            body (str):
            signature (str):
            trace_id (str):
            path (str | Unset):
     """

    body: str
    signature: str
    trace_id: str
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        body = self.body

        signature = self.signature

        trace_id = self.trace_id

        path = self.path


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "body": body,
            "signature": signature,
            "trace_id": trace_id,
        })
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        signature = d.pop("signature")

        trace_id = d.pop("trace_id")

        path = d.pop("path", UNSET)

        refund_request_request_receipt = cls(
            body=body,
            signature=signature,
            trace_id=trace_id,
            path=path,
        )


        refund_request_request_receipt.additional_properties = d
        return refund_request_request_receipt

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
