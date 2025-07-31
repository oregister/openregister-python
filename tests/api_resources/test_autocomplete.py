# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types import (
    AutocompleteAutocompleteCompaniesV1Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutocomplete:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_autocomplete_companies_v1(self, client: Openregister) -> None:
        autocomplete = client.autocomplete.autocomplete_companies_v1(
            query="query",
        )
        assert_matches_type(AutocompleteAutocompleteCompaniesV1Response, autocomplete, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_autocomplete_companies_v1(self, client: Openregister) -> None:
        response = client.autocomplete.with_raw_response.autocomplete_companies_v1(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteAutocompleteCompaniesV1Response, autocomplete, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_autocomplete_companies_v1(self, client: Openregister) -> None:
        with client.autocomplete.with_streaming_response.autocomplete_companies_v1(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteAutocompleteCompaniesV1Response, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutocomplete:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_autocomplete_companies_v1(self, async_client: AsyncOpenregister) -> None:
        autocomplete = await async_client.autocomplete.autocomplete_companies_v1(
            query="query",
        )
        assert_matches_type(AutocompleteAutocompleteCompaniesV1Response, autocomplete, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_autocomplete_companies_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.autocomplete.with_raw_response.autocomplete_companies_v1(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteAutocompleteCompaniesV1Response, autocomplete, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_autocomplete_companies_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.autocomplete.with_streaming_response.autocomplete_companies_v1(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteAutocompleteCompaniesV1Response, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True
