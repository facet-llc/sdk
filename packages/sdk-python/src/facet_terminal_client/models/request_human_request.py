from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.request_human_request_context import RequestHumanRequestContext





T = TypeVar("T", bound="RequestHumanRequest")



@_attrs_define
class RequestHumanRequest:
    """ 
        Attributes:
            reason (str):
            context (RequestHumanRequestContext | Unset):
     """

    reason: str
    context: RequestHumanRequestContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.request_human_request_context import RequestHumanRequestContext
        reason = self.reason

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reason": reason,
        })
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_human_request_context import RequestHumanRequestContext
        d = dict(src_dict)
        reason = d.pop("reason")

        _context = d.pop("context", UNSET)
        context: RequestHumanRequestContext | Unset
        if isinstance(_context,  Unset):
            context = UNSET
        else:
            context = RequestHumanRequestContext.from_dict(_context)




        request_human_request = cls(
            reason=reason,
            context=context,
        )


        request_human_request.additional_properties = d
        return request_human_request

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
