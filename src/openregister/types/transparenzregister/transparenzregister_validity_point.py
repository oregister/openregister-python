# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["TransparenzregisterValidityPoint"]


class TransparenzregisterValidityPoint(BaseModel):
    date: Optional[datetime.date] = None

    note: Optional[str] = None
