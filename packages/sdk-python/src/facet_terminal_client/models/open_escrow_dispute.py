from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="OpenEscrowDispute")



@_attrs_define
class OpenEscrowDispute:
    """ 
        Attributes:
            escrow_id (str): 32-byte 0x escrow id (settlement id).
            site_id (None | str):
            site_handle (None | str): Always null in the overview (not enriched).
            order_id (None | str):
            payer (str): Stored on-chain payer (buyer) address.
            merchant (str): Stored on-chain merchant address.
            amount_minor (int): Escrow amount in USD cents.
            disputed_amount_minor (int | None): Always null (not read from the snapshot).
            evidence_hash (None | str): Always null in the overview.
            dispute_opened_at (None | str): ISO 8601 dispute-opened timestamp, or null.
            dispute_deadline (None | str): ISO 8601 dispute deadline, or null.
            chain_id (int): EVM chain id of the OpenEscrow contract.
            escrow_contract (str): OpenEscrow contract address.
     """

    escrow_id: str
    site_id: None | str
    site_handle: None | str
    order_id: None | str
    payer: str
    merchant: str
    amount_minor: int
    disputed_amount_minor: int | None
    evidence_hash: None | str
    dispute_opened_at: None | str
    dispute_deadline: None | str
    chain_id: int
    escrow_contract: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        escrow_id = self.escrow_id

        site_id: None | str
        site_id = self.site_id

        site_handle: None | str
        site_handle = self.site_handle

        order_id: None | str
        order_id = self.order_id

        payer = self.payer

        merchant = self.merchant

        amount_minor = self.amount_minor

        disputed_amount_minor: int | None
        disputed_amount_minor = self.disputed_amount_minor

        evidence_hash: None | str
        evidence_hash = self.evidence_hash

        dispute_opened_at: None | str
        dispute_opened_at = self.dispute_opened_at

        dispute_deadline: None | str
        dispute_deadline = self.dispute_deadline

        chain_id = self.chain_id

        escrow_contract = self.escrow_contract


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "escrowId": escrow_id,
            "siteId": site_id,
            "siteHandle": site_handle,
            "orderId": order_id,
            "payer": payer,
            "merchant": merchant,
            "amountMinor": amount_minor,
            "disputedAmountMinor": disputed_amount_minor,
            "evidenceHash": evidence_hash,
            "disputeOpenedAt": dispute_opened_at,
            "disputeDeadline": dispute_deadline,
            "chainId": chain_id,
            "escrowContract": escrow_contract,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escrow_id = d.pop("escrowId")

        def _parse_site_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        site_id = _parse_site_id(d.pop("siteId"))


        def _parse_site_handle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        site_handle = _parse_site_handle(d.pop("siteHandle"))


        def _parse_order_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        order_id = _parse_order_id(d.pop("orderId"))


        payer = d.pop("payer")

        merchant = d.pop("merchant")

        amount_minor = d.pop("amountMinor")

        def _parse_disputed_amount_minor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        disputed_amount_minor = _parse_disputed_amount_minor(d.pop("disputedAmountMinor"))


        def _parse_evidence_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        evidence_hash = _parse_evidence_hash(d.pop("evidenceHash"))


        def _parse_dispute_opened_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dispute_opened_at = _parse_dispute_opened_at(d.pop("disputeOpenedAt"))


        def _parse_dispute_deadline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dispute_deadline = _parse_dispute_deadline(d.pop("disputeDeadline"))


        chain_id = d.pop("chainId")

        escrow_contract = d.pop("escrowContract")

        open_escrow_dispute = cls(
            escrow_id=escrow_id,
            site_id=site_id,
            site_handle=site_handle,
            order_id=order_id,
            payer=payer,
            merchant=merchant,
            amount_minor=amount_minor,
            disputed_amount_minor=disputed_amount_minor,
            evidence_hash=evidence_hash,
            dispute_opened_at=dispute_opened_at,
            dispute_deadline=dispute_deadline,
            chain_id=chain_id,
            escrow_contract=escrow_contract,
        )


        open_escrow_dispute.additional_properties = d
        return open_escrow_dispute

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
