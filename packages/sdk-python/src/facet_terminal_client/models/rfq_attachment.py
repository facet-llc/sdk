from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RfqAttachment")



@_attrs_define
class RfqAttachment:
    """ 
        Attributes:
            url (str):
            label (str | Unset):
            mime (str | Unset):
            size (int | Unset):
            kind (str | Unset):
     """

    url: str
    label: str | Unset = UNSET
    mime: str | Unset = UNSET
    size: int | Unset = UNSET
    kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        label = self.label

        mime = self.mime

        size = self.size

        kind = self.kind


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
        })
        if label is not UNSET:
            field_dict["label"] = label
        if mime is not UNSET:
            field_dict["mime"] = mime
        if size is not UNSET:
            field_dict["size"] = size
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        label = d.pop("label", UNSET)

        mime = d.pop("mime", UNSET)

        size = d.pop("size", UNSET)

        kind = d.pop("kind", UNSET)

        rfq_attachment = cls(
            url=url,
            label=label,
            mime=mime,
            size=size,
            kind=kind,
        )


        rfq_attachment.additional_properties = d
        return rfq_attachment

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
