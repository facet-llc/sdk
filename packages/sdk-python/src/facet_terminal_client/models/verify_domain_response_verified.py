from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.verification_method import VerificationMethod






T = TypeVar("T", bound="VerifyDomainResponseVerified")



@_attrs_define
class VerifyDomainResponseVerified:
    """ 
        Attributes:
            verified (bool): Always true on this branch.
            site_id (str):
            method (VerificationMethod):
            verified_at (str):
     """

    verified: bool
    site_id: str
    method: VerificationMethod
    verified_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        verified = self.verified

        site_id = self.site_id

        method = self.method.value

        verified_at = self.verified_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "verified": verified,
            "site_id": site_id,
            "method": method,
            "verified_at": verified_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verified = d.pop("verified")

        site_id = d.pop("site_id")

        method = VerificationMethod(d.pop("method"))




        verified_at = d.pop("verified_at")

        verify_domain_response_verified = cls(
            verified=verified,
            site_id=site_id,
            method=method,
            verified_at=verified_at,
        )


        verify_domain_response_verified.additional_properties = d
        return verify_domain_response_verified

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
