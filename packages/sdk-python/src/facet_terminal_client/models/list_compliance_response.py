from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_override import ComplianceOverride





T = TypeVar("T", bound="ListComplianceResponse")



@_attrs_define
class ListComplianceResponse:
    """ 
        Attributes:
            overrides (list[ComplianceOverride]):
            next_cursor (None | str):
     """

    overrides: list[ComplianceOverride]
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_override import ComplianceOverride
        overrides = []
        for overrides_item_data in self.overrides:
            overrides_item = overrides_item_data.to_dict()
            overrides.append(overrides_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "overrides": overrides,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_override import ComplianceOverride
        d = dict(src_dict)
        overrides = []
        _overrides = d.pop("overrides")
        for overrides_item_data in (_overrides):
            overrides_item = ComplianceOverride.from_dict(overrides_item_data)



            overrides.append(overrides_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        list_compliance_response = cls(
            overrides=overrides,
            next_cursor=next_cursor,
        )


        list_compliance_response.additional_properties = d
        return list_compliance_response

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
