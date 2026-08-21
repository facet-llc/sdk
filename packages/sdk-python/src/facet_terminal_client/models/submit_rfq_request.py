from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rfq_attachment import RfqAttachment
  from ..models.submit_rfq_request_spec import SubmitRfqRequestSpec





T = TypeVar("T", bound="SubmitRfqRequest")



@_attrs_define
class SubmitRfqRequest:
    """ 
        Attributes:
            site_id (str):
            spec (SubmitRfqRequestSpec):
            attachments (list[RfqAttachment] | Unset):
            needed_by (str | Unset):
            expires_at (str | Unset):
            notes (str | Unset):
     """

    site_id: str
    spec: SubmitRfqRequestSpec
    attachments: list[RfqAttachment] | Unset = UNSET
    needed_by: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rfq_attachment import RfqAttachment
        from ..models.submit_rfq_request_spec import SubmitRfqRequestSpec
        site_id = self.site_id

        spec = self.spec.to_dict()

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        needed_by = self.needed_by

        expires_at = self.expires_at

        notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "spec": spec,
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if needed_by is not UNSET:
            field_dict["needed_by"] = needed_by
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rfq_attachment import RfqAttachment
        from ..models.submit_rfq_request_spec import SubmitRfqRequestSpec
        d = dict(src_dict)
        site_id = d.pop("site_id")

        spec = SubmitRfqRequestSpec.from_dict(d.pop("spec"))




        _attachments = d.pop("attachments", UNSET)
        attachments: list[RfqAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = RfqAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        needed_by = d.pop("needed_by", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        notes = d.pop("notes", UNSET)

        submit_rfq_request = cls(
            site_id=site_id,
            spec=spec,
            attachments=attachments,
            needed_by=needed_by,
            expires_at=expires_at,
            notes=notes,
        )


        submit_rfq_request.additional_properties = d
        return submit_rfq_request

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
