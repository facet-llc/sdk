from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.rfq_quote import RfqQuote
  from ..models.rfq_request import RfqRequest





T = TypeVar("T", bound="GetRfqStatusResponse")



@_attrs_define
class GetRfqStatusResponse:
    """ 
        Attributes:
            request (RfqRequest):
            quotes (list[RfqQuote]):
     """

    request: RfqRequest
    quotes: list[RfqQuote]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rfq_quote import RfqQuote
        from ..models.rfq_request import RfqRequest
        request = self.request.to_dict()

        quotes = []
        for quotes_item_data in self.quotes:
            quotes_item = quotes_item_data.to_dict()
            quotes.append(quotes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "request": request,
            "quotes": quotes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rfq_quote import RfqQuote
        from ..models.rfq_request import RfqRequest
        d = dict(src_dict)
        request = RfqRequest.from_dict(d.pop("request"))




        quotes = []
        _quotes = d.pop("quotes")
        for quotes_item_data in (_quotes):
            quotes_item = RfqQuote.from_dict(quotes_item_data)



            quotes.append(quotes_item)


        get_rfq_status_response = cls(
            request=request,
            quotes=quotes,
        )


        get_rfq_status_response.additional_properties = d
        return get_rfq_status_response

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
