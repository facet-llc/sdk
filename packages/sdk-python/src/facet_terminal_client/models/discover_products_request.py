from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DiscoverProductsRequest")



@_attrs_define
class DiscoverProductsRequest:
    """ 
        Attributes:
            query (str | Unset): Free-text search over product name + description (case-insensitive; % and _ match
                literally).
            category (str | Unset): Exact product category match.
            tags (list[str] | Unset): Tag containment: every listed tag must be present on the product.
            like_id (str | Unset): Attribute-based similar items: an anchor product_id. When set, returns other same-
                category products ranked by tag overlap then price proximity to the anchor (no ML, no embeddings), and `query`
                becomes optional. Counts as a narrowing filter. The anchor is resolved only from an opted-in merchant, so a
                like_id for a non-discoverable product returns empty.
            like_merchant (str | Unset): Optional companion to `like_id`: the anchor merchant's display name, disambiguating
                an anchor SKU shared across merchants. Ignored unless `like_id` is set.
            limit (int | Unset): Page size (default 20, capped server-side at 50).
            offset (int | Unset): Page offset (default 0; forced to 0 on the credential-less public-safe path).
     """

    query: str | Unset = UNSET
    category: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    like_id: str | Unset = UNSET
    like_merchant: str | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        query = self.query

        category = self.category

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        like_id = self.like_id

        like_merchant = self.like_merchant

        limit = self.limit

        offset = self.offset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if query is not UNSET:
            field_dict["query"] = query
        if category is not UNSET:
            field_dict["category"] = category
        if tags is not UNSET:
            field_dict["tags"] = tags
        if like_id is not UNSET:
            field_dict["like_id"] = like_id
        if like_merchant is not UNSET:
            field_dict["like_merchant"] = like_merchant
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query", UNSET)

        category = d.pop("category", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        like_id = d.pop("like_id", UNSET)

        like_merchant = d.pop("like_merchant", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        discover_products_request = cls(
            query=query,
            category=category,
            tags=tags,
            like_id=like_id,
            like_merchant=like_merchant,
            limit=limit,
            offset=offset,
        )


        discover_products_request.additional_properties = d
        return discover_products_request

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
