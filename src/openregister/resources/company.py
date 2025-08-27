# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import company_get_owners_v1_params, company_get_details_v1_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.company_get_owners_v1_response import CompanyGetOwnersV1Response
from ..types.company_get_contact_v0_response import CompanyGetContactV0Response
from ..types.company_get_details_v1_response import CompanyGetDetailsV1Response
from ..types.company_get_holdings_v1_response import CompanyGetHoldingsV1Response
from ..types.company_get_financials_v1_response import CompanyGetFinancialsV1Response

__all__ = ["CompanyResource", "AsyncCompanyResource"]


class CompanyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompanyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return CompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return CompanyResourceWithStreamingResponse(self)

    def get_contact_v0(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetContactV0Response:
        """
        Get company contact information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/v0/company/{company_id}/contact",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetContactV0Response,
        )

    def get_details_v1(
        self,
        company_id: str,
        *,
        realtime: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetDetailsV1Response:
        """
        Get detailed company information

        Args:
          realtime: Get the most up-to-date company information directly from the Handelsregister.
              When set to true, we fetch the latest data in real-time from the official German
              commercial register, ensuring you receive the most current company details.
              Note: Real-time requests take longer but guarantee the freshest data available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/v1/company/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"realtime": realtime}, company_get_details_v1_params.CompanyGetDetailsV1Params),
            ),
            cast_to=CompanyGetDetailsV1Response,
        )

    def get_financials_v1(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetFinancialsV1Response:
        """
        Get financial reports

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/v1/company/{company_id}/financials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetFinancialsV1Response,
        )

    def get_holdings_v1(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetHoldingsV1Response:
        """
        Get company holdings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/v1/company/{company_id}/holdings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetHoldingsV1Response,
        )

    def get_owners_v1(
        self,
        company_id: str,
        *,
        realtime: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetOwnersV1Response:
        """
        Get company owners

        Args:
          realtime: Get the most up-to-date company information directly from the Handelsregister.
              When set to true, we fetch the latest data in real-time from the official German
              commercial register, ensuring you receive the most current company details.
              Note: Real-time requests take longer but guarantee the freshest data available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/v1/company/{company_id}/owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"realtime": realtime}, company_get_owners_v1_params.CompanyGetOwnersV1Params),
            ),
            cast_to=CompanyGetOwnersV1Response,
        )


class AsyncCompanyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompanyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncCompanyResourceWithStreamingResponse(self)

    async def get_contact_v0(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetContactV0Response:
        """
        Get company contact information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/v0/company/{company_id}/contact",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetContactV0Response,
        )

    async def get_details_v1(
        self,
        company_id: str,
        *,
        realtime: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetDetailsV1Response:
        """
        Get detailed company information

        Args:
          realtime: Get the most up-to-date company information directly from the Handelsregister.
              When set to true, we fetch the latest data in real-time from the official German
              commercial register, ensuring you receive the most current company details.
              Note: Real-time requests take longer but guarantee the freshest data available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/v1/company/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"realtime": realtime}, company_get_details_v1_params.CompanyGetDetailsV1Params
                ),
            ),
            cast_to=CompanyGetDetailsV1Response,
        )

    async def get_financials_v1(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetFinancialsV1Response:
        """
        Get financial reports

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/v1/company/{company_id}/financials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetFinancialsV1Response,
        )

    async def get_holdings_v1(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetHoldingsV1Response:
        """
        Get company holdings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/v1/company/{company_id}/holdings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyGetHoldingsV1Response,
        )

    async def get_owners_v1(
        self,
        company_id: str,
        *,
        realtime: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyGetOwnersV1Response:
        """
        Get company owners

        Args:
          realtime: Get the most up-to-date company information directly from the Handelsregister.
              When set to true, we fetch the latest data in real-time from the official German
              commercial register, ensuring you receive the most current company details.
              Note: Real-time requests take longer but guarantee the freshest data available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/v1/company/{company_id}/owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"realtime": realtime}, company_get_owners_v1_params.CompanyGetOwnersV1Params
                ),
            ),
            cast_to=CompanyGetOwnersV1Response,
        )


class CompanyResourceWithRawResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.get_contact_v0 = to_raw_response_wrapper(
            company.get_contact_v0,
        )
        self.get_details_v1 = to_raw_response_wrapper(
            company.get_details_v1,
        )
        self.get_financials_v1 = to_raw_response_wrapper(
            company.get_financials_v1,
        )
        self.get_holdings_v1 = to_raw_response_wrapper(
            company.get_holdings_v1,
        )
        self.get_owners_v1 = to_raw_response_wrapper(
            company.get_owners_v1,
        )


class AsyncCompanyResourceWithRawResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.get_contact_v0 = async_to_raw_response_wrapper(
            company.get_contact_v0,
        )
        self.get_details_v1 = async_to_raw_response_wrapper(
            company.get_details_v1,
        )
        self.get_financials_v1 = async_to_raw_response_wrapper(
            company.get_financials_v1,
        )
        self.get_holdings_v1 = async_to_raw_response_wrapper(
            company.get_holdings_v1,
        )
        self.get_owners_v1 = async_to_raw_response_wrapper(
            company.get_owners_v1,
        )


class CompanyResourceWithStreamingResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.get_contact_v0 = to_streamed_response_wrapper(
            company.get_contact_v0,
        )
        self.get_details_v1 = to_streamed_response_wrapper(
            company.get_details_v1,
        )
        self.get_financials_v1 = to_streamed_response_wrapper(
            company.get_financials_v1,
        )
        self.get_holdings_v1 = to_streamed_response_wrapper(
            company.get_holdings_v1,
        )
        self.get_owners_v1 = to_streamed_response_wrapper(
            company.get_owners_v1,
        )


class AsyncCompanyResourceWithStreamingResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.get_contact_v0 = async_to_streamed_response_wrapper(
            company.get_contact_v0,
        )
        self.get_details_v1 = async_to_streamed_response_wrapper(
            company.get_details_v1,
        )
        self.get_financials_v1 = async_to_streamed_response_wrapper(
            company.get_financials_v1,
        )
        self.get_holdings_v1 = async_to_streamed_response_wrapper(
            company.get_holdings_v1,
        )
        self.get_owners_v1 = async_to_streamed_response_wrapper(
            company.get_owners_v1,
        )
