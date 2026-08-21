from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ComplianceCertification")



@_attrs_define
class ComplianceCertification:
    """ 
        Attributes:
            name (str):
            issued_by (None | str):
            valid_until (None | str):
            document_id (None | str):
     """

    name: str
    issued_by: None | str
    valid_until: None | str
    document_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        issued_by: None | str
        issued_by = self.issued_by

        valid_until: None | str
        valid_until = self.valid_until

        document_id: None | str
        document_id = self.document_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "issued_by": issued_by,
            "valid_until": valid_until,
            "document_id": document_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_issued_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issued_by = _parse_issued_by(d.pop("issued_by"))


        def _parse_valid_until(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        valid_until = _parse_valid_until(d.pop("valid_until"))


        def _parse_document_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        document_id = _parse_document_id(d.pop("document_id"))


        compliance_certification = cls(
            name=name,
            issued_by=issued_by,
            valid_until=valid_until,
            document_id=document_id,
        )


        compliance_certification.additional_properties = d
        return compliance_certification

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
