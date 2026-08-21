from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.reconcile_settlement_result import ReconcileSettlementResult





T = TypeVar("T", bound="ReconcileSettlementsResponse")



@_attrs_define
class ReconcileSettlementsResponse:
    """ 
        Attributes:
            scanned (int): Stuck exchanges examined this pass.
            advanced (int): Re-read RELEASED on-chain and advanced to settled.
            skipped (int): Already terminal / not actionable.
            still_pending (int): Re-read but not yet RELEASED — left untouched for a later pass.
            results (list[ReconcileSettlementResult]):
     """

    scanned: int
    advanced: int
    skipped: int
    still_pending: int
    results: list[ReconcileSettlementResult]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reconcile_settlement_result import ReconcileSettlementResult
        scanned = self.scanned

        advanced = self.advanced

        skipped = self.skipped

        still_pending = self.still_pending

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "scanned": scanned,
            "advanced": advanced,
            "skipped": skipped,
            "still_pending": still_pending,
            "results": results,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reconcile_settlement_result import ReconcileSettlementResult
        d = dict(src_dict)
        scanned = d.pop("scanned")

        advanced = d.pop("advanced")

        skipped = d.pop("skipped")

        still_pending = d.pop("still_pending")

        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = ReconcileSettlementResult.from_dict(results_item_data)



            results.append(results_item)


        reconcile_settlements_response = cls(
            scanned=scanned,
            advanced=advanced,
            skipped=skipped,
            still_pending=still_pending,
            results=results,
        )


        reconcile_settlements_response.additional_properties = d
        return reconcile_settlements_response

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
