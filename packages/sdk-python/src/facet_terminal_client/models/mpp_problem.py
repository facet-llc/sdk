from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MppProblem")



@_attrs_define
class MppProblem:
    """ RFC 9457 problem details for an MPP failure. ALWAYS accompanied by a fresh `WWW-Authenticate: Payment ...`
    challenge, because an agent whose credential was rejected cannot retry otherwise: the challenge it was holding may
    be exactly what was wrong with it.

        Attributes:
            type_ (str): Stable problem-type URI an agent can branch on.
            title (str):
            status (int): Always 402.
            detail (str):
            retryable (bool): Whether signing a new credential against the FRESH challenge on this response can succeed.
                False means something other than the credential must change (a different order, a different chain), so a blind
                retry loop is pointless.
     """

    type_: str
    title: str
    status: int
    detail: str
    retryable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        detail = self.detail

        retryable = self.retryable


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "title": title,
            "status": status,
            "detail": detail,
            "retryable": retryable,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        detail = d.pop("detail")

        retryable = d.pop("retryable")

        mpp_problem = cls(
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            retryable=retryable,
        )


        mpp_problem.additional_properties = d
        return mpp_problem

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
