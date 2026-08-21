from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.settlement_state import SettlementState
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListSettlementsRequest")



@_attrs_define
class ListSettlementsRequest:
    """ 
        Attributes:
            site_id (str): UUID. The caller must be a viewer+ member of this site.
            state (SettlementState | Unset):
            limit (int | Unset):
            cursor (str | Unset):
     """

    site_id: str
    state: SettlementState | Unset = UNSET
    limit: int | Unset = UNSET
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value


        limit = self.limit

        cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
        })
        if state is not UNSET:
            field_dict["state"] = state
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        _state = d.pop("state", UNSET)
        state: SettlementState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = SettlementState(_state)




        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        list_settlements_request = cls(
            site_id=site_id,
            state=state,
            limit=limit,
            cursor=cursor,
        )


        list_settlements_request.additional_properties = d
        return list_settlements_request

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
