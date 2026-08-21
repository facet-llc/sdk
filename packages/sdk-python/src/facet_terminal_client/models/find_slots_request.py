from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.date_range import DateRange





T = TypeVar("T", bound="FindSlotsRequest")



@_attrs_define
class FindSlotsRequest:
    """ 
        Attributes:
            resource_id (str):
            date_range (DateRange):
            party_size (int | Unset):
            limit (int | Unset):
     """

    resource_id: str
    date_range: DateRange
    party_size: int | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.date_range import DateRange
        resource_id = self.resource_id

        date_range = self.date_range.to_dict()

        party_size = self.party_size

        limit = self.limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "resource_id": resource_id,
            "date_range": date_range,
        })
        if party_size is not UNSET:
            field_dict["party_size"] = party_size
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_range import DateRange
        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        date_range = DateRange.from_dict(d.pop("date_range"))




        party_size = d.pop("party_size", UNSET)

        limit = d.pop("limit", UNSET)

        find_slots_request = cls(
            resource_id=resource_id,
            date_range=date_range,
            party_size=party_size,
            limit=limit,
        )


        find_slots_request.additional_properties = d
        return find_slots_request

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
