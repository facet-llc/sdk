from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_escrow_buyer_cancel_open_dispute_phase import OpenEscrowBuyerCancelOpenDisputePhase
from ..models.open_escrow_buyer_cancel_open_dispute_status import OpenEscrowBuyerCancelOpenDisputeStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.open_escrow_call import OpenEscrowCall





T = TypeVar("T", bound="OpenEscrowBuyerCancelOpenDispute")



@_attrs_define
class OpenEscrowBuyerCancelOpenDispute:
    """ 
        Attributes:
            field_status (OpenEscrowBuyerCancelOpenDisputeStatus):
            phase (OpenEscrowBuyerCancelOpenDisputePhase):
            escrow_id (str):
            disputed_amount_base_units (str): Full escrow amount in USDC base units, decimal string.
            evidence_hash (str):
            dispute_deadline (None | str): ISO 8601 on-chain dispute deadline, or null.
            open_dispute_calldata (OpenEscrowCall):
            note (str): Guidance to self-broadcast openDispute, then re-call once mined.
     """

    field_status: OpenEscrowBuyerCancelOpenDisputeStatus
    phase: OpenEscrowBuyerCancelOpenDisputePhase
    escrow_id: str
    disputed_amount_base_units: str
    evidence_hash: str
    dispute_deadline: None | str
    open_dispute_calldata: OpenEscrowCall
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_escrow_call import OpenEscrowCall
        field_status = self.field_status.value

        phase = self.phase.value

        escrow_id = self.escrow_id

        disputed_amount_base_units = self.disputed_amount_base_units

        evidence_hash = self.evidence_hash

        dispute_deadline: None | str
        dispute_deadline = self.dispute_deadline

        open_dispute_calldata = self.open_dispute_calldata.to_dict()

        note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "_status": field_status,
            "phase": phase,
            "escrowId": escrow_id,
            "disputedAmountBaseUnits": disputed_amount_base_units,
            "evidenceHash": evidence_hash,
            "dispute_deadline": dispute_deadline,
            "open_dispute_calldata": open_dispute_calldata,
            "note": note,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_escrow_call import OpenEscrowCall
        d = dict(src_dict)
        field_status = OpenEscrowBuyerCancelOpenDisputeStatus(d.pop("_status"))




        phase = OpenEscrowBuyerCancelOpenDisputePhase(d.pop("phase"))




        escrow_id = d.pop("escrowId")

        disputed_amount_base_units = d.pop("disputedAmountBaseUnits")

        evidence_hash = d.pop("evidenceHash")

        def _parse_dispute_deadline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dispute_deadline = _parse_dispute_deadline(d.pop("dispute_deadline"))


        open_dispute_calldata = OpenEscrowCall.from_dict(d.pop("open_dispute_calldata"))




        note = d.pop("note")

        open_escrow_buyer_cancel_open_dispute = cls(
            field_status=field_status,
            phase=phase,
            escrow_id=escrow_id,
            disputed_amount_base_units=disputed_amount_base_units,
            evidence_hash=evidence_hash,
            dispute_deadline=dispute_deadline,
            open_dispute_calldata=open_dispute_calldata,
            note=note,
        )


        open_escrow_buyer_cancel_open_dispute.additional_properties = d
        return open_escrow_buyer_cancel_open_dispute

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
