from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ready_response_checks_supabase import ReadyResponseChecksSupabase






T = TypeVar("T", bound="ReadyResponseChecks")



@_attrs_define
class ReadyResponseChecks:
    """ Per-dependency reachability outcomes. `supabase` is always present; further critical deps may appear as they are
    wired.

        Attributes:
            supabase (ReadyResponseChecksSupabase): Supabase reachability — a bounded, RLS-bypassing read against `sites`.
     """

    supabase: ReadyResponseChecksSupabase
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        supabase = self.supabase.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "supabase": supabase,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supabase = ReadyResponseChecksSupabase(d.pop("supabase"))




        ready_response_checks = cls(
            supabase=supabase,
        )


        ready_response_checks.additional_properties = d
        return ready_response_checks

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
