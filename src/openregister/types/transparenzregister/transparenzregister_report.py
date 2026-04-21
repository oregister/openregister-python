# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel
from .transparenzregister_ubo import TransparenzregisterUbo
from .transparenzregister_group import TransparenzregisterGroup
from .transparenzregister_validity import TransparenzregisterValidity
from .transparenzregister_status_flags import TransparenzregisterStatusFlags

__all__ = ["TransparenzregisterReport"]


class TransparenzregisterReport(BaseModel):
    """Parsed Transparenzregister extract report limited to UBO-relevant fields."""

    created_at: Optional[date] = None
    """Extract creation date."""

    fictional_ubo_reason: Optional[str] = None
    """Reason indicating no natural person UBO could be determined."""

    groups: Optional[List[TransparenzregisterGroup]] = None

    notice_type: Optional[str] = None
    """Type of Transparenzregister notice."""

    status_flags: Optional[TransparenzregisterStatusFlags] = None

    ubos: Optional[List[TransparenzregisterUbo]] = None

    validity: Optional[TransparenzregisterValidity] = None
