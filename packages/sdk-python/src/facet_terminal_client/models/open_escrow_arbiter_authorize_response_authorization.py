from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.open_escrow_call import OpenEscrowCall





T = TypeVar("T", bound="OpenEscrowArbiterAuthorizeResponseAuthorization")



@_attrs_define
class OpenEscrowArbiterAuthorizeResponseAuthorization:
    """ 
        Attributes:
            escrow_id (str):
            refund_amount_minor (int): Capped refund in USD cents.
            refund_amount_base_units (str): Capped refund in USDC base units (6dp), decimal string.
            evidence_hash (str):
            nonce (str): Single-use nonce, decimal string.
            deadline (str): Unix deadline seconds, decimal string.
            arbiter_address (str):
            arbiter_sig (str): EIP-712 RefundAuthorization signature.
            resolve_dispute_call (OpenEscrowCall):
     """

    escrow_id: str
    refund_amount_minor: int
    refund_amount_base_units: str
    evidence_hash: str
    nonce: str
    deadline: str
    arbiter_address: str
    arbiter_sig: str
    resolve_dispute_call: OpenEscrowCall
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_escrow_call import OpenEscrowCall
        escrow_id = self.escrow_id

        refund_amount_minor = self.refund_amount_minor

        refund_amount_base_units = self.refund_amount_base_units

        evidence_hash = self.evidence_hash

        nonce = self.nonce

        deadline = self.deadline

        arbiter_address = self.arbiter_address

        arbiter_sig = self.arbiter_sig

        resolve_dispute_call = self.resolve_dispute_call.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "escrowId": escrow_id,
            "refundAmountMinor": refund_amount_minor,
            "refundAmountBaseUnits": refund_amount_base_units,
            "evidenceHash": evidence_hash,
            "nonce": nonce,
            "deadline": deadline,
            "arbiterAddress": arbiter_address,
            "arbiterSig": arbiter_sig,
            "resolveDisputeCall": resolve_dispute_call,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_escrow_call import OpenEscrowCall
        d = dict(src_dict)
        escrow_id = d.pop("escrowId")

        refund_amount_minor = d.pop("refundAmountMinor")

        refund_amount_base_units = d.pop("refundAmountBaseUnits")

        evidence_hash = d.pop("evidenceHash")

        nonce = d.pop("nonce")

        deadline = d.pop("deadline")

        arbiter_address = d.pop("arbiterAddress")

        arbiter_sig = d.pop("arbiterSig")

        resolve_dispute_call = OpenEscrowCall.from_dict(d.pop("resolveDisputeCall"))




        open_escrow_arbiter_authorize_response_authorization = cls(
            escrow_id=escrow_id,
            refund_amount_minor=refund_amount_minor,
            refund_amount_base_units=refund_amount_base_units,
            evidence_hash=evidence_hash,
            nonce=nonce,
            deadline=deadline,
            arbiter_address=arbiter_address,
            arbiter_sig=arbiter_sig,
            resolve_dispute_call=resolve_dispute_call,
        )


        open_escrow_arbiter_authorize_response_authorization.additional_properties = d
        return open_escrow_arbiter_authorize_response_authorization

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
