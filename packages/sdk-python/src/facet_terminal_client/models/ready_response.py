from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ready_response_status import ReadyResponseStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.ready_response_checks import ReadyResponseChecks





T = TypeVar("T", bound="ReadyResponse")



@_attrs_define
class ReadyResponse:
    """ 
        Attributes:
            status (ReadyResponseStatus): 'ready' (HTTP 200) when every critical dependency check is 'ok'; 'not_ready' (HTTP
                503) when any is 'fail'.
            timestamp (str): ISO 8601 timestamp the Terminal generated the response.
            checks (ReadyResponseChecks): Per-dependency reachability outcomes. `supabase` is always present; further
                critical deps may appear as they are wired.
     """

    status: ReadyResponseStatus
    timestamp: str
    checks: ReadyResponseChecks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ready_response_checks import ReadyResponseChecks
        status = self.status.value

        timestamp = self.timestamp

        checks = self.checks.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "timestamp": timestamp,
            "checks": checks,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ready_response_checks import ReadyResponseChecks
        d = dict(src_dict)
        status = ReadyResponseStatus(d.pop("status"))




        timestamp = d.pop("timestamp")

        checks = ReadyResponseChecks.from_dict(d.pop("checks"))




        ready_response = cls(
            status=status,
            timestamp=timestamp,
            checks=checks,
        )


        ready_response.additional_properties = d
        return ready_response

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
