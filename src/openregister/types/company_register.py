# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .company_register_type import CompanyRegisterType

__all__ = ["CompanyRegister"]


class CompanyRegister(BaseModel):
    register_court: str
    """Court where the company is registered. Example: "Berlin (Charlottenburg)" """

    register_number: str
    """Registration number in the company register. Example: "230633" """

    register_type: CompanyRegisterType
    """
    Type of register where the company is recorded. Example: "HRB" (Commercial
    Register B)
    """

    company_id: Optional[str] = None
    """Unique company identifier. Example: DE-HRB-F1103-267645"""

    start_date: Optional[str] = None
    """
    Date when this registration information became effective. Format: ISO 8601
    (YYYY-MM-DD) Example: "2022-01-01"
    """
