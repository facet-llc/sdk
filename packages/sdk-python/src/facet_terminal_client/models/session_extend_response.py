from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SessionExtendResponse")



@_attrs_define
class SessionExtendResponse:
    """ 
        Attributes:
            session_id (str):
            aid (str):
            apd (None | str):
            scopes (list[str]):
            expires_at (str):
     """

    session_id: str
    aid: str
    apd: None | str
    scopes: list[str]
    expires_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        aid = self.aid

        apd: None | str
        apd = self.apd

        scopes = self.scopes



        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "session_id": session_id,
            "aid": aid,
            "apd": apd,
            "scopes": scopes,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("session_id")

        aid = d.pop("aid")

        def _parse_apd(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        apd = _parse_apd(d.pop("apd"))


        scopes = cast(list[str], d.pop("scopes"))


        expires_at = d.pop("expires_at")

        session_extend_response = cls(
            session_id=session_id,
            aid=aid,
            apd=apd,
            scopes=scopes,
            expires_at=expires_at,
        )


        session_extend_response.additional_properties = d
        return session_extend_response

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
