from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.document_kind import DocumentKind
from typing import cast






T = TypeVar("T", bound="CreateDocumentResponse")



@_attrs_define
class CreateDocumentResponse:
    """ 
        Attributes:
            document_id (str):
            product_id (str):
            kind (DocumentKind):
            title (str):
            url (str):
            mime_type (str):
            size_bytes (int | None):
            issued_at (None | str):
            expires_at (None | str):
     """

    document_id: str
    product_id: str
    kind: DocumentKind
    title: str
    url: str
    mime_type: str
    size_bytes: int | None
    issued_at: None | str
    expires_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        product_id = self.product_id

        kind = self.kind.value

        title = self.title

        url = self.url

        mime_type = self.mime_type

        size_bytes: int | None
        size_bytes = self.size_bytes

        issued_at: None | str
        issued_at = self.issued_at

        expires_at: None | str
        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "document_id": document_id,
            "product_id": product_id,
            "kind": kind,
            "title": title,
            "url": url,
            "mime_type": mime_type,
            "size_bytes": size_bytes,
            "issued_at": issued_at,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("document_id")

        product_id = d.pop("product_id")

        kind = DocumentKind(d.pop("kind"))




        title = d.pop("title")

        url = d.pop("url")

        mime_type = d.pop("mime_type")

        def _parse_size_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes"))


        def _parse_issued_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issued_at = _parse_issued_at(d.pop("issued_at"))


        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))


        create_document_response = cls(
            document_id=document_id,
            product_id=product_id,
            kind=kind,
            title=title,
            url=url,
            mime_type=mime_type,
            size_bytes=size_bytes,
            issued_at=issued_at,
            expires_at=expires_at,
        )


        create_document_response.additional_properties = d
        return create_document_response

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
