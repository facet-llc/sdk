from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.document_kind import DocumentKind
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateDocumentRequest")



@_attrs_define
class UpdateDocumentRequest:
    """ 
        Attributes:
            site_id (str): UUID. The caller must be an admin+ member of this site.
            document_id (str):
            kind (DocumentKind | Unset):
            title (str | Unset):
            url (str | Unset):
            mime_type (str | Unset):
            size_bytes (int | None | Unset):
            issued_at (None | str | Unset): ISO 8601.
            expires_at (None | str | Unset): ISO 8601.
     """

    site_id: str
    document_id: str
    kind: DocumentKind | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    size_bytes: int | None | Unset = UNSET
    issued_at: None | str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        document_id = self.document_id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        title = self.title

        url = self.url

        mime_type = self.mime_type

        size_bytes: int | None | Unset
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        issued_at: None | str | Unset
        if isinstance(self.issued_at, Unset):
            issued_at = UNSET
        else:
            issued_at = self.issued_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "document_id": document_id,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        document_id = d.pop("document_id")

        _kind = d.pop("kind", UNSET)
        kind: DocumentKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = DocumentKind(_kind)




        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        def _parse_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes", UNSET))


        def _parse_issued_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issued_at = _parse_issued_at(d.pop("issued_at", UNSET))


        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        update_document_request = cls(
            site_id=site_id,
            document_id=document_id,
            kind=kind,
            title=title,
            url=url,
            mime_type=mime_type,
            size_bytes=size_bytes,
            issued_at=issued_at,
            expires_at=expires_at,
        )


        update_document_request.additional_properties = d
        return update_document_request

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
