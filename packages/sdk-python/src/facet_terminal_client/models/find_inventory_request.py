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
  from ..models.find_inventory_request_criteria import FindInventoryRequestCriteria





T = TypeVar("T", bound="FindInventoryRequest")



@_attrs_define
class FindInventoryRequest:
    """ 
        Attributes:
            resource_id (str):
            date_range (DateRange):
            qty (int | Unset):
            criteria (FindInventoryRequestCriteria | Unset):
            limit (int | Unset):
     """

    resource_id: str
    date_range: DateRange
    qty: int | Unset = UNSET
    criteria: FindInventoryRequestCriteria | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.date_range import DateRange
        from ..models.find_inventory_request_criteria import FindInventoryRequestCriteria
        resource_id = self.resource_id

        date_range = self.date_range.to_dict()

        qty = self.qty

        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        limit = self.limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "resource_id": resource_id,
            "date_range": date_range,
        })
        if qty is not UNSET:
            field_dict["qty"] = qty
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_range import DateRange
        from ..models.find_inventory_request_criteria import FindInventoryRequestCriteria
        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        date_range = DateRange.from_dict(d.pop("date_range"))




        qty = d.pop("qty", UNSET)

        _criteria = d.pop("criteria", UNSET)
        criteria: FindInventoryRequestCriteria | Unset
        if isinstance(_criteria,  Unset):
            criteria = UNSET
        else:
            criteria = FindInventoryRequestCriteria.from_dict(_criteria)




        limit = d.pop("limit", UNSET)

        find_inventory_request = cls(
            resource_id=resource_id,
            date_range=date_range,
            qty=qty,
            criteria=criteria,
            limit=limit,
        )


        find_inventory_request.additional_properties = d
        return find_inventory_request

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
