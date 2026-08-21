from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.discover_result_handoff import DiscoverResultHandoff
  from ..models.discover_result_reputation import DiscoverResultReputation





T = TypeVar("T", bound="DiscoverResult")



@_attrs_define
class DiscoverResult:
    """ 
        Attributes:
            ubi_id (str):
            name (str):
            address (None | str): Formatted single-line address from address_jsonb.
            lat (float | None):
            lng (float | None):
            distance_m (float | None): Distance from the search center; null with no geo center.
            naics (int | None):
            taxonomy (list[str]): facet_taxonomy tags.
            claim_status (str):
            reputation (DiscoverResultReputation):
            terminal_url (None | str): CLAIMED + live → https://<domain|terminal.facet.llc>/v1; CLAIMED + pre-live →
                https://<handle>.sandbox.facet.llc/v1; UNCLAIMED → null.
            capabilities (list[str] | None):
            handoff (DiscoverResultHandoff):
     """

    ubi_id: str
    name: str
    address: None | str
    lat: float | None
    lng: float | None
    distance_m: float | None
    naics: int | None
    taxonomy: list[str]
    claim_status: str
    reputation: DiscoverResultReputation
    terminal_url: None | str
    capabilities: list[str] | None
    handoff: DiscoverResultHandoff
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.discover_result_handoff import DiscoverResultHandoff
        from ..models.discover_result_reputation import DiscoverResultReputation
        ubi_id = self.ubi_id

        name = self.name

        address: None | str
        address = self.address

        lat: float | None
        lat = self.lat

        lng: float | None
        lng = self.lng

        distance_m: float | None
        distance_m = self.distance_m

        naics: int | None
        naics = self.naics

        taxonomy = self.taxonomy



        claim_status = self.claim_status

        reputation = self.reputation.to_dict()

        terminal_url: None | str
        terminal_url = self.terminal_url

        capabilities: list[str] | None
        if isinstance(self.capabilities, list):
            capabilities = self.capabilities


        else:
            capabilities = self.capabilities

        handoff = self.handoff.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ubi_id": ubi_id,
            "name": name,
            "address": address,
            "lat": lat,
            "lng": lng,
            "distance_m": distance_m,
            "naics": naics,
            "taxonomy": taxonomy,
            "claim_status": claim_status,
            "reputation": reputation,
            "terminal_url": terminal_url,
            "capabilities": capabilities,
            "handoff": handoff,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discover_result_handoff import DiscoverResultHandoff
        from ..models.discover_result_reputation import DiscoverResultReputation
        d = dict(src_dict)
        ubi_id = d.pop("ubi_id")

        name = d.pop("name")

        def _parse_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address = _parse_address(d.pop("address"))


        def _parse_lat(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lat = _parse_lat(d.pop("lat"))


        def _parse_lng(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lng = _parse_lng(d.pop("lng"))


        def _parse_distance_m(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        distance_m = _parse_distance_m(d.pop("distance_m"))


        def _parse_naics(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        naics = _parse_naics(d.pop("naics"))


        taxonomy = cast(list[str], d.pop("taxonomy"))


        claim_status = d.pop("claim_status")

        reputation = DiscoverResultReputation.from_dict(d.pop("reputation"))




        def _parse_terminal_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        terminal_url = _parse_terminal_url(d.pop("terminal_url"))


        def _parse_capabilities(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                capabilities_type_0 = cast(list[str], data)

                return capabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        capabilities = _parse_capabilities(d.pop("capabilities"))


        handoff = DiscoverResultHandoff.from_dict(d.pop("handoff"))




        discover_result = cls(
            ubi_id=ubi_id,
            name=name,
            address=address,
            lat=lat,
            lng=lng,
            distance_m=distance_m,
            naics=naics,
            taxonomy=taxonomy,
            claim_status=claim_status,
            reputation=reputation,
            terminal_url=terminal_url,
            capabilities=capabilities,
            handoff=handoff,
        )


        discover_result.additional_properties = d
        return discover_result

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
