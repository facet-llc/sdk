from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UcpPerLineActionResult")



@_attrs_define
class UcpPerLineActionResult:
    """ One line's outcome in a PER-LINE redeem/cancel/dispute response.

        Attributes:
            exchange_id (str): This line's own on-chain Boson exchange id.
            line_index (int): 0-based index of this line in the cart's line_items.
            status (str): This line's outcome: "cancelled" / "redeemed" / "disputed" on success, "failed" or "rate_limited"
                otherwise. A failure on one line never unwinds a sibling.
            action (str | Unset): Dispute only: the action applied (raise/retract/escalate).
            refund_id (str | Unset): Cancel only: the rail refund id for this line.
            dispute_id (str | Unset): Dispute only: the rail dispute id for this line.
            tx_hash (str | Unset): Redeem only: the on-chain redeem tx hash for this line.
            error (str | Unset): Present when status is failed: the error code.
            rail_metadata (Any | Unset): On-chain evidence for this line: { escrow_state, tx_hash }.
     """

    exchange_id: str
    line_index: int
    status: str
    action: str | Unset = UNSET
    refund_id: str | Unset = UNSET
    dispute_id: str | Unset = UNSET
    tx_hash: str | Unset = UNSET
    error: str | Unset = UNSET
    rail_metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        line_index = self.line_index

        status = self.status

        action = self.action

        refund_id = self.refund_id

        dispute_id = self.dispute_id

        tx_hash = self.tx_hash

        error = self.error

        rail_metadata = self.rail_metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "exchange_id": exchange_id,
            "line_index": line_index,
            "status": status,
        })
        if action is not UNSET:
            field_dict["action"] = action
        if refund_id is not UNSET:
            field_dict["refund_id"] = refund_id
        if dispute_id is not UNSET:
            field_dict["dispute_id"] = dispute_id
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if error is not UNSET:
            field_dict["error"] = error
        if rail_metadata is not UNSET:
            field_dict["rail_metadata"] = rail_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id")

        line_index = d.pop("line_index")

        status = d.pop("status")

        action = d.pop("action", UNSET)

        refund_id = d.pop("refund_id", UNSET)

        dispute_id = d.pop("dispute_id", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        error = d.pop("error", UNSET)

        rail_metadata = d.pop("rail_metadata", UNSET)

        ucp_per_line_action_result = cls(
            exchange_id=exchange_id,
            line_index=line_index,
            status=status,
            action=action,
            refund_id=refund_id,
            dispute_id=dispute_id,
            tx_hash=tx_hash,
            error=error,
            rail_metadata=rail_metadata,
        )


        ucp_per_line_action_result.additional_properties = d
        return ucp_per_line_action_result

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
