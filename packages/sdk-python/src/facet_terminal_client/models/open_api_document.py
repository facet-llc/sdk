from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.open_api_document_components import OpenApiDocumentComponents
  from ..models.open_api_document_info import OpenApiDocumentInfo
  from ..models.open_api_document_paths import OpenApiDocumentPaths
  from ..models.open_api_document_servers_item import OpenApiDocumentServersItem
  from ..models.open_api_document_tags_item import OpenApiDocumentTagsItem





T = TypeVar("T", bound="OpenApiDocument")



@_attrs_define
class OpenApiDocument:
    """ OpenAPI 3.1 document. Shape is defined by the OpenAPI 3.1 schema; this stub lists the top-level fields a Facet
    Terminal emits and opts into additionalProperties so per-merchant overlays + future spec extensions parse cleanly.
    SDK generators should treat the response body as a self-describing OpenAPI 3.1 document.

        Attributes:
            openapi (str): OpenAPI specification version (e.g. '3.1.0').
            info (OpenApiDocumentInfo):
            paths (OpenApiDocumentPaths):
            servers (list[OpenApiDocumentServersItem] | Unset):
            tags (list[OpenApiDocumentTagsItem] | Unset):
            components (OpenApiDocumentComponents | Unset):
     """

    openapi: str
    info: OpenApiDocumentInfo
    paths: OpenApiDocumentPaths
    servers: list[OpenApiDocumentServersItem] | Unset = UNSET
    tags: list[OpenApiDocumentTagsItem] | Unset = UNSET
    components: OpenApiDocumentComponents | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_api_document_components import OpenApiDocumentComponents
        from ..models.open_api_document_info import OpenApiDocumentInfo
        from ..models.open_api_document_paths import OpenApiDocumentPaths
        from ..models.open_api_document_servers_item import OpenApiDocumentServersItem
        from ..models.open_api_document_tags_item import OpenApiDocumentTagsItem
        openapi = self.openapi

        info = self.info.to_dict()

        paths = self.paths.to_dict()

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)



        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)



        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "openapi": openapi,
            "info": info,
            "paths": paths,
        })
        if servers is not UNSET:
            field_dict["servers"] = servers
        if tags is not UNSET:
            field_dict["tags"] = tags
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_api_document_components import OpenApiDocumentComponents
        from ..models.open_api_document_info import OpenApiDocumentInfo
        from ..models.open_api_document_paths import OpenApiDocumentPaths
        from ..models.open_api_document_servers_item import OpenApiDocumentServersItem
        from ..models.open_api_document_tags_item import OpenApiDocumentTagsItem
        d = dict(src_dict)
        openapi = d.pop("openapi")

        info = OpenApiDocumentInfo.from_dict(d.pop("info"))




        paths = OpenApiDocumentPaths.from_dict(d.pop("paths"))




        _servers = d.pop("servers", UNSET)
        servers: list[OpenApiDocumentServersItem] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = OpenApiDocumentServersItem.from_dict(servers_item_data)



                servers.append(servers_item)


        _tags = d.pop("tags", UNSET)
        tags: list[OpenApiDocumentTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = OpenApiDocumentTagsItem.from_dict(tags_item_data)



                tags.append(tags_item)


        _components = d.pop("components", UNSET)
        components: OpenApiDocumentComponents | Unset
        if isinstance(_components,  Unset):
            components = UNSET
        else:
            components = OpenApiDocumentComponents.from_dict(_components)




        open_api_document = cls(
            openapi=openapi,
            info=info,
            paths=paths,
            servers=servers,
            tags=tags,
            components=components,
        )


        open_api_document.additional_properties = d
        return open_api_document

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
