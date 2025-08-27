# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.person_get_details_v1_response import PersonGetDetailsV1Response
from ..types.person_get_holdings_v1_response import PersonGetHoldingsV1Response

__all__ = ["PersonResource", "AsyncPersonResource"]


class PersonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return PersonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return PersonResourceWithStreamingResponse(self)

    def get_details_v1(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonGetDetailsV1Response:
        """
        Get detailed person information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return self._get(
            f"/v1/person/{person_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonGetDetailsV1Response,
        )

    def get_holdings_v1(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonGetHoldingsV1Response:
        """
        Get person holdings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return self._get(
            f"/v1/person/{person_id}/holdings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonGetHoldingsV1Response,
        )


class AsyncPersonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/oregister/openregister-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/oregister/openregister-python#with_streaming_response
        """
        return AsyncPersonResourceWithStreamingResponse(self)

    async def get_details_v1(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonGetDetailsV1Response:
        """
        Get detailed person information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return await self._get(
            f"/v1/person/{person_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonGetDetailsV1Response,
        )

    async def get_holdings_v1(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonGetHoldingsV1Response:
        """
        Get person holdings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return await self._get(
            f"/v1/person/{person_id}/holdings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonGetHoldingsV1Response,
        )


class PersonResourceWithRawResponse:
    def __init__(self, person: PersonResource) -> None:
        self._person = person

        self.get_details_v1 = to_raw_response_wrapper(
            person.get_details_v1,
        )
        self.get_holdings_v1 = to_raw_response_wrapper(
            person.get_holdings_v1,
        )


class AsyncPersonResourceWithRawResponse:
    def __init__(self, person: AsyncPersonResource) -> None:
        self._person = person

        self.get_details_v1 = async_to_raw_response_wrapper(
            person.get_details_v1,
        )
        self.get_holdings_v1 = async_to_raw_response_wrapper(
            person.get_holdings_v1,
        )


class PersonResourceWithStreamingResponse:
    def __init__(self, person: PersonResource) -> None:
        self._person = person

        self.get_details_v1 = to_streamed_response_wrapper(
            person.get_details_v1,
        )
        self.get_holdings_v1 = to_streamed_response_wrapper(
            person.get_holdings_v1,
        )


class AsyncPersonResourceWithStreamingResponse:
    def __init__(self, person: AsyncPersonResource) -> None:
        self._person = person

        self.get_details_v1 = async_to_streamed_response_wrapper(
            person.get_details_v1,
        )
        self.get_holdings_v1 = async_to_streamed_response_wrapper(
            person.get_holdings_v1,
        )
