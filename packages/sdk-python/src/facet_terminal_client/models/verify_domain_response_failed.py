from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.verification_method import VerificationMethod
from ..models.verify_domain_response_failed_reason import VerifyDomainResponseFailedReason
from ..types import UNSET, Unset






T = TypeVar("T", bound="VerifyDomainResponseFailed")



@_attrs_define
class VerifyDomainResponseFailed:
    """ 
        Attributes:
            verified (bool): Always false on this branch.
            reason (VerifyDomainResponseFailedReason):
            method (VerificationMethod):
            hint (str):
            found (str | Unset):
     """

    verified: bool
    reason: VerifyDomainResponseFailedReason
    method: VerificationMethod
    hint: str
    found: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        verified = self.verified

        reason = self.reason.value

        method = self.method.value

        hint = self.hint

        found = self.found


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "verified": verified,
            "reason": reason,
            "method": method,
            "hint": hint,
        })
        if found is not UNSET:
            field_dict["found"] = found

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verified = d.pop("verified")

        reason = VerifyDomainResponseFailedReason(d.pop("reason"))




        method = VerificationMethod(d.pop("method"))




        hint = d.pop("hint")

        found = d.pop("found", UNSET)

        verify_domain_response_failed = cls(
            verified=verified,
            reason=reason,
            method=method,
            hint=hint,
            found=found,
        )


        verify_domain_response_failed.additional_properties = d
        return verify_domain_response_failed

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
