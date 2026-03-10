# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .company_owner_legal_person import CompanyOwnerLegalPerson
from .company_owner_natural_person import CompanyOwnerNaturalPerson

__all__ = ["CompanyGetUbosV1Response", "Ubo"]


class Ubo(BaseModel):
    id: Optional[str] = None
    """
    Unique identifier for the shareholder. For individuals: UUID For companies:
    Format matches company_id pattern Example: "DE-HRB-F1103-267645" or UUID May be
    null for certain shareholders.
    """

    legal_person: Optional[CompanyOwnerLegalPerson] = None

    max_percentage_share: Optional[float] = None
    """
    Maximum percentage of company ownership. Example: 5.36 represents maximum of
    5.36% ownership There is no exact percentage share for owners that hold a stake
    as or through a limited partner. For these owners, we can only show the maximum
    percentage share they could have based on their deposit as a limited partner. Is
    null for all owners that have an exact percentage share or owners that hold a
    stake as or through a personal liable director.
    """

    name: str
    """The name of the shareholder. E.g. "Max Mustermann" """

    natural_person: Optional[CompanyOwnerNaturalPerson] = None

    percentage_share: Optional[float] = None
    """
    Percentage of company ownership. Example: 5.36 represents 5.36% ownership Is
    null for all owners that hold a stake as or through a personal liable directors
    or limited partner.
    """


class CompanyGetUbosV1Response(BaseModel):
    company_id: str
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    ubos: List[Ubo]
