from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rfq_request_status import RfqRequestStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.rfq_attachment import RfqAttachment
  from ..models.rfq_request_spec_jsonb import RfqRequestSpecJsonb





T = TypeVar("T", bound="RfqRequest")



@_attrs_define
class RfqRequest:
    """ 
        Attributes:
            id (str):
            site_id (str):
            agent_aid (str):
            spec_jsonb (RfqRequestSpecJsonb):
            attachments_jsonb (list[RfqAttachment]):
            status (RfqRequestStatus):
            needed_by (None | str):
            expires_at (None | str):
            notes (None | str):
            created_at (str):
            updated_at (str):
     """

    id: str
    site_id: str
    agent_aid: str
    spec_jsonb: RfqRequestSpecJsonb
    attachments_jsonb: list[RfqAttachment]
    status: RfqRequestStatus
    needed_by: None | str
    expires_at: None | str
    notes: None | str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rfq_attachment import RfqAttachment
        from ..models.rfq_request_spec_jsonb import RfqRequestSpecJsonb
        id = self.id

        site_id = self.site_id

        agent_aid = self.agent_aid

        spec_jsonb = self.spec_jsonb.to_dict()

        attachments_jsonb = []
        for attachments_jsonb_item_data in self.attachments_jsonb:
            attachments_jsonb_item = attachments_jsonb_item_data.to_dict()
            attachments_jsonb.append(attachments_jsonb_item)



        status = self.status.value

        needed_by: None | str
        needed_by = self.needed_by

        expires_at: None | str
        expires_at = self.expires_at

        notes: None | str
        notes = self.notes

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "site_id": site_id,
            "agent_aid": agent_aid,
            "spec_jsonb": spec_jsonb,
            "attachments_jsonb": attachments_jsonb,
            "status": status,
            "needed_by": needed_by,
            "expires_at": expires_at,
            "notes": notes,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rfq_attachment import RfqAttachment
        from ..models.rfq_request_spec_jsonb import RfqRequestSpecJsonb
        d = dict(src_dict)
        id = d.pop("id")

        site_id = d.pop("site_id")

        agent_aid = d.pop("agent_aid")

        spec_jsonb = RfqRequestSpecJsonb.from_dict(d.pop("spec_jsonb"))




        attachments_jsonb = []
        _attachments_jsonb = d.pop("attachments_jsonb")
        for attachments_jsonb_item_data in (_attachments_jsonb):
            attachments_jsonb_item = RfqAttachment.from_dict(attachments_jsonb_item_data)



            attachments_jsonb.append(attachments_jsonb_item)


        status = RfqRequestStatus(d.pop("status"))




        def _parse_needed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        needed_by = _parse_needed_by(d.pop("needed_by"))


        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))


        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))


        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        rfq_request = cls(
            id=id,
            site_id=site_id,
            agent_aid=agent_aid,
            spec_jsonb=spec_jsonb,
            attachments_jsonb=attachments_jsonb,
            status=status,
            needed_by=needed_by,
            expires_at=expires_at,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
        )


        rfq_request.additional_properties = d
        return rfq_request

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
