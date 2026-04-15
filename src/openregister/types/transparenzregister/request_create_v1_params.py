# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RequestCreateV1Params"]


class RequestCreateV1Params(TypedDict, total=False):
    company_id: str
    """Unique company identifier.

    Required unless using X-Credential-Label=test. Example: DE-HRB-F1103-267645
    """

    x_credential_label: Annotated[str, PropertyInfo(alias="X-Credential-Label")]
