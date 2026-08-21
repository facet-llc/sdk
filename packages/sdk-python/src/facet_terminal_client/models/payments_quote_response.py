from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.payments_quote_response_rail_metadata import PaymentsQuoteResponseRailMetadata
  from ..models.payments_quote_response_requirements import PaymentsQuoteResponseRequirements





T = TypeVar("T", bound="PaymentsQuoteResponse")



@_attrs_define
class PaymentsQuoteResponse:
    """ 
        Attributes:
            rail_id (str): Stable rail identifier — namespaces match /v1/terms.settlement_rails (e.g. 'coin/usdc-base',
                'card/stripe', 'voucher/skyfire').
            requirements (PaymentsQuoteResponseRequirements): Rail-specific payment-requirements; for Boson the seller-
                signed EscrowPaymentRequirements.
            expires_at (None | str): ISO-8601 quote expiry.
            rail_metadata (PaymentsQuoteResponseRailMetadata | Unset):
     """

    rail_id: str
    requirements: PaymentsQuoteResponseRequirements
    expires_at: None | str
    rail_metadata: PaymentsQuoteResponseRailMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.payments_quote_response_rail_metadata import PaymentsQuoteResponseRailMetadata
        from ..models.payments_quote_response_requirements import PaymentsQuoteResponseRequirements
        rail_id = self.rail_id

        requirements = self.requirements.to_dict()

        expires_at: None | str
        expires_at = self.expires_at

        rail_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rail_metadata, Unset):
            rail_metadata = self.rail_metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rail_id": rail_id,
            "requirements": requirements,
            "expires_at": expires_at,
        })
        if rail_metadata is not UNSET:
            field_dict["rail_metadata"] = rail_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payments_quote_response_rail_metadata import PaymentsQuoteResponseRailMetadata
        from ..models.payments_quote_response_requirements import PaymentsQuoteResponseRequirements
        d = dict(src_dict)
        rail_id = d.pop("rail_id")

        requirements = PaymentsQuoteResponseRequirements.from_dict(d.pop("requirements"))




        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))


        _rail_metadata = d.pop("rail_metadata", UNSET)
        rail_metadata: PaymentsQuoteResponseRailMetadata | Unset
        if isinstance(_rail_metadata,  Unset):
            rail_metadata = UNSET
        else:
            rail_metadata = PaymentsQuoteResponseRailMetadata.from_dict(_rail_metadata)




        payments_quote_response = cls(
            rail_id=rail_id,
            requirements=requirements,
            expires_at=expires_at,
            rail_metadata=rail_metadata,
        )


        payments_quote_response.additional_properties = d
        return payments_quote_response

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
