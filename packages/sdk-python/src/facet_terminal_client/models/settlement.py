from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.settlement_state import SettlementState
from typing import cast






T = TypeVar("T", bound="Settlement")



@_attrs_define
class Settlement:
    """ 
        Attributes:
            settlement_id (str): The dispatch trace_id (journal primary key).
            site_id (str):
            merchant_id (None | str):
            rail_id (str):
            op (str):
            state (SettlementState):
            exchange_id (None | str):
            tx_hash (None | str):
            agent_aid (None | str):
            amount_atomic (None | str): Amount in the rail's smallest unit, stringified (USDC = 6 decimals).
            currency (None | str):
            error_code (None | str):
            created_at (str): ISO 8601.
            updated_at (str): ISO 8601.
     """

    settlement_id: str
    site_id: str
    merchant_id: None | str
    rail_id: str
    op: str
    state: SettlementState
    exchange_id: None | str
    tx_hash: None | str
    agent_aid: None | str
    amount_atomic: None | str
    currency: None | str
    error_code: None | str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        settlement_id = self.settlement_id

        site_id = self.site_id

        merchant_id: None | str
        merchant_id = self.merchant_id

        rail_id = self.rail_id

        op = self.op

        state = self.state.value

        exchange_id: None | str
        exchange_id = self.exchange_id

        tx_hash: None | str
        tx_hash = self.tx_hash

        agent_aid: None | str
        agent_aid = self.agent_aid

        amount_atomic: None | str
        amount_atomic = self.amount_atomic

        currency: None | str
        currency = self.currency

        error_code: None | str
        error_code = self.error_code

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "settlement_id": settlement_id,
            "site_id": site_id,
            "merchant_id": merchant_id,
            "rail_id": rail_id,
            "op": op,
            "state": state,
            "exchange_id": exchange_id,
            "tx_hash": tx_hash,
            "agent_aid": agent_aid,
            "amount_atomic": amount_atomic,
            "currency": currency,
            "error_code": error_code,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        settlement_id = d.pop("settlement_id")

        site_id = d.pop("site_id")

        def _parse_merchant_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        merchant_id = _parse_merchant_id(d.pop("merchant_id"))


        rail_id = d.pop("rail_id")

        op = d.pop("op")

        state = SettlementState(d.pop("state"))




        def _parse_exchange_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        exchange_id = _parse_exchange_id(d.pop("exchange_id"))


        def _parse_tx_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tx_hash = _parse_tx_hash(d.pop("tx_hash"))


        def _parse_agent_aid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_aid = _parse_agent_aid(d.pop("agent_aid"))


        def _parse_amount_atomic(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        amount_atomic = _parse_amount_atomic(d.pop("amount_atomic"))


        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))


        def _parse_error_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_code = _parse_error_code(d.pop("error_code"))


        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        settlement = cls(
            settlement_id=settlement_id,
            site_id=site_id,
            merchant_id=merchant_id,
            rail_id=rail_id,
            op=op,
            state=state,
            exchange_id=exchange_id,
            tx_hash=tx_hash,
            agent_aid=agent_aid,
            amount_atomic=amount_atomic,
            currency=currency,
            error_code=error_code,
            created_at=created_at,
            updated_at=updated_at,
        )


        settlement.additional_properties = d
        return settlement

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
