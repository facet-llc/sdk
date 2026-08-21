from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_signature_record_party import OrderSignatureRecordParty
from typing import cast






T = TypeVar("T", bound="OrderSignatureRecord")



@_attrs_define
class OrderSignatureRecord:
    """ One row of the outbound Facet signature ledger. A party='facet' row is Facet's Ed25519 signature over the response
    it returned, with the hex request/response hashes and the hash-chain links; a merchant/agent row is a post-
    settlement fulfilment attestation. Byte values are lowercase hex.

        Attributes:
            party (OrderSignatureRecordParty):
            signing_key_id (str):
            request_hash (str):
            response_hash (str):
            prev_hash (None | str): Null at the chain root.
            this_hash (str):
            signature (str):
            attestation (None | str):
            attestation_strength (None | str):
            attestation_jws (None | str):
            signer_ref (None | str):
            signed_at (str):
     """

    party: OrderSignatureRecordParty
    signing_key_id: str
    request_hash: str
    response_hash: str
    prev_hash: None | str
    this_hash: str
    signature: str
    attestation: None | str
    attestation_strength: None | str
    attestation_jws: None | str
    signer_ref: None | str
    signed_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        party = self.party.value

        signing_key_id = self.signing_key_id

        request_hash = self.request_hash

        response_hash = self.response_hash

        prev_hash: None | str
        prev_hash = self.prev_hash

        this_hash = self.this_hash

        signature = self.signature

        attestation: None | str
        attestation = self.attestation

        attestation_strength: None | str
        attestation_strength = self.attestation_strength

        attestation_jws: None | str
        attestation_jws = self.attestation_jws

        signer_ref: None | str
        signer_ref = self.signer_ref

        signed_at = self.signed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "party": party,
            "signing_key_id": signing_key_id,
            "request_hash": request_hash,
            "response_hash": response_hash,
            "prev_hash": prev_hash,
            "this_hash": this_hash,
            "signature": signature,
            "attestation": attestation,
            "attestation_strength": attestation_strength,
            "attestation_jws": attestation_jws,
            "signer_ref": signer_ref,
            "signed_at": signed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party = OrderSignatureRecordParty(d.pop("party"))




        signing_key_id = d.pop("signing_key_id")

        request_hash = d.pop("request_hash")

        response_hash = d.pop("response_hash")

        def _parse_prev_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev_hash = _parse_prev_hash(d.pop("prev_hash"))


        this_hash = d.pop("this_hash")

        signature = d.pop("signature")

        def _parse_attestation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        attestation = _parse_attestation(d.pop("attestation"))


        def _parse_attestation_strength(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        attestation_strength = _parse_attestation_strength(d.pop("attestation_strength"))


        def _parse_attestation_jws(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        attestation_jws = _parse_attestation_jws(d.pop("attestation_jws"))


        def _parse_signer_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signer_ref = _parse_signer_ref(d.pop("signer_ref"))


        signed_at = d.pop("signed_at")

        order_signature_record = cls(
            party=party,
            signing_key_id=signing_key_id,
            request_hash=request_hash,
            response_hash=response_hash,
            prev_hash=prev_hash,
            this_hash=this_hash,
            signature=signature,
            attestation=attestation,
            attestation_strength=attestation_strength,
            attestation_jws=attestation_jws,
            signer_ref=signer_ref,
            signed_at=signed_at,
        )


        order_signature_record.additional_properties = d
        return order_signature_record

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
