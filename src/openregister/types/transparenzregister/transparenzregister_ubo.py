# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .transparenzregister_ubo_interest import TransparenzregisterUboInterest
from .transparenzregister_ubo_natural_person import TransparenzregisterUboNaturalPerson

__all__ = ["TransparenzregisterUbo"]


class TransparenzregisterUbo(BaseModel):
    interest: Optional[TransparenzregisterUboInterest] = None

    natural_person: Optional[TransparenzregisterUboNaturalPerson] = None

    position: Optional[int] = None
