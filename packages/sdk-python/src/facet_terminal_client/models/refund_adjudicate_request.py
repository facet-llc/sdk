from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RefundAdjudicateRequest")



@_attrs_define
class RefundAdjudicateRequest:
    """ Internal: a neutral Facet operator rules on an ESCALATED dispute. Operator-authed (a shared adjudicator secret),
    NEITHER the merchant NOR the agent. Money-inert.

        Attributes:
            refund_id (str):
            ruling (str): 'uphold_buyer' or 'uphold_merchant'.
            rationale (None | str | Unset): Optional operator rationale (max 2000 chars).
     """

    refund_id: str
    ruling: str
    rationale: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        refund_id = self.refund_id

        ruling = self.ruling

        rationale: None | str | Unset
        if isinstance(self.rationale, Unset):
            rationale = UNSET
        else:
            rationale = self.rationale


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refund_id": refund_id,
            "ruling": ruling,
        })
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refund_id = d.pop("refund_id")

        ruling = d.pop("ruling")

        def _parse_rationale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rationale = _parse_rationale(d.pop("rationale", UNSET))


        refund_adjudicate_request = cls(
            refund_id=refund_id,
            ruling=ruling,
            rationale=rationale,
        )


        refund_adjudicate_request.additional_properties = d
        return refund_adjudicate_request

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
