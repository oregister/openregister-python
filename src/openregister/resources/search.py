# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    CompanyLegalForm,
    CompanyRegisterType,
    search_find_person_v1_params,
    search_find_companies_v0_params,
    search_find_companies_v1_params,
    search_lookup_company_by_url_params,
    search_autocomplete_companies_v1_params,
)
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
from ..types.company_search import CompanySearch
from ..types.company_legal_form import CompanyLegalForm
from ..types.company_register_type import CompanyRegisterType
from ..types.search_find_person_v1_response import SearchFindPersonV1Response
from ..types.search_lookup_company_by_url_response import SearchLookupCompanyByURLResponse
from ..types.search_autocomplete_companies_v1_response import SearchAutocompleteCompaniesV1Response

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def autocomplete_companies_v1(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchAutocompleteCompaniesV1Response:
        """
        Autocomplete company search

        Args:
          query: Text search query to find companies by name. Example: "Descartes Technologies
              UG"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/autocomplete/company",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"query": query}, search_autocomplete_companies_v1_params.SearchAutocompleteCompaniesV1Params
                ),
            ),
            cast_to=SearchAutocompleteCompaniesV1Response,
        )

    def find_companies_v0(
        self,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        incorporation_date: str | NotGiven = NOT_GIVEN,
        legal_form: CompanyLegalForm | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        register_court: str | NotGiven = NOT_GIVEN,
        register_number: str | NotGiven = NOT_GIVEN,
        register_type: CompanyRegisterType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanySearch:
        """Search for companies

        Args:
          active: Filter for active or inactive companies.

        Set to true for active companies only,
              false for inactive only.

          incorporation_date:
              Date of incorporation of the company. Format: ISO 8601 (YYYY-MM-DD) Example:
              "2022-01-01"

          legal_form: Legal form of the company. Example: "gmbh" for "Gesellschaft mit beschränkter
              Haftung"

          page: Page number for pagination.

          per_page: Number of results per page (max 50).

          query: Text search query to find companies by name. Example: "Descartes Technologies
              UG"

          register_court: Court where the company is registered. Example: "Berlin (Charlottenburg)"

          register_number: Company register number for exact matching. Example: "230633"

          register_type: Type of register to filter results. Example: "HRB" (Commercial Register B)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v0/search/company",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "incorporation_date": incorporation_date,
                        "legal_form": legal_form,
                        "page": page,
                        "per_page": per_page,
                        "query": query,
                        "register_court": register_court,
                        "register_number": register_number,
                        "register_type": register_type,
                    },
                    search_find_companies_v0_params.SearchFindCompaniesV0Params,
                ),
            ),
            cast_to=CompanySearch,
        )

    def find_companies_v1(
        self,
        *,
        filters: Iterable[search_find_companies_v1_params.Filter] | NotGiven = NOT_GIVEN,
        location: search_find_companies_v1_params.Location | NotGiven = NOT_GIVEN,
        pagination: search_find_companies_v1_params.Pagination | NotGiven = NOT_GIVEN,
        query: search_find_companies_v1_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanySearch:
        """
        Search for companies

        Args:
          filters: Filters to filter companies.

          location: Location to filter companies.

          pagination: Pagination parameters.

          query: Search query to filter companies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/search/company",
            body=maybe_transform(
                {
                    "filters": filters,
                    "location": location,
                    "pagination": pagination,
                    "query": query,
                },
                search_find_companies_v1_params.SearchFindCompaniesV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanySearch,
        )

    def find_person_v1(
        self,
        *,
        filters: Iterable[search_find_person_v1_params.Filter] | NotGiven = NOT_GIVEN,
        pagination: search_find_person_v1_params.Pagination | NotGiven = NOT_GIVEN,
        query: search_find_person_v1_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchFindPersonV1Response:
        """
        Search for people

        Args:
          filters: Filters to filter people.

          pagination: Pagination parameters.

          query: Search query to filter people.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/search/person",
            body=maybe_transform(
                {
                    "filters": filters,
                    "pagination": pagination,
                    "query": query,
                },
                search_find_person_v1_params.SearchFindPersonV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchFindPersonV1Response,
        )

    def lookup_company_by_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchLookupCompanyByURLResponse:
        """Find company by website URL

        Args:
          url: Website URL to search for.

        Example: "https://openregister.de"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v0/search/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, search_lookup_company_by_url_params.SearchLookupCompanyByURLParams),
            ),
            cast_to=SearchLookupCompanyByURLResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def autocomplete_companies_v1(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchAutocompleteCompaniesV1Response:
        """
        Autocomplete company search

        Args:
          query: Text search query to find companies by name. Example: "Descartes Technologies
              UG"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/autocomplete/company",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query": query}, search_autocomplete_companies_v1_params.SearchAutocompleteCompaniesV1Params
                ),
            ),
            cast_to=SearchAutocompleteCompaniesV1Response,
        )

    async def find_companies_v0(
        self,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        incorporation_date: str | NotGiven = NOT_GIVEN,
        legal_form: CompanyLegalForm | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        register_court: str | NotGiven = NOT_GIVEN,
        register_number: str | NotGiven = NOT_GIVEN,
        register_type: CompanyRegisterType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanySearch:
        """Search for companies

        Args:
          active: Filter for active or inactive companies.

        Set to true for active companies only,
              false for inactive only.

          incorporation_date:
              Date of incorporation of the company. Format: ISO 8601 (YYYY-MM-DD) Example:
              "2022-01-01"

          legal_form: Legal form of the company. Example: "gmbh" for "Gesellschaft mit beschränkter
              Haftung"

          page: Page number for pagination.

          per_page: Number of results per page (max 50).

          query: Text search query to find companies by name. Example: "Descartes Technologies
              UG"

          register_court: Court where the company is registered. Example: "Berlin (Charlottenburg)"

          register_number: Company register number for exact matching. Example: "230633"

          register_type: Type of register to filter results. Example: "HRB" (Commercial Register B)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v0/search/company",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "incorporation_date": incorporation_date,
                        "legal_form": legal_form,
                        "page": page,
                        "per_page": per_page,
                        "query": query,
                        "register_court": register_court,
                        "register_number": register_number,
                        "register_type": register_type,
                    },
                    search_find_companies_v0_params.SearchFindCompaniesV0Params,
                ),
            ),
            cast_to=CompanySearch,
        )

    async def find_companies_v1(
        self,
        *,
        filters: Iterable[search_find_companies_v1_params.Filter] | NotGiven = NOT_GIVEN,
        location: search_find_companies_v1_params.Location | NotGiven = NOT_GIVEN,
        pagination: search_find_companies_v1_params.Pagination | NotGiven = NOT_GIVEN,
        query: search_find_companies_v1_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanySearch:
        """
        Search for companies

        Args:
          filters: Filters to filter companies.

          location: Location to filter companies.

          pagination: Pagination parameters.

          query: Search query to filter companies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/search/company",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "location": location,
                    "pagination": pagination,
                    "query": query,
                },
                search_find_companies_v1_params.SearchFindCompaniesV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanySearch,
        )

    async def find_person_v1(
        self,
        *,
        filters: Iterable[search_find_person_v1_params.Filter] | NotGiven = NOT_GIVEN,
        pagination: search_find_person_v1_params.Pagination | NotGiven = NOT_GIVEN,
        query: search_find_person_v1_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchFindPersonV1Response:
        """
        Search for people

        Args:
          filters: Filters to filter people.

          pagination: Pagination parameters.

          query: Search query to filter people.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/search/person",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "pagination": pagination,
                    "query": query,
                },
                search_find_person_v1_params.SearchFindPersonV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchFindPersonV1Response,
        )

    async def lookup_company_by_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchLookupCompanyByURLResponse:
        """Find company by website URL

        Args:
          url: Website URL to search for.

        Example: "https://openregister.de"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v0/search/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"url": url}, search_lookup_company_by_url_params.SearchLookupCompanyByURLParams
                ),
            ),
            cast_to=SearchLookupCompanyByURLResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.autocomplete_companies_v1 = to_raw_response_wrapper(
            search.autocomplete_companies_v1,
        )
        self.find_companies_v0 = to_raw_response_wrapper(
            search.find_companies_v0,
        )
        self.find_companies_v1 = to_raw_response_wrapper(
            search.find_companies_v1,
        )
        self.find_person_v1 = to_raw_response_wrapper(
            search.find_person_v1,
        )
        self.lookup_company_by_url = to_raw_response_wrapper(
            search.lookup_company_by_url,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.autocomplete_companies_v1 = async_to_raw_response_wrapper(
            search.autocomplete_companies_v1,
        )
        self.find_companies_v0 = async_to_raw_response_wrapper(
            search.find_companies_v0,
        )
        self.find_companies_v1 = async_to_raw_response_wrapper(
            search.find_companies_v1,
        )
        self.find_person_v1 = async_to_raw_response_wrapper(
            search.find_person_v1,
        )
        self.lookup_company_by_url = async_to_raw_response_wrapper(
            search.lookup_company_by_url,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.autocomplete_companies_v1 = to_streamed_response_wrapper(
            search.autocomplete_companies_v1,
        )
        self.find_companies_v0 = to_streamed_response_wrapper(
            search.find_companies_v0,
        )
        self.find_companies_v1 = to_streamed_response_wrapper(
            search.find_companies_v1,
        )
        self.find_person_v1 = to_streamed_response_wrapper(
            search.find_person_v1,
        )
        self.lookup_company_by_url = to_streamed_response_wrapper(
            search.lookup_company_by_url,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.autocomplete_companies_v1 = async_to_streamed_response_wrapper(
            search.autocomplete_companies_v1,
        )
        self.find_companies_v0 = async_to_streamed_response_wrapper(
            search.find_companies_v0,
        )
        self.find_companies_v1 = async_to_streamed_response_wrapper(
            search.find_companies_v1,
        )
        self.find_person_v1 = async_to_streamed_response_wrapper(
            search.find_person_v1,
        )
        self.lookup_company_by_url = async_to_streamed_response_wrapper(
            search.lookup_company_by_url,
        )
