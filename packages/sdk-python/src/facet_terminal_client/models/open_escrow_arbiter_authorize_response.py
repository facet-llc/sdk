from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_escrow_arbiter_authorize_response_status import OpenEscrowArbiterAuthorizeResponseStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.open_escrow_arbiter_authorize_response_authorization import OpenEscrowArbiterAuthorizeResponseAuthorization





T = TypeVar("T", bound="OpenEscrowArbiterAuthorizeResponse")



@_attrs_define
class OpenEscrowArbiterAuthorizeResponse:
    """ 
        Attributes:
            field_status (OpenEscrowArbiterAuthorizeResponseStatus):
            authorization (OpenEscrowArbiterAuthorizeResponseAuthorization):
     """

    field_status: OpenEscrowArbiterAuthorizeResponseStatus
    authorization: OpenEscrowArbiterAuthorizeResponseAuthorization
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_escrow_arbiter_authorize_response_authorization import OpenEscrowArbiterAuthorizeResponseAuthorization
        field_status = self.field_status.value

        authorization = self.authorization.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "_status": field_status,
            "authorization": authorization,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_escrow_arbiter_authorize_response_authorization import OpenEscrowArbiterAuthorizeResponseAuthorization
        d = dict(src_dict)
        field_status = OpenEscrowArbiterAuthorizeResponseStatus(d.pop("_status"))




        authorization = OpenEscrowArbiterAuthorizeResponseAuthorization.from_dict(d.pop("authorization"))




        open_escrow_arbiter_authorize_response = cls(
            field_status=field_status,
            authorization=authorization,
        )


        open_escrow_arbiter_authorize_response.additional_properties = d
        return open_escrow_arbiter_authorize_response

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
