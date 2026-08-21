from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sku_kind import SkuKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pricing_schedule import PricingSchedule
  from ..models.search_product_result_pack import SearchProductResultPack





T = TypeVar("T", bound="SearchProductResult")



@_attrs_define
class SearchProductResult:
    """ 
        Attributes:
            id (str):
            name (str):
            category (str):
            tags (list[str]):
            pricing (PricingSchedule):
            pack (SearchProductResultPack):
            in_stock (bool):
            kind (SkuKind | Unset): What kind of SKU — only `physical` requires a ship-to destination.
     """

    id: str
    name: str
    category: str
    tags: list[str]
    pricing: PricingSchedule
    pack: SearchProductResultPack
    in_stock: bool
    kind: SkuKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pricing_schedule import PricingSchedule
        from ..models.search_product_result_pack import SearchProductResultPack
        id = self.id

        name = self.name

        category = self.category

        tags = self.tags



        pricing = self.pricing.to_dict()

        pack = self.pack.to_dict()

        in_stock = self.in_stock

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "category": category,
            "tags": tags,
            "pricing": pricing,
            "pack": pack,
            "in_stock": in_stock,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_schedule import PricingSchedule
        from ..models.search_product_result_pack import SearchProductResultPack
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        category = d.pop("category")

        tags = cast(list[str], d.pop("tags"))


        pricing = PricingSchedule.from_dict(d.pop("pricing"))




        pack = SearchProductResultPack.from_dict(d.pop("pack"))




        in_stock = d.pop("in_stock")

        _kind = d.pop("kind", UNSET)
        kind: SkuKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = SkuKind(_kind)




        search_product_result = cls(
            id=id,
            name=name,
            category=category,
            tags=tags,
            pricing=pricing,
            pack=pack,
            in_stock=in_stock,
            kind=kind,
        )


        search_product_result.additional_properties = d
        return search_product_result

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
