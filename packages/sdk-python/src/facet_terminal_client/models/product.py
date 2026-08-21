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
  from ..models.product_pack import ProductPack





T = TypeVar("T", bound="Product")



@_attrs_define
class Product:
    """ 
        Attributes:
            id (str):
            name (str):
            category (str):
            description (None | str):
            origin (None | str):
            hts_code (None | str):
            allergens (list[str]):
            tags (list[str]):
            pricing (PricingSchedule):
            pack (ProductPack):
            in_stock (bool):
            inventory (int):
            coa_available (bool):
            document_ids (list[str]):
            kind (SkuKind | Unset): What kind of SKU — only `physical` requires a ship-to destination.
     """

    id: str
    name: str
    category: str
    description: None | str
    origin: None | str
    hts_code: None | str
    allergens: list[str]
    tags: list[str]
    pricing: PricingSchedule
    pack: ProductPack
    in_stock: bool
    inventory: int
    coa_available: bool
    document_ids: list[str]
    kind: SkuKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pricing_schedule import PricingSchedule
        from ..models.product_pack import ProductPack
        id = self.id

        name = self.name

        category = self.category

        description: None | str
        description = self.description

        origin: None | str
        origin = self.origin

        hts_code: None | str
        hts_code = self.hts_code

        allergens = self.allergens



        tags = self.tags



        pricing = self.pricing.to_dict()

        pack = self.pack.to_dict()

        in_stock = self.in_stock

        inventory = self.inventory

        coa_available = self.coa_available

        document_ids = self.document_ids



        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "category": category,
            "description": description,
            "origin": origin,
            "hts_code": hts_code,
            "allergens": allergens,
            "tags": tags,
            "pricing": pricing,
            "pack": pack,
            "in_stock": in_stock,
            "inventory": inventory,
            "coa_available": coa_available,
            "document_ids": document_ids,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_schedule import PricingSchedule
        from ..models.product_pack import ProductPack
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        category = d.pop("category")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        def _parse_origin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        origin = _parse_origin(d.pop("origin"))


        def _parse_hts_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hts_code = _parse_hts_code(d.pop("hts_code"))


        allergens = cast(list[str], d.pop("allergens"))


        tags = cast(list[str], d.pop("tags"))


        pricing = PricingSchedule.from_dict(d.pop("pricing"))




        pack = ProductPack.from_dict(d.pop("pack"))




        in_stock = d.pop("in_stock")

        inventory = d.pop("inventory")

        coa_available = d.pop("coa_available")

        document_ids = cast(list[str], d.pop("document_ids"))


        _kind = d.pop("kind", UNSET)
        kind: SkuKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = SkuKind(_kind)




        product = cls(
            id=id,
            name=name,
            category=category,
            description=description,
            origin=origin,
            hts_code=hts_code,
            allergens=allergens,
            tags=tags,
            pricing=pricing,
            pack=pack,
            in_stock=in_stock,
            inventory=inventory,
            coa_available=coa_available,
            document_ids=document_ids,
            kind=kind,
        )


        product.additional_properties = d
        return product

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
