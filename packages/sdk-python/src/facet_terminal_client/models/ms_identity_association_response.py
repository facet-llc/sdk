from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.ms_identity_associated_application import MsIdentityAssociatedApplication





T = TypeVar("T", bound="MsIdentityAssociationResponse")



@_attrs_define
class MsIdentityAssociationResponse:
    """ 
        Attributes:
            associated_applications (list[MsIdentityAssociatedApplication]):
     """

    associated_applications: list[MsIdentityAssociatedApplication]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ms_identity_associated_application import MsIdentityAssociatedApplication
        associated_applications = []
        for associated_applications_item_data in self.associated_applications:
            associated_applications_item = associated_applications_item_data.to_dict()
            associated_applications.append(associated_applications_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "associatedApplications": associated_applications,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ms_identity_associated_application import MsIdentityAssociatedApplication
        d = dict(src_dict)
        associated_applications = []
        _associated_applications = d.pop("associatedApplications")
        for associated_applications_item_data in (_associated_applications):
            associated_applications_item = MsIdentityAssociatedApplication.from_dict(associated_applications_item_data)



            associated_applications.append(associated_applications_item)


        ms_identity_association_response = cls(
            associated_applications=associated_applications,
        )


        ms_identity_association_response.additional_properties = d
        return ms_identity_association_response

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
