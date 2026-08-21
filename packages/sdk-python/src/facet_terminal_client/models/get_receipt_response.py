from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.receipt_envelope_entry import ReceiptEnvelopeEntry





T = TypeVar("T", bound="GetReceiptResponse")



@_attrs_define
class GetReceiptResponse:
    """ 
        Attributes:
            receipt (ReceiptEnvelopeEntry):
     """

    receipt: ReceiptEnvelopeEntry
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.receipt_envelope_entry import ReceiptEnvelopeEntry
        receipt = self.receipt.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "receipt": receipt,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.receipt_envelope_entry import ReceiptEnvelopeEntry
        d = dict(src_dict)
        receipt = ReceiptEnvelopeEntry.from_dict(d.pop("receipt"))




        get_receipt_response = cls(
            receipt=receipt,
        )


        get_receipt_response.additional_properties = d
        return get_receipt_response

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
