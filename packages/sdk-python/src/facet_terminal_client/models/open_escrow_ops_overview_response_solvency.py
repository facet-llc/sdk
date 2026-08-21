from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="OpenEscrowOpsOverviewResponseSolvency")



@_attrs_define
class OpenEscrowOpsOverviewResponseSolvency:
    """ 
        Attributes:
            total_escrowed_minor (int): Sum of funded + disputed escrow amounts, in USD cents.
            total_withdrawable_minor (int): Always 0 (reserved).
            contract_balance_minor (int | None): On-chain contract balance in cents; always null (not read).
     """

    total_escrowed_minor: int
    total_withdrawable_minor: int
    contract_balance_minor: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_escrowed_minor = self.total_escrowed_minor

        total_withdrawable_minor = self.total_withdrawable_minor

        contract_balance_minor: int | None
        contract_balance_minor = self.contract_balance_minor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "totalEscrowedMinor": total_escrowed_minor,
            "totalWithdrawableMinor": total_withdrawable_minor,
            "contractBalanceMinor": contract_balance_minor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_escrowed_minor = d.pop("totalEscrowedMinor")

        total_withdrawable_minor = d.pop("totalWithdrawableMinor")

        def _parse_contract_balance_minor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        contract_balance_minor = _parse_contract_balance_minor(d.pop("contractBalanceMinor"))


        open_escrow_ops_overview_response_solvency = cls(
            total_escrowed_minor=total_escrowed_minor,
            total_withdrawable_minor=total_withdrawable_minor,
            contract_balance_minor=contract_balance_minor,
        )


        open_escrow_ops_overview_response_solvency.additional_properties = d
        return open_escrow_ops_overview_response_solvency

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
