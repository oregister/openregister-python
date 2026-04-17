# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TransparenzregisterGroup"]


class TransparenzregisterGroup(BaseModel):
    description: Optional[str] = None

    interest_type: Optional[str] = None

    position: Optional[int] = None
