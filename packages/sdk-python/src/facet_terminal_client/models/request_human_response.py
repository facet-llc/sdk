from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.escalation_status import EscalationStatus
from typing import cast






T = TypeVar("T", bound="RequestHumanResponse")



@_attrs_define
class RequestHumanResponse:
    """ 
        Attributes:
            ticket_id (str):
            status (EscalationStatus):
            reason (str):
            sla_hours (float):
            created_at (str):
            resolved_at (None | str):
     """

    ticket_id: str
    status: EscalationStatus
    reason: str
    sla_hours: float
    created_at: str
    resolved_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ticket_id = self.ticket_id

        status = self.status.value

        reason = self.reason

        sla_hours = self.sla_hours

        created_at = self.created_at

        resolved_at: None | str
        resolved_at = self.resolved_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ticket_id": ticket_id,
            "status": status,
            "reason": reason,
            "sla_hours": sla_hours,
            "created_at": created_at,
            "resolved_at": resolved_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticket_id = d.pop("ticket_id")

        status = EscalationStatus(d.pop("status"))




        reason = d.pop("reason")

        sla_hours = d.pop("sla_hours")

        created_at = d.pop("created_at")

        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))


        request_human_response = cls(
            ticket_id=ticket_id,
            status=status,
            reason=reason,
            sla_hours=sla_hours,
            created_at=created_at,
            resolved_at=resolved_at,
        )


        request_human_response.additional_properties = d
        return request_human_response

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
