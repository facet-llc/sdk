from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.order_authorization_record import OrderAuthorizationRecord
  from ..models.order_signature_record import OrderSignatureRecord





T = TypeVar("T", bound="GetSignaturesResponse")



@_attrs_define
class GetSignaturesResponse:
    """ 
        Attributes:
            order_id (str):
            signatures (list[OrderSignatureRecord]):
            authorizations (list[OrderAuthorizationRecord]):
     """

    order_id: str
    signatures: list[OrderSignatureRecord]
    authorizations: list[OrderAuthorizationRecord]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_authorization_record import OrderAuthorizationRecord
        from ..models.order_signature_record import OrderSignatureRecord
        order_id = self.order_id

        signatures = []
        for signatures_item_data in self.signatures:
            signatures_item = signatures_item_data.to_dict()
            signatures.append(signatures_item)



        authorizations = []
        for authorizations_item_data in self.authorizations:
            authorizations_item = authorizations_item_data.to_dict()
            authorizations.append(authorizations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
            "signatures": signatures,
            "authorizations": authorizations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_authorization_record import OrderAuthorizationRecord
        from ..models.order_signature_record import OrderSignatureRecord
        d = dict(src_dict)
        order_id = d.pop("order_id")

        signatures = []
        _signatures = d.pop("signatures")
        for signatures_item_data in (_signatures):
            signatures_item = OrderSignatureRecord.from_dict(signatures_item_data)



            signatures.append(signatures_item)


        authorizations = []
        _authorizations = d.pop("authorizations")
        for authorizations_item_data in (_authorizations):
            authorizations_item = OrderAuthorizationRecord.from_dict(authorizations_item_data)



            authorizations.append(authorizations_item)


        get_signatures_response = cls(
            order_id=order_id,
            signatures=signatures,
            authorizations=authorizations,
        )


        get_signatures_response.additional_properties = d
        return get_signatures_response

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
