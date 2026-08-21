from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ucp_mcp_request_jsonrpc import UcpMcpRequestJsonrpc
from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpMcpRequest")



@_attrs_define
class UcpMcpRequest:
    """ A JSON-RPC 2.0 request for the UCP MCP catalog endpoint (POST /ucp/mcp). The dev.ucp.shopping tool schemas
    (search_catalog, lookup_catalog, get_product) are defined by the UCP MCP service schema referenced in the /.well-
    known/ucp profile.

        Attributes:
            jsonrpc (UcpMcpRequestJsonrpc): JSON-RPC version, always "2.0".
            method (str): MCP method, e.g. initialize, tools/list, tools/call.
            id (Any | Unset): Request id (string or number); absent for notifications.
            params (Any | Unset): Method params (e.g. { name, arguments } for tools/call).
     """

    jsonrpc: UcpMcpRequestJsonrpc
    method: str
    id: Any | Unset = UNSET
    params: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        jsonrpc = self.jsonrpc.value

        method = self.method

        id = self.id

        params = self.params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "jsonrpc": jsonrpc,
            "method": method,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jsonrpc = UcpMcpRequestJsonrpc(d.pop("jsonrpc"))




        method = d.pop("method")

        id = d.pop("id", UNSET)

        params = d.pop("params", UNSET)

        ucp_mcp_request = cls(
            jsonrpc=jsonrpc,
            method=method,
            id=id,
            params=params,
        )


        ucp_mcp_request.additional_properties = d
        return ucp_mcp_request

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
