from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.payments_route_request_authority import PaymentsRouteRequestAuthority





T = TypeVar("T", bound="PaymentsRouteRequest")



@_attrs_define
class PaymentsRouteRequest:
    """ 
        Attributes:
            authority (PaymentsRouteRequestAuthority | Unset):
     """

    authority: PaymentsRouteRequestAuthority | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.payments_route_request_authority import PaymentsRouteRequestAuthority
        authority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authority, Unset):
            authority = self.authority.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if authority is not UNSET:
            field_dict["authority"] = authority

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payments_route_request_authority import PaymentsRouteRequestAuthority
        d = dict(src_dict)
        _authority = d.pop("authority", UNSET)
        authority: PaymentsRouteRequestAuthority | Unset
        if isinstance(_authority,  Unset):
            authority = UNSET
        else:
            authority = PaymentsRouteRequestAuthority.from_dict(_authority)




        payments_route_request = cls(
            authority=authority,
        )


        payments_route_request.additional_properties = d
        return payments_route_request

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
