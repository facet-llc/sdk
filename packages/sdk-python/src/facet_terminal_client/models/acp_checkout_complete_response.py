from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AcpCheckoutCompleteResponse")



@_attrs_define
class AcpCheckoutCompleteResponse:
    """ An ACP checkout completion mapped from a settled Terminal order. The Stripe charge id (or PaymentIntent id when no
    charge id is available) is the settlement_id surfaced by the dispatcher's CaptureOk envelope.

        Attributes:
            id (str | Unset): The checkout session id.
            status (str | Unset): Completion status, "completed" on success.
            order (Any | Unset): The settled order: { id, checkout_session_id, permalink_url }.
     """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    order: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        order = self.order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        order = d.pop("order", UNSET)

        acp_checkout_complete_response = cls(
            id=id,
            status=status,
            order=order,
        )


        acp_checkout_complete_response.additional_properties = d
        return acp_checkout_complete_response

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
