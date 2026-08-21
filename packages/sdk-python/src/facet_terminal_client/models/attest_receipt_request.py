from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AttestReceiptRequest")



@_attrs_define
class AttestReceiptRequest:
    """ 
        Attributes:
            this_hash (str):
            jws (str): Compact JWS, alg EdDSA, typ facet-attestation+jws.
     """

    this_hash: str
    jws: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        this_hash = self.this_hash

        jws = self.jws


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "this_hash": this_hash,
            "jws": jws,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        this_hash = d.pop("this_hash")

        jws = d.pop("jws")

        attest_receipt_request = cls(
            this_hash=this_hash,
            jws=jws,
        )


        attest_receipt_request.additional_properties = d
        return attest_receipt_request

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
