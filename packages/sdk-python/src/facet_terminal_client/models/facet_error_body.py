from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.facet_error_code import FacetErrorCode
from typing import cast

if TYPE_CHECKING:
  from ..models.facet_error_suggest import FacetErrorSuggest





T = TypeVar("T", bound="FacetErrorBody")



@_attrs_define
class FacetErrorBody:
    """ Error body inside the Facet error envelope.

        Attributes:
            code (FacetErrorCode): Closed enumeration of public error codes the Terminal will return. Grouped by class: auth
                (UNAUTHORIZED, FORBIDDEN, CAPABILITY_NOT_GRANTED); client (INVALID_REQUEST, NOT_FOUND, VERSION_NOT_SUPPORTED,
                METHOD_NOT_ALLOWED); throttling (RATE_LIMITED); domain (INVENTORY_UNAVAILABLE, QUOTE_EXPIRED,
                IDEMPOTENCY_CONFLICT, ALLERGEN_CONFLICT, SETTLEMENT_FAILED); fulfillment (FULFILLMENT_REQUIRED, UNDELIVERABLE);
                safety (PROHIBITED_GOODS); server (INTERNAL_ERROR).
            message (str): Human-readable error message.
            retryable (bool): Whether the caller may retry after backoff.
            retry_after_seconds (int | None):
            suggest (FacetErrorSuggest | None):
     """

    code: FacetErrorCode
    message: str
    retryable: bool
    retry_after_seconds: int | None
    suggest: FacetErrorSuggest | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.facet_error_suggest import FacetErrorSuggest
        code = self.code.value

        message = self.message

        retryable = self.retryable

        retry_after_seconds: int | None
        retry_after_seconds = self.retry_after_seconds

        suggest: dict[str, Any] | None
        if isinstance(self.suggest, FacetErrorSuggest):
            suggest = self.suggest.to_dict()
        else:
            suggest = self.suggest


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "message": message,
            "retryable": retryable,
            "retry_after_seconds": retry_after_seconds,
            "suggest": suggest,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.facet_error_suggest import FacetErrorSuggest
        d = dict(src_dict)
        code = FacetErrorCode(d.pop("code"))




        message = d.pop("message")

        retryable = d.pop("retryable")

        def _parse_retry_after_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        retry_after_seconds = _parse_retry_after_seconds(d.pop("retry_after_seconds"))


        def _parse_suggest(data: object) -> FacetErrorSuggest | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                suggest_type_0 = FacetErrorSuggest.from_dict(data)



                return suggest_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FacetErrorSuggest | None, data)

        suggest = _parse_suggest(d.pop("suggest"))


        facet_error_body = cls(
            code=code,
            message=message,
            retryable=retryable,
            retry_after_seconds=retry_after_seconds,
            suggest=suggest,
        )


        facet_error_body.additional_properties = d
        return facet_error_body

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
