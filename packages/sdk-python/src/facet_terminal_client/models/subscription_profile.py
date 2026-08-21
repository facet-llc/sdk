from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subscription_status import SubscriptionStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.subscription_line_item import SubscriptionLineItem





T = TypeVar("T", bound="SubscriptionProfile")



@_attrs_define
class SubscriptionProfile:
    """ 
        Attributes:
            id (str):
            site_id (str):
            agent_aid (str):
            cadence_iso8601 (str):
            line_items_jsonb (list[SubscriptionLineItem]):
            status (SubscriptionStatus):
            paused_until (None | str):
            next_run_at (str):
            settlement_rail (None | str):
            currency (str):
            notes (None | str):
            created_at (str):
            updated_at (str):
            cancelled_at (None | str):
     """

    id: str
    site_id: str
    agent_aid: str
    cadence_iso8601: str
    line_items_jsonb: list[SubscriptionLineItem]
    status: SubscriptionStatus
    paused_until: None | str
    next_run_at: str
    settlement_rail: None | str
    currency: str
    notes: None | str
    created_at: str
    updated_at: str
    cancelled_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_line_item import SubscriptionLineItem
        id = self.id

        site_id = self.site_id

        agent_aid = self.agent_aid

        cadence_iso8601 = self.cadence_iso8601

        line_items_jsonb = []
        for line_items_jsonb_item_data in self.line_items_jsonb:
            line_items_jsonb_item = line_items_jsonb_item_data.to_dict()
            line_items_jsonb.append(line_items_jsonb_item)



        status = self.status.value

        paused_until: None | str
        paused_until = self.paused_until

        next_run_at = self.next_run_at

        settlement_rail: None | str
        settlement_rail = self.settlement_rail

        currency = self.currency

        notes: None | str
        notes = self.notes

        created_at = self.created_at

        updated_at = self.updated_at

        cancelled_at: None | str
        cancelled_at = self.cancelled_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "site_id": site_id,
            "agent_aid": agent_aid,
            "cadence_iso8601": cadence_iso8601,
            "line_items_jsonb": line_items_jsonb,
            "status": status,
            "paused_until": paused_until,
            "next_run_at": next_run_at,
            "settlement_rail": settlement_rail,
            "currency": currency,
            "notes": notes,
            "created_at": created_at,
            "updated_at": updated_at,
            "cancelled_at": cancelled_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_line_item import SubscriptionLineItem
        d = dict(src_dict)
        id = d.pop("id")

        site_id = d.pop("site_id")

        agent_aid = d.pop("agent_aid")

        cadence_iso8601 = d.pop("cadence_iso8601")

        line_items_jsonb = []
        _line_items_jsonb = d.pop("line_items_jsonb")
        for line_items_jsonb_item_data in (_line_items_jsonb):
            line_items_jsonb_item = SubscriptionLineItem.from_dict(line_items_jsonb_item_data)



            line_items_jsonb.append(line_items_jsonb_item)


        status = SubscriptionStatus(d.pop("status"))




        def _parse_paused_until(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        paused_until = _parse_paused_until(d.pop("paused_until"))


        next_run_at = d.pop("next_run_at")

        def _parse_settlement_rail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        settlement_rail = _parse_settlement_rail(d.pop("settlement_rail"))


        currency = d.pop("currency")

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))


        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_cancelled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at"))


        subscription_profile = cls(
            id=id,
            site_id=site_id,
            agent_aid=agent_aid,
            cadence_iso8601=cadence_iso8601,
            line_items_jsonb=line_items_jsonb,
            status=status,
            paused_until=paused_until,
            next_run_at=next_run_at,
            settlement_rail=settlement_rail,
            currency=currency,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
            cancelled_at=cancelled_at,
        )


        subscription_profile.additional_properties = d
        return subscription_profile

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
