from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reconcile_settlement_outcome import ReconcileSettlementOutcome






T = TypeVar("T", bound="ReconcileSettlementResult")



@_attrs_define
class ReconcileSettlementResult:
    """ 
        Attributes:
            exchange_id (str):
            outcome (ReconcileSettlementOutcome):
            reason (str): On-chain state, skip reason, or read error.
     """

    exchange_id: str
    outcome: ReconcileSettlementOutcome
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        outcome = self.outcome.value

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "exchange_id": exchange_id,
            "outcome": outcome,
            "reason": reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id")

        outcome = ReconcileSettlementOutcome(d.pop("outcome"))




        reason = d.pop("reason")

        reconcile_settlement_result = cls(
            exchange_id=exchange_id,
            outcome=outcome,
            reason=reason,
        )


        reconcile_settlement_result.additional_properties = d
        return reconcile_settlement_result

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
