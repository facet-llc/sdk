from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ucp_per_line_action_result import UcpPerLineActionResult





T = TypeVar("T", bound="UcpCancelResponse")



@_attrs_define
class UcpCancelResponse:
    """ Acknowledges the on-chain cancel. The escrowed USDC returns to the buyer's protocol available-funds; the buyer
    cashes out to their wallet gaslessly with POST /ucp/v1/checkout-sessions/withdraw. In PER-LINE mode the top-level
    status summarizes the set and `lines` itemizes each line's outcome.

        Attributes:
            status (str | Unset): SINGLE mode: "cancelled". PER-LINE mode: "cancelled" (all), "partially_cancelled", or
                "cancel_failed".
            exchange_id (str | Unset): SINGLE mode: the cancelled exchange.
            refund_id (str | Unset): SINGLE mode: the rail refund id (the exchange id).
            rail_metadata (Any | Unset): On-chain evidence: { escrow_state, tx_hash }.
            cancelled_count (int | Unset): PER-LINE mode: how many selected lines cancelled.
            line_count (int | Unset): PER-LINE mode: how many lines were in the selection.
            lines (list[UcpPerLineActionResult] | Unset): PER-LINE mode: the per-line cancel outcome, one entry per selected
                line.
     """

    status: str | Unset = UNSET
    exchange_id: str | Unset = UNSET
    refund_id: str | Unset = UNSET
    rail_metadata: Any | Unset = UNSET
    cancelled_count: int | Unset = UNSET
    line_count: int | Unset = UNSET
    lines: list[UcpPerLineActionResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ucp_per_line_action_result import UcpPerLineActionResult
        status = self.status

        exchange_id = self.exchange_id

        refund_id = self.refund_id

        rail_metadata = self.rail_metadata

        cancelled_count = self.cancelled_count

        line_count = self.line_count

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if refund_id is not UNSET:
            field_dict["refund_id"] = refund_id
        if rail_metadata is not UNSET:
            field_dict["rail_metadata"] = rail_metadata
        if cancelled_count is not UNSET:
            field_dict["cancelled_count"] = cancelled_count
        if line_count is not UNSET:
            field_dict["line_count"] = line_count
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ucp_per_line_action_result import UcpPerLineActionResult
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        exchange_id = d.pop("exchange_id", UNSET)

        refund_id = d.pop("refund_id", UNSET)

        rail_metadata = d.pop("rail_metadata", UNSET)

        cancelled_count = d.pop("cancelled_count", UNSET)

        line_count = d.pop("line_count", UNSET)

        _lines = d.pop("lines", UNSET)
        lines: list[UcpPerLineActionResult] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = UcpPerLineActionResult.from_dict(lines_item_data)



                lines.append(lines_item)


        ucp_cancel_response = cls(
            status=status,
            exchange_id=exchange_id,
            refund_id=refund_id,
            rail_metadata=rail_metadata,
            cancelled_count=cancelled_count,
            line_count=line_count,
            lines=lines,
        )


        ucp_cancel_response.additional_properties = d
        return ucp_cancel_response

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
