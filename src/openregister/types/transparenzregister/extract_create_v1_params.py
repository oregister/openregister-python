# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExtractCreateV1Params"]


class ExtractCreateV1Params(TypedDict, total=False):
    company_id: str
    """
    Unique company identifier. Required unless `X-Credential-Name` is set to
    `sandbox`. In sandbox mode this field should be omitted. Example:
    DE-HRB-F1103-267645
    """

    x_credential_name: Annotated[str, PropertyInfo(alias="X-Credential-Name")]
