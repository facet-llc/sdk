from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.discover_product_result import DiscoverProductResult





T = TypeVar("T", bound="DiscoverProductsResponse")



@_attrs_define
class DiscoverProductsResponse:
    """ 
        Attributes:
            results (list[DiscoverProductResult]):
            total_estimate (int):
            next_offset (int | None):
     """

    results: list[DiscoverProductResult]
    total_estimate: int
    next_offset: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.discover_product_result import DiscoverProductResult
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)



        total_estimate = self.total_estimate

        next_offset: int | None
        next_offset = self.next_offset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "results": results,
            "total_estimate": total_estimate,
            "next_offset": next_offset,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discover_product_result import DiscoverProductResult
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = DiscoverProductResult.from_dict(results_item_data)



            results.append(results_item)


        total_estimate = d.pop("total_estimate")

        def _parse_next_offset(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_offset = _parse_next_offset(d.pop("next_offset"))


        discover_products_response = cls(
            results=results,
            total_estimate=total_estimate,
            next_offset=next_offset,
        )


        discover_products_response.additional_properties = d
        return discover_products_response

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
