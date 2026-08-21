from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OmsDrainResponse")



@_attrs_define
class OmsDrainResponse:
    """ 
        Attributes:
            scanned (int): Due orders claimed + attempted this run.
            pushed (int): Orders pushed (or already present) this run.
            failed (int): Orders whose push failed this run (retried later).
            batch (int): Max orders claimed per drain run.
     """

    scanned: int
    pushed: int
    failed: int
    batch: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        scanned = self.scanned

        pushed = self.pushed

        failed = self.failed

        batch = self.batch


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "scanned": scanned,
            "pushed": pushed,
            "failed": failed,
            "batch": batch,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scanned = d.pop("scanned")

        pushed = d.pop("pushed")

        failed = d.pop("failed")

        batch = d.pop("batch")

        oms_drain_response = cls(
            scanned=scanned,
            pushed=pushed,
            failed=failed,
            batch=batch,
        )


        oms_drain_response.additional_properties = d
        return oms_drain_response

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
