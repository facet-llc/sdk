from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_certification import ComplianceCertification





T = TypeVar("T", bound="CreateComplianceRequest")



@_attrs_define
class CreateComplianceRequest:
    """ 
        Attributes:
            site_id (str): UUID. The caller must be an admin+ member of this site.
            product_id (str): The product this override applies to. MUST belong to site_id.
            may_contain (list[str] | Unset):
            certifications (list[ComplianceCertification] | Unset):
            ftl_listed (bool | None | Unset):
            lot_code_format (None | str | Unset):
            kde_support (list[str] | None | Unset):
            cte_support (list[str] | None | Unset):
     """

    site_id: str
    product_id: str
    may_contain: list[str] | Unset = UNSET
    certifications: list[ComplianceCertification] | Unset = UNSET
    ftl_listed: bool | None | Unset = UNSET
    lot_code_format: None | str | Unset = UNSET
    kde_support: list[str] | None | Unset = UNSET
    cte_support: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_certification import ComplianceCertification
        site_id = self.site_id

        product_id = self.product_id

        may_contain: list[str] | Unset = UNSET
        if not isinstance(self.may_contain, Unset):
            may_contain = self.may_contain



        certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)



        ftl_listed: bool | None | Unset
        if isinstance(self.ftl_listed, Unset):
            ftl_listed = UNSET
        else:
            ftl_listed = self.ftl_listed

        lot_code_format: None | str | Unset
        if isinstance(self.lot_code_format, Unset):
            lot_code_format = UNSET
        else:
            lot_code_format = self.lot_code_format

        kde_support: list[str] | None | Unset
        if isinstance(self.kde_support, Unset):
            kde_support = UNSET
        elif isinstance(self.kde_support, list):
            kde_support = self.kde_support


        else:
            kde_support = self.kde_support

        cte_support: list[str] | None | Unset
        if isinstance(self.cte_support, Unset):
            cte_support = UNSET
        elif isinstance(self.cte_support, list):
            cte_support = self.cte_support


        else:
            cte_support = self.cte_support


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "site_id": site_id,
            "product_id": product_id,
        })
        if may_contain is not UNSET:
            field_dict["may_contain"] = may_contain
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if ftl_listed is not UNSET:
            field_dict["ftl_listed"] = ftl_listed
        if lot_code_format is not UNSET:
            field_dict["lot_code_format"] = lot_code_format
        if kde_support is not UNSET:
            field_dict["kde_support"] = kde_support
        if cte_support is not UNSET:
            field_dict["cte_support"] = cte_support

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_certification import ComplianceCertification
        d = dict(src_dict)
        site_id = d.pop("site_id")

        product_id = d.pop("product_id")

        may_contain = cast(list[str], d.pop("may_contain", UNSET))


        _certifications = d.pop("certifications", UNSET)
        certifications: list[ComplianceCertification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = ComplianceCertification.from_dict(certifications_item_data)



                certifications.append(certifications_item)


        def _parse_ftl_listed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ftl_listed = _parse_ftl_listed(d.pop("ftl_listed", UNSET))


        def _parse_lot_code_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_code_format = _parse_lot_code_format(d.pop("lot_code_format", UNSET))


        def _parse_kde_support(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kde_support_type_0 = cast(list[str], data)

                return kde_support_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        kde_support = _parse_kde_support(d.pop("kde_support", UNSET))


        def _parse_cte_support(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cte_support_type_0 = cast(list[str], data)

                return cte_support_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cte_support = _parse_cte_support(d.pop("cte_support", UNSET))


        create_compliance_request = cls(
            site_id=site_id,
            product_id=product_id,
            may_contain=may_contain,
            certifications=certifications,
            ftl_listed=ftl_listed,
            lot_code_format=lot_code_format,
            kde_support=kde_support,
            cte_support=cte_support,
        )


        create_compliance_request.additional_properties = d
        return create_compliance_request

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
