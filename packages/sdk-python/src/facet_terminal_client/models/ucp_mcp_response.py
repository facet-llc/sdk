from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ucp_mcp_response_jsonrpc import UcpMcpResponseJsonrpc
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ucp_mcp_response_error import UcpMcpResponseError





T = TypeVar("T", bound="UcpMcpResponse")



@_attrs_define
class UcpMcpResponse:
    """ A JSON-RPC 2.0 response from the UCP MCP catalog endpoint (POST /ucp/mcp). Carries `result` on success or `error` on
    a protocol failure.

        Attributes:
            jsonrpc (UcpMcpResponseJsonrpc | Unset): JSON-RPC version, always "2.0".
            id (Any | Unset): Echoes the request id; null for a parse error.
            result (Any | Unset): Present on success. tools/list -> { tools }; tools/call -> { content, structuredContent }
                (a tool failure is result.isError = true).
            error (UcpMcpResponseError | Unset): Present instead of result on a JSON-RPC protocol error.
     """

    jsonrpc: UcpMcpResponseJsonrpc | Unset = UNSET
    id: Any | Unset = UNSET
    result: Any | Unset = UNSET
    error: UcpMcpResponseError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ucp_mcp_response_error import UcpMcpResponseError
        jsonrpc: str | Unset = UNSET
        if not isinstance(self.jsonrpc, Unset):
            jsonrpc = self.jsonrpc.value


        id = self.id

        result = self.result

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if jsonrpc is not UNSET:
            field_dict["jsonrpc"] = jsonrpc
        if id is not UNSET:
            field_dict["id"] = id
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ucp_mcp_response_error import UcpMcpResponseError
        d = dict(src_dict)
        _jsonrpc = d.pop("jsonrpc", UNSET)
        jsonrpc: UcpMcpResponseJsonrpc | Unset
        if isinstance(_jsonrpc,  Unset):
            jsonrpc = UNSET
        else:
            jsonrpc = UcpMcpResponseJsonrpc(_jsonrpc)




        id = d.pop("id", UNSET)

        result = d.pop("result", UNSET)

        _error = d.pop("error", UNSET)
        error: UcpMcpResponseError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = UcpMcpResponseError.from_dict(_error)




        ucp_mcp_response = cls(
            jsonrpc=jsonrpc,
            id=id,
            result=result,
            error=error,
        )


        ucp_mcp_response.additional_properties = d
        return ucp_mcp_response

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
