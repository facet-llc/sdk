from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jwk_alg import JwkAlg
from ..models.jwk_crv import JwkCrv
from ..models.jwk_kty import JwkKty
from ..models.jwk_use import JwkUse
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Jwk")



@_attrs_define
class Jwk:
    """ 
        Attributes:
            kty (JwkKty):
            crv (JwkCrv):
            x (str): Raw 32-byte Ed25519 public key, unpadded base64url. Identical bytes and encoding to
                FacetPublicKey.public_key_b64; only the name differs.
            alg (JwkAlg):
            kid (str):
            use (JwkUse | Unset):
            key_ops (list[str] | Unset):
     """

    kty: JwkKty
    crv: JwkCrv
    x: str
    alg: JwkAlg
    kid: str
    use: JwkUse | Unset = UNSET
    key_ops: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kty = self.kty.value

        crv = self.crv.value

        x = self.x

        alg = self.alg.value

        kid = self.kid

        use: str | Unset = UNSET
        if not isinstance(self.use, Unset):
            use = self.use.value


        key_ops: list[str] | Unset = UNSET
        if not isinstance(self.key_ops, Unset):
            key_ops = self.key_ops




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kty": kty,
            "crv": crv,
            "x": x,
            "alg": alg,
            "kid": kid,
        })
        if use is not UNSET:
            field_dict["use"] = use
        if key_ops is not UNSET:
            field_dict["key_ops"] = key_ops

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kty = JwkKty(d.pop("kty"))




        crv = JwkCrv(d.pop("crv"))




        x = d.pop("x")

        alg = JwkAlg(d.pop("alg"))




        kid = d.pop("kid")

        _use = d.pop("use", UNSET)
        use: JwkUse | Unset
        if isinstance(_use,  Unset):
            use = UNSET
        else:
            use = JwkUse(_use)




        key_ops = cast(list[str], d.pop("key_ops", UNSET))


        jwk = cls(
            kty=kty,
            crv=crv,
            x=x,
            alg=alg,
            kid=kid,
            use=use,
            key_ops=key_ops,
        )


        jwk.additional_properties = d
        return jwk

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
