from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="VersionResponse")



@_attrs_define
class VersionResponse:
    """ 
        Attributes:
            facet (str): Facet protocol version (e.g. '0.2.0').
            mcp_protocol_version (str): MCP protocol revision Terminal speaks.
            terminal (str): Terminal build identifier.
     """

    facet: str
    mcp_protocol_version: str
    terminal: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        facet = self.facet

        mcp_protocol_version = self.mcp_protocol_version

        terminal = self.terminal


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "facet": facet,
            "mcp_protocol_version": mcp_protocol_version,
            "terminal": terminal,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        facet = d.pop("facet")

        mcp_protocol_version = d.pop("mcp_protocol_version")

        terminal = d.pop("terminal")

        version_response = cls(
            facet=facet,
            mcp_protocol_version=mcp_protocol_version,
            terminal=terminal,
        )


        version_response.additional_properties = d
        return version_response

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
