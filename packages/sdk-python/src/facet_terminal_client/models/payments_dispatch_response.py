from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.dispatch_agent_summary import DispatchAgentSummary





T = TypeVar("T", bound="PaymentsDispatchResponse")



@_attrs_define
class PaymentsDispatchResponse:
    """ 
        Attributes:
            rail_id (str): Stable rail identifier — namespaces match /v1/terms.settlement_rails (e.g. 'coin/usdc-base',
                'card/stripe', 'voucher/skyfire').
            origination_id (str): Verifier id that authenticated the agent's attestation (e.g. 'issuer/direct').
            agent (DispatchAgentSummary):
            result (Any): Adapter's raw result — shape varies per op (VerifyAuthorityOk, CaptureOk, etc.).
     """

    rail_id: str
    origination_id: str
    agent: DispatchAgentSummary
    result: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dispatch_agent_summary import DispatchAgentSummary
        rail_id = self.rail_id

        origination_id = self.origination_id

        agent = self.agent.to_dict()

        result = self.result


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rail_id": rail_id,
            "origination_id": origination_id,
            "agent": agent,
            "result": result,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dispatch_agent_summary import DispatchAgentSummary
        d = dict(src_dict)
        rail_id = d.pop("rail_id")

        origination_id = d.pop("origination_id")

        agent = DispatchAgentSummary.from_dict(d.pop("agent"))




        result = d.pop("result")

        payments_dispatch_response = cls(
            rail_id=rail_id,
            origination_id=origination_id,
            agent=agent,
            result=result,
        )


        payments_dispatch_response.additional_properties = d
        return payments_dispatch_response

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
