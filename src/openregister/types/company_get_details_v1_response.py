# Deprecated module kept so existing imports keep working. Use `company_v1` instead.

from .company_v1 import (
    Contact as Contact,
    CompanyV1,
    Estimates as Estimates,
    Indicator as Indicator,
    Insolvency as Insolvency,
    MergedInto as MergedInto,
    Acquisition as Acquisition,
    AssetSpinOff as AssetSpinOff,
    IndustryCodes as IndustryCodes,
    Representation as Representation,
    EstimatesEbitda as EstimatesEbitda,
    EstimatesRevenue as EstimatesRevenue,
    ContactSocialMedia as ContactSocialMedia,
    EstimatesEmployees as EstimatesEmployees,
    IndustryCodesWz2025 as IndustryCodesWz2025,
    ProfitTransferAgreement as ProfitTransferAgreement,
    RepresentationRoleDetail as RepresentationRoleDetail,
    RepresentationLegalPerson as RepresentationLegalPerson,
    IndustryCodesWz2025Subclass as IndustryCodesWz2025Subclass,
    RepresentationNaturalPerson as RepresentationNaturalPerson,
    RepresentationAuthorityDetail as RepresentationAuthorityDetail,
)

__all__ = ["CompanyGetDetailsV1Response", "Acquisition", "AssetSpinOff", "Contact", "ContactSocialMedia", "Estimates", "EstimatesEbitda", "EstimatesEmployees", "EstimatesRevenue", "Indicator", "IndustryCodes", "IndustryCodesWz2025", "IndustryCodesWz2025Subclass", "MergedInto", "ProfitTransferAgreement", "Representation", "RepresentationAuthorityDetail", "RepresentationRoleDetail", "RepresentationLegalPerson", "RepresentationNaturalPerson", "Insolvency"]

CompanyGetDetailsV1Response = CompanyV1
"""Deprecated: use `CompanyV1`."""
