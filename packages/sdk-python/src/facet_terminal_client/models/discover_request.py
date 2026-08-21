from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.discover_request_edge import DiscoverRequestEdge
  from ..models.discover_request_near import DiscoverRequestNear





T = TypeVar("T", bound="DiscoverRequest")



@_attrs_define
class DiscoverRequest:
    """ 
        Attributes:
            query (str | Unset): NL / keyword search over name (+ facet_taxonomy text match).
            near (DiscoverRequestNear | Unset): Geo search center; pairs with radius_km.
            radius_km (float | Unset): Search radius in km (applied only when `near` is given).
            naics (list[int] | Unset): Match universal_business_index.naics = ANY.
            taxonomy (list[str] | Unset): facet_taxonomy overlap (&&) filter.
            capabilities (list[str] | Unset): Capability tags; folded into the facet_taxonomy overlap filter.
            edge (DiscoverRequestEdge | Unset): One-hop knowledge-graph relationship filter.
            min_reputation (float | Unset): Min mv_ubi_facet_score.avg_score.
            claimed_only (bool | Unset): Only return businesses with a claimed site.
            limit (int | Unset): Page size (default 20, capped server-side at 50).
            offset (int | Unset): Page offset (default 0).
     """

    query: str | Unset = UNSET
    near: DiscoverRequestNear | Unset = UNSET
    radius_km: float | Unset = UNSET
    naics: list[int] | Unset = UNSET
    taxonomy: list[str] | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    edge: DiscoverRequestEdge | Unset = UNSET
    min_reputation: float | Unset = UNSET
    claimed_only: bool | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.discover_request_edge import DiscoverRequestEdge
        from ..models.discover_request_near import DiscoverRequestNear
        query = self.query

        near: dict[str, Any] | Unset = UNSET
        if not isinstance(self.near, Unset):
            near = self.near.to_dict()

        radius_km = self.radius_km

        naics: list[int] | Unset = UNSET
        if not isinstance(self.naics, Unset):
            naics = self.naics



        taxonomy: list[str] | Unset = UNSET
        if not isinstance(self.taxonomy, Unset):
            taxonomy = self.taxonomy



        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities



        edge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.edge, Unset):
            edge = self.edge.to_dict()

        min_reputation = self.min_reputation

        claimed_only = self.claimed_only

        limit = self.limit

        offset = self.offset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if query is not UNSET:
            field_dict["query"] = query
        if near is not UNSET:
            field_dict["near"] = near
        if radius_km is not UNSET:
            field_dict["radius_km"] = radius_km
        if naics is not UNSET:
            field_dict["naics"] = naics
        if taxonomy is not UNSET:
            field_dict["taxonomy"] = taxonomy
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if edge is not UNSET:
            field_dict["edge"] = edge
        if min_reputation is not UNSET:
            field_dict["min_reputation"] = min_reputation
        if claimed_only is not UNSET:
            field_dict["claimed_only"] = claimed_only
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discover_request_edge import DiscoverRequestEdge
        from ..models.discover_request_near import DiscoverRequestNear
        d = dict(src_dict)
        query = d.pop("query", UNSET)

        _near = d.pop("near", UNSET)
        near: DiscoverRequestNear | Unset
        if isinstance(_near,  Unset):
            near = UNSET
        else:
            near = DiscoverRequestNear.from_dict(_near)




        radius_km = d.pop("radius_km", UNSET)

        naics = cast(list[int], d.pop("naics", UNSET))


        taxonomy = cast(list[str], d.pop("taxonomy", UNSET))


        capabilities = cast(list[str], d.pop("capabilities", UNSET))


        _edge = d.pop("edge", UNSET)
        edge: DiscoverRequestEdge | Unset
        if isinstance(_edge,  Unset):
            edge = UNSET
        else:
            edge = DiscoverRequestEdge.from_dict(_edge)




        min_reputation = d.pop("min_reputation", UNSET)

        claimed_only = d.pop("claimed_only", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        discover_request = cls(
            query=query,
            near=near,
            radius_km=radius_km,
            naics=naics,
            taxonomy=taxonomy,
            capabilities=capabilities,
            edge=edge,
            min_reputation=min_reputation,
            claimed_only=claimed_only,
            limit=limit,
            offset=offset,
        )


        discover_request.additional_properties = d
        return discover_request

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
