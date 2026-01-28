# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, OpenregisterError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import person, search, company, document
    from .resources.person import PersonResource, AsyncPersonResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.company import CompanyResource, AsyncCompanyResource
    from .resources.document import DocumentResource, AsyncDocumentResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Openregister",
    "AsyncOpenregister",
    "Client",
    "AsyncClient",
]


class Openregister(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Openregister client instance.

        This automatically infers the `api_key` argument from the `OPENREGISTER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("OPENREGISTER_API_KEY")
        if api_key is None:
            raise OpenregisterError(
                "The api_key client option must be set either by passing api_key to the client or by setting the OPENREGISTER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("OPENREGISTER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openregister.de"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def company(self) -> CompanyResource:
        from .resources.company import CompanyResource

        return CompanyResource(self)

    @cached_property
    def document(self) -> DocumentResource:
        from .resources.document import DocumentResource

        return DocumentResource(self)

    @cached_property
    def person(self) -> PersonResource:
        from .resources.person import PersonResource

        return PersonResource(self)

    @cached_property
    def with_raw_response(self) -> OpenregisterWithRawResponse:
        return OpenregisterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenregisterWithStreamedResponse:
        return OpenregisterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOpenregister(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOpenregister client instance.

        This automatically infers the `api_key` argument from the `OPENREGISTER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("OPENREGISTER_API_KEY")
        if api_key is None:
            raise OpenregisterError(
                "The api_key client option must be set either by passing api_key to the client or by setting the OPENREGISTER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("OPENREGISTER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openregister.de"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def company(self) -> AsyncCompanyResource:
        from .resources.company import AsyncCompanyResource

        return AsyncCompanyResource(self)

    @cached_property
    def document(self) -> AsyncDocumentResource:
        from .resources.document import AsyncDocumentResource

        return AsyncDocumentResource(self)

    @cached_property
    def person(self) -> AsyncPersonResource:
        from .resources.person import AsyncPersonResource

        return AsyncPersonResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOpenregisterWithRawResponse:
        return AsyncOpenregisterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenregisterWithStreamedResponse:
        return AsyncOpenregisterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OpenregisterWithRawResponse:
    _client: Openregister

    def __init__(self, client: Openregister) -> None:
        self._client = client

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def company(self) -> company.CompanyResourceWithRawResponse:
        from .resources.company import CompanyResourceWithRawResponse

        return CompanyResourceWithRawResponse(self._client.company)

    @cached_property
    def document(self) -> document.DocumentResourceWithRawResponse:
        from .resources.document import DocumentResourceWithRawResponse

        return DocumentResourceWithRawResponse(self._client.document)

    @cached_property
    def person(self) -> person.PersonResourceWithRawResponse:
        from .resources.person import PersonResourceWithRawResponse

        return PersonResourceWithRawResponse(self._client.person)


class AsyncOpenregisterWithRawResponse:
    _client: AsyncOpenregister

    def __init__(self, client: AsyncOpenregister) -> None:
        self._client = client

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def company(self) -> company.AsyncCompanyResourceWithRawResponse:
        from .resources.company import AsyncCompanyResourceWithRawResponse

        return AsyncCompanyResourceWithRawResponse(self._client.company)

    @cached_property
    def document(self) -> document.AsyncDocumentResourceWithRawResponse:
        from .resources.document import AsyncDocumentResourceWithRawResponse

        return AsyncDocumentResourceWithRawResponse(self._client.document)

    @cached_property
    def person(self) -> person.AsyncPersonResourceWithRawResponse:
        from .resources.person import AsyncPersonResourceWithRawResponse

        return AsyncPersonResourceWithRawResponse(self._client.person)


class OpenregisterWithStreamedResponse:
    _client: Openregister

    def __init__(self, client: Openregister) -> None:
        self._client = client

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def company(self) -> company.CompanyResourceWithStreamingResponse:
        from .resources.company import CompanyResourceWithStreamingResponse

        return CompanyResourceWithStreamingResponse(self._client.company)

    @cached_property
    def document(self) -> document.DocumentResourceWithStreamingResponse:
        from .resources.document import DocumentResourceWithStreamingResponse

        return DocumentResourceWithStreamingResponse(self._client.document)

    @cached_property
    def person(self) -> person.PersonResourceWithStreamingResponse:
        from .resources.person import PersonResourceWithStreamingResponse

        return PersonResourceWithStreamingResponse(self._client.person)


class AsyncOpenregisterWithStreamedResponse:
    _client: AsyncOpenregister

    def __init__(self, client: AsyncOpenregister) -> None:
        self._client = client

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def company(self) -> company.AsyncCompanyResourceWithStreamingResponse:
        from .resources.company import AsyncCompanyResourceWithStreamingResponse

        return AsyncCompanyResourceWithStreamingResponse(self._client.company)

    @cached_property
    def document(self) -> document.AsyncDocumentResourceWithStreamingResponse:
        from .resources.document import AsyncDocumentResourceWithStreamingResponse

        return AsyncDocumentResourceWithStreamingResponse(self._client.document)

    @cached_property
    def person(self) -> person.AsyncPersonResourceWithStreamingResponse:
        from .resources.person import AsyncPersonResourceWithStreamingResponse

        return AsyncPersonResourceWithStreamingResponse(self._client.person)


Client = Openregister

AsyncClient = AsyncOpenregister
