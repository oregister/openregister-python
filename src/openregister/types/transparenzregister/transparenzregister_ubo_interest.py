# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TransparenzregisterUboInterest"]


class TransparenzregisterUboInterest(BaseModel):
    percentage: Optional[float] = None

    scope: Optional[str] = None

    type: Optional[str] = None
