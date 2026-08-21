from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.facet_error_suggest_args import FacetErrorSuggestArgs





T = TypeVar("T", bound="FacetErrorSuggest")



@_attrs_define
class FacetErrorSuggest:
    """ Optional follow-up hints attached to a FacetErrorBody.

        Attributes:
            tool (str | Unset): Suggested tool name to call next.
            args (FacetErrorSuggestArgs | Unset): Suggested arguments to pass on the suggested call.
            doc (str | Unset): Link to the relevant documentation.
            upgrade (str | Unset): Upgrade CTA when CAPABILITY_NOT_GRANTED gates a tier-paid tool.
            signup (str | Unset): Issuer signup URL surfaced on UNAUTHORIZED so an unauthenticated agent can onboard without
                an out-of-band lookup.
     """

    tool: str | Unset = UNSET
    args: FacetErrorSuggestArgs | Unset = UNSET
    doc: str | Unset = UNSET
    upgrade: str | Unset = UNSET
    signup: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.facet_error_suggest_args import FacetErrorSuggestArgs
        tool = self.tool

        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        doc = self.doc

        upgrade = self.upgrade

        signup = self.signup


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tool is not UNSET:
            field_dict["tool"] = tool
        if args is not UNSET:
            field_dict["args"] = args
        if doc is not UNSET:
            field_dict["doc"] = doc
        if upgrade is not UNSET:
            field_dict["upgrade"] = upgrade
        if signup is not UNSET:
            field_dict["signup"] = signup

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.facet_error_suggest_args import FacetErrorSuggestArgs
        d = dict(src_dict)
        tool = d.pop("tool", UNSET)

        _args = d.pop("args", UNSET)
        args: FacetErrorSuggestArgs | Unset
        if isinstance(_args,  Unset):
            args = UNSET
        else:
            args = FacetErrorSuggestArgs.from_dict(_args)




        doc = d.pop("doc", UNSET)

        upgrade = d.pop("upgrade", UNSET)

        signup = d.pop("signup", UNSET)

        facet_error_suggest = cls(
            tool=tool,
            args=args,
            doc=doc,
            upgrade=upgrade,
            signup=signup,
        )


        facet_error_suggest.additional_properties = d
        return facet_error_suggest

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
