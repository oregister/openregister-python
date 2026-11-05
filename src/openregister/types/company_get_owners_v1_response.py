# Deprecated module kept so existing imports keep working. Use `company_owners` instead.

from .company_owners import (
    Owner as Owner,
    CompanyOwners,
    OwnerRoleDetail as OwnerRoleDetail,
)

__all__ = ["CompanyGetOwnersV1Response", "Owner", "OwnerRoleDetail"]

CompanyGetOwnersV1Response = CompanyOwners
"""Deprecated: use `CompanyOwners`."""
