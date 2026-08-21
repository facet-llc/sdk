from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.facet_public_key import FacetPublicKey





T = TypeVar("T", bound="FacetKeyBundle")



@_attrs_define
class FacetKeyBundle:
    """ 
        Attributes:
            keys (list[FacetPublicKey]):
            current_kid (str):
     """

    keys: list[FacetPublicKey]
    current_kid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.facet_public_key import FacetPublicKey
        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)



        current_kid = self.current_kid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keys": keys,
            "current_kid": current_kid,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.facet_public_key import FacetPublicKey
        d = dict(src_dict)
        keys = []
        _keys = d.pop("keys")
        for keys_item_data in (_keys):
            keys_item = FacetPublicKey.from_dict(keys_item_data)



            keys.append(keys_item)


        current_kid = d.pop("current_kid")

        facet_key_bundle = cls(
            keys=keys,
            current_kid=current_kid,
        )


        facet_key_bundle.additional_properties = d
        return facet_key_bundle

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
