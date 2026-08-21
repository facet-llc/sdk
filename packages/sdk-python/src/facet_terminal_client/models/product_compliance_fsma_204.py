from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ProductComplianceFsma204")



@_attrs_define
class ProductComplianceFsma204:
    """ 
        Attributes:
            ftl_listed (bool):
            lot_code_format (None | str):
            kde_support (list[str]):
            cte_support (list[str]):
     """

    ftl_listed: bool
    lot_code_format: None | str
    kde_support: list[str]
    cte_support: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ftl_listed = self.ftl_listed

        lot_code_format: None | str
        lot_code_format = self.lot_code_format

        kde_support = self.kde_support



        cte_support = self.cte_support




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ftl_listed": ftl_listed,
            "lot_code_format": lot_code_format,
            "kde_support": kde_support,
            "cte_support": cte_support,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ftl_listed = d.pop("ftl_listed")

        def _parse_lot_code_format(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        lot_code_format = _parse_lot_code_format(d.pop("lot_code_format"))


        kde_support = cast(list[str], d.pop("kde_support"))


        cte_support = cast(list[str], d.pop("cte_support"))


        product_compliance_fsma_204 = cls(
            ftl_listed=ftl_listed,
            lot_code_format=lot_code_format,
            kde_support=kde_support,
            cte_support=cte_support,
        )


        product_compliance_fsma_204.additional_properties = d
        return product_compliance_fsma_204

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
