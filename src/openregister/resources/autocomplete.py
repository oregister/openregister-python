# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import autocomplete_autocomplete_companies_v1_params
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
from ..types.autocomplete_autocomplete_companies_v1_response import AutocompleteAutocompleteCompaniesV1Response

__all__ = ["AutocompleteResource", "AsyncAutocompleteResource"]


class AutocompleteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutocompleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AutocompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutocompleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AutocompleteResourceWithStreamingResponse(self)

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
    ) -> AutocompleteAutocompleteCompaniesV1Response:
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
                    {"query": query},
                    autocomplete_autocomplete_companies_v1_params.AutocompleteAutocompleteCompaniesV1Params,
                ),
            ),
            cast_to=AutocompleteAutocompleteCompaniesV1Response,
        )


class AsyncAutocompleteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutocompleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutocompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutocompleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncAutocompleteResourceWithStreamingResponse(self)

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
    ) -> AutocompleteAutocompleteCompaniesV1Response:
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
                    {"query": query},
                    autocomplete_autocomplete_companies_v1_params.AutocompleteAutocompleteCompaniesV1Params,
                ),
            ),
            cast_to=AutocompleteAutocompleteCompaniesV1Response,
        )


class AutocompleteResourceWithRawResponse:
    def __init__(self, autocomplete: AutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.autocomplete_companies_v1 = to_raw_response_wrapper(
            autocomplete.autocomplete_companies_v1,
        )


class AsyncAutocompleteResourceWithRawResponse:
    def __init__(self, autocomplete: AsyncAutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.autocomplete_companies_v1 = async_to_raw_response_wrapper(
            autocomplete.autocomplete_companies_v1,
        )


class AutocompleteResourceWithStreamingResponse:
    def __init__(self, autocomplete: AutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.autocomplete_companies_v1 = to_streamed_response_wrapper(
            autocomplete.autocomplete_companies_v1,
        )


class AsyncAutocompleteResourceWithStreamingResponse:
    def __init__(self, autocomplete: AsyncAutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.autocomplete_companies_v1 = async_to_streamed_response_wrapper(
            autocomplete.autocomplete_companies_v1,
        )
