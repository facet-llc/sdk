from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.counter_quote_request_counter_terms import CounterQuoteRequestCounterTerms





T = TypeVar("T", bound="CounterQuoteRequest")



@_attrs_define
class CounterQuoteRequest:
    """ 
        Attributes:
            request_id (str):
            body (str):
            quote_id (str | Unset):
            counter_terms (CounterQuoteRequestCounterTerms | Unset):
     """

    request_id: str
    body: str
    quote_id: str | Unset = UNSET
    counter_terms: CounterQuoteRequestCounterTerms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.counter_quote_request_counter_terms import CounterQuoteRequestCounterTerms
        request_id = self.request_id

        body = self.body

        quote_id = self.quote_id

        counter_terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counter_terms, Unset):
            counter_terms = self.counter_terms.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "request_id": request_id,
            "body": body,
        })
        if quote_id is not UNSET:
            field_dict["quote_id"] = quote_id
        if counter_terms is not UNSET:
            field_dict["counter_terms"] = counter_terms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.counter_quote_request_counter_terms import CounterQuoteRequestCounterTerms
        d = dict(src_dict)
        request_id = d.pop("request_id")

        body = d.pop("body")

        quote_id = d.pop("quote_id", UNSET)

        _counter_terms = d.pop("counter_terms", UNSET)
        counter_terms: CounterQuoteRequestCounterTerms | Unset
        if isinstance(_counter_terms,  Unset):
            counter_terms = UNSET
        else:
            counter_terms = CounterQuoteRequestCounterTerms.from_dict(_counter_terms)




        counter_quote_request = cls(
            request_id=request_id,
            body=body,
            quote_id=quote_id,
            counter_terms=counter_terms,
        )


        counter_quote_request.additional_properties = d
        return counter_quote_request

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
