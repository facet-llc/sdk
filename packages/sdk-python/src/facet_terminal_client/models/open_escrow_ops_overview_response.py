from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_escrow_ops_overview_response_status import OpenEscrowOpsOverviewResponseStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.open_escrow_dispute import OpenEscrowDispute
  from ..models.open_escrow_ops_overview_response_arbiter import OpenEscrowOpsOverviewResponseArbiter
  from ..models.open_escrow_ops_overview_response_counts import OpenEscrowOpsOverviewResponseCounts
  from ..models.open_escrow_ops_overview_response_solvency import OpenEscrowOpsOverviewResponseSolvency





T = TypeVar("T", bound="OpenEscrowOpsOverviewResponse")



@_attrs_define
class OpenEscrowOpsOverviewResponse:
    """ 
        Attributes:
            field_status (OpenEscrowOpsOverviewResponseStatus):
            generated_at (str): ISO 8601 timestamp the census was generated.
            chain_id (int | None): EVM chain id; null when the rail is unconfigured.
            escrow_contract (None | str): OpenEscrow contract address; null when unconfigured.
            arbiter (OpenEscrowOpsOverviewResponseArbiter):
            solvency (OpenEscrowOpsOverviewResponseSolvency):
            counts (OpenEscrowOpsOverviewResponseCounts):
            disputes (list[OpenEscrowDispute]):
     """

    field_status: OpenEscrowOpsOverviewResponseStatus
    generated_at: str
    chain_id: int | None
    escrow_contract: None | str
    arbiter: OpenEscrowOpsOverviewResponseArbiter
    solvency: OpenEscrowOpsOverviewResponseSolvency
    counts: OpenEscrowOpsOverviewResponseCounts
    disputes: list[OpenEscrowDispute]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_escrow_dispute import OpenEscrowDispute
        from ..models.open_escrow_ops_overview_response_arbiter import OpenEscrowOpsOverviewResponseArbiter
        from ..models.open_escrow_ops_overview_response_counts import OpenEscrowOpsOverviewResponseCounts
        from ..models.open_escrow_ops_overview_response_solvency import OpenEscrowOpsOverviewResponseSolvency
        field_status = self.field_status.value

        generated_at = self.generated_at

        chain_id: int | None
        chain_id = self.chain_id

        escrow_contract: None | str
        escrow_contract = self.escrow_contract

        arbiter = self.arbiter.to_dict()

        solvency = self.solvency.to_dict()

        counts = self.counts.to_dict()

        disputes = []
        for disputes_item_data in self.disputes:
            disputes_item = disputes_item_data.to_dict()
            disputes.append(disputes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "_status": field_status,
            "generatedAt": generated_at,
            "chainId": chain_id,
            "escrowContract": escrow_contract,
            "arbiter": arbiter,
            "solvency": solvency,
            "counts": counts,
            "disputes": disputes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_escrow_dispute import OpenEscrowDispute
        from ..models.open_escrow_ops_overview_response_arbiter import OpenEscrowOpsOverviewResponseArbiter
        from ..models.open_escrow_ops_overview_response_counts import OpenEscrowOpsOverviewResponseCounts
        from ..models.open_escrow_ops_overview_response_solvency import OpenEscrowOpsOverviewResponseSolvency
        d = dict(src_dict)
        field_status = OpenEscrowOpsOverviewResponseStatus(d.pop("_status"))




        generated_at = d.pop("generatedAt")

        def _parse_chain_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        chain_id = _parse_chain_id(d.pop("chainId"))


        def _parse_escrow_contract(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        escrow_contract = _parse_escrow_contract(d.pop("escrowContract"))


        arbiter = OpenEscrowOpsOverviewResponseArbiter.from_dict(d.pop("arbiter"))




        solvency = OpenEscrowOpsOverviewResponseSolvency.from_dict(d.pop("solvency"))




        counts = OpenEscrowOpsOverviewResponseCounts.from_dict(d.pop("counts"))




        disputes = []
        _disputes = d.pop("disputes")
        for disputes_item_data in (_disputes):
            disputes_item = OpenEscrowDispute.from_dict(disputes_item_data)



            disputes.append(disputes_item)


        open_escrow_ops_overview_response = cls(
            field_status=field_status,
            generated_at=generated_at,
            chain_id=chain_id,
            escrow_contract=escrow_contract,
            arbiter=arbiter,
            solvency=solvency,
            counts=counts,
            disputes=disputes,
        )


        open_escrow_ops_overview_response.additional_properties = d
        return open_escrow_ops_overview_response

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
