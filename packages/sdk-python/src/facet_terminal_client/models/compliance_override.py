from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_certification import ComplianceCertification





T = TypeVar("T", bound="ComplianceOverride")



@_attrs_define
class ComplianceOverride:
    """ 
        Attributes:
            product_id (str):
            may_contain (list[str]):
            certifications (list[ComplianceCertification]):
            ftl_listed (bool | None):
            lot_code_format (None | str):
            kde_support (list[str] | None):
            cte_support (list[str] | None):
     """

    product_id: str
    may_contain: list[str]
    certifications: list[ComplianceCertification]
    ftl_listed: bool | None
    lot_code_format: None | str
    kde_support: list[str] | None
    cte_support: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_certification import ComplianceCertification
        product_id = self.product_id

        may_contain = self.may_contain



        certifications = []
        for certifications_item_data in self.certifications:
            certifications_item = certifications_item_data.to_dict()
            certifications.append(certifications_item)



        ftl_listed: bool | None
        ftl_listed = self.ftl_listed

        lot_code_format: None | str
        lot_code_format = self.lot_code_format

        kde_support: list[str] | None
        if isinstance(self.kde_support, list):
            kde_support = self.kde_support


        else:
            kde_support = self.kde_support

        cte_support: list[str] | None
        if isinstance(self.cte_support, list):
            cte_support = self.cte_support


        else:
            cte_support = self.cte_support


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_id": product_id,
            "may_contain": may_contain,
            "certifications": certifications,
            "ftl_listed": ftl_listed,
            "lot_code_format": lot_code_format,
            "kde_support": kde_support,
            "cte_support": cte_support,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_certification import ComplianceCertification
        d = dict(src_dict)
        product_id = d.pop("product_id")

        may_contain = cast(list[str], d.pop("may_contain"))


        certifications = []
        _certifications = d.pop("certifications")
        for certifications_item_data in (_certifications):
            certifications_item = ComplianceCertification.from_dict(certifications_item_data)



            certifications.append(certifications_item)


        def _parse_ftl_listed(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        ftl_listed = _parse_ftl_listed(d.pop("ftl_listed"))


        def _parse_lot_code_format(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        lot_code_format = _parse_lot_code_format(d.pop("lot_code_format"))


        def _parse_kde_support(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kde_support_type_0 = cast(list[str], data)

                return kde_support_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        kde_support = _parse_kde_support(d.pop("kde_support"))


        def _parse_cte_support(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cte_support_type_0 = cast(list[str], data)

                return cte_support_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        cte_support = _parse_cte_support(d.pop("cte_support"))


        compliance_override = cls(
            product_id=product_id,
            may_contain=may_contain,
            certifications=certifications,
            ftl_listed=ftl_listed,
            lot_code_format=lot_code_format,
            kde_support=kde_support,
            cte_support=cte_support,
        )


        compliance_override.additional_properties = d
        return compliance_override

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
