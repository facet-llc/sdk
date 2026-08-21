from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_certification import ComplianceCertification
  from ..models.compliance_document import ComplianceDocument
  from ..models.get_compliance_response_allergens import GetComplianceResponseAllergens
  from ..models.get_compliance_response_fsma_204 import GetComplianceResponseFsma204





T = TypeVar("T", bound="GetComplianceResponse")



@_attrs_define
class GetComplianceResponse:
    """ 
        Attributes:
            product_id (str):
            allergens (GetComplianceResponseAllergens):
            fsma_204 (GetComplianceResponseFsma204):
            certifications (list[ComplianceCertification]):
            documents (list[ComplianceDocument]):
     """

    product_id: str
    allergens: GetComplianceResponseAllergens
    fsma_204: GetComplianceResponseFsma204
    certifications: list[ComplianceCertification]
    documents: list[ComplianceDocument]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_certification import ComplianceCertification
        from ..models.compliance_document import ComplianceDocument
        from ..models.get_compliance_response_allergens import GetComplianceResponseAllergens
        from ..models.get_compliance_response_fsma_204 import GetComplianceResponseFsma204
        product_id = self.product_id

        allergens = self.allergens.to_dict()

        fsma_204 = self.fsma_204.to_dict()

        certifications = []
        for certifications_item_data in self.certifications:
            certifications_item = certifications_item_data.to_dict()
            certifications.append(certifications_item)



        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
            "allergens": allergens,
            "fsma_204": fsma_204,
            "certifications": certifications,
            "documents": documents,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_certification import ComplianceCertification
        from ..models.compliance_document import ComplianceDocument
        from ..models.get_compliance_response_allergens import GetComplianceResponseAllergens
        from ..models.get_compliance_response_fsma_204 import GetComplianceResponseFsma204
        d = dict(src_dict)
        product_id = d.pop("product_id")

        allergens = GetComplianceResponseAllergens.from_dict(d.pop("allergens"))




        fsma_204 = GetComplianceResponseFsma204.from_dict(d.pop("fsma_204"))




        certifications = []
        _certifications = d.pop("certifications")
        for certifications_item_data in (_certifications):
            certifications_item = ComplianceCertification.from_dict(certifications_item_data)



            certifications.append(certifications_item)


        documents = []
        _documents = d.pop("documents")
        for documents_item_data in (_documents):
            documents_item = ComplianceDocument.from_dict(documents_item_data)



            documents.append(documents_item)


        get_compliance_response = cls(
            product_id=product_id,
            allergens=allergens,
            fsma_204=fsma_204,
            certifications=certifications,
            documents=documents,
        )


        get_compliance_response.additional_properties = d
        return get_compliance_response

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
