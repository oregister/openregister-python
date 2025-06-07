# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import company_retrieve_params
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
from ..types.company_retrieve_response import CompanyRetrieveResponse
from ..types.company_retrieve_contact_response import CompanyRetrieveContactResponse
from ..types.company_list_shareholders_response import CompanyListShareholdersResponse

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

    def retrieve(
        self,
        company_id: str,
        *,
        documents: bool | NotGiven = NOT_GIVEN,
        financials: bool | NotGiven = NOT_GIVEN,
        history: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveResponse:
        """
        Get detailed company information

        Args:
          documents: Include document metadata when set to true. Lists available official documents
              related to the company.

          financials: Include financial data when set to true. Provides access to financial reports
              and key financial indicators.

          history: Include historical company data when set to true. This returns past names,
              addresses, and other changed information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/v0/company/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "documents": documents,
                        "financials": financials,
                        "history": history,
                    },
                    company_retrieve_params.CompanyRetrieveParams,
                ),
            ),
            cast_to=CompanyRetrieveResponse,
        )

    def list_shareholders(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyListShareholdersResponse:
        """
        Get company shareholders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/v0/company/{company_id}/shareholders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyListShareholdersResponse,
        )

    def retrieve_contact(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveContactResponse:
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
            cast_to=CompanyRetrieveContactResponse,
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

    async def retrieve(
        self,
        company_id: str,
        *,
        documents: bool | NotGiven = NOT_GIVEN,
        financials: bool | NotGiven = NOT_GIVEN,
        history: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveResponse:
        """
        Get detailed company information

        Args:
          documents: Include document metadata when set to true. Lists available official documents
              related to the company.

          financials: Include financial data when set to true. Provides access to financial reports
              and key financial indicators.

          history: Include historical company data when set to true. This returns past names,
              addresses, and other changed information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/v0/company/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "documents": documents,
                        "financials": financials,
                        "history": history,
                    },
                    company_retrieve_params.CompanyRetrieveParams,
                ),
            ),
            cast_to=CompanyRetrieveResponse,
        )

    async def list_shareholders(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyListShareholdersResponse:
        """
        Get company shareholders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/v0/company/{company_id}/shareholders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyListShareholdersResponse,
        )

    async def retrieve_contact(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveContactResponse:
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
            cast_to=CompanyRetrieveContactResponse,
        )


class CompanyResourceWithRawResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.retrieve = to_raw_response_wrapper(
            company.retrieve,
        )
        self.list_shareholders = to_raw_response_wrapper(
            company.list_shareholders,
        )
        self.retrieve_contact = to_raw_response_wrapper(
            company.retrieve_contact,
        )


class AsyncCompanyResourceWithRawResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.retrieve = async_to_raw_response_wrapper(
            company.retrieve,
        )
        self.list_shareholders = async_to_raw_response_wrapper(
            company.list_shareholders,
        )
        self.retrieve_contact = async_to_raw_response_wrapper(
            company.retrieve_contact,
        )


class CompanyResourceWithStreamingResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.retrieve = to_streamed_response_wrapper(
            company.retrieve,
        )
        self.list_shareholders = to_streamed_response_wrapper(
            company.list_shareholders,
        )
        self.retrieve_contact = to_streamed_response_wrapper(
            company.retrieve_contact,
        )


class AsyncCompanyResourceWithStreamingResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.retrieve = async_to_streamed_response_wrapper(
            company.retrieve,
        )
        self.list_shareholders = async_to_streamed_response_wrapper(
            company.list_shareholders,
        )
        self.retrieve_contact = async_to_streamed_response_wrapper(
            company.retrieve_contact,
        )
