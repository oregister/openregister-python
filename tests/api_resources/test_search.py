# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types import (
    CompanySearch,
    SearchFindPersonV1Response,
    SearchLookupCompanyByURLResponse,
    SearchAutocompleteCompaniesV1Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_autocomplete_companies_v1(self, client: Openregister) -> None:
        search = client.search.autocomplete_companies_v1(
            query="query",
        )
        assert_matches_type(SearchAutocompleteCompaniesV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_autocomplete_companies_v1(self, client: Openregister) -> None:
        response = client.search.with_raw_response.autocomplete_companies_v1(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchAutocompleteCompaniesV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete_companies_v1(self, client: Openregister) -> None:
        with client.search.with_streaming_response.autocomplete_companies_v1(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchAutocompleteCompaniesV1Response, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_find_companies_v0(self, client: Openregister) -> None:
        search = client.search.find_companies_v0()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_find_companies_v0_with_all_params(self, client: Openregister) -> None:
        search = client.search.find_companies_v0(
            active=True,
            incorporation_date="incorporation_date",
            legal_form="ag",
            page=0,
            per_page=0,
            query="query",
            register_court="register_court",
            register_number="register_number",
            register_type="HRB",
        )
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_find_companies_v0(self, client: Openregister) -> None:
        response = client.search.with_raw_response.find_companies_v0()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_find_companies_v0(self, client: Openregister) -> None:
        with client.search.with_streaming_response.find_companies_v0() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(CompanySearch, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_find_companies_v1(self, client: Openregister) -> None:
        search = client.search.find_companies_v1()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_find_companies_v1_with_all_params(self, client: Openregister) -> None:
        search = client.search.find_companies_v1(
            filters=[
                {
                    "field": "status",
                    "keywords": ["string"],
                    "max": "max",
                    "min": "min",
                    "value": "value",
                    "values": ["string"],
                }
            ],
            location={
                "latitude": 0,
                "longitude": 0,
                "radius": 0,
            },
            pagination={
                "page": 0,
                "per_page": 0,
            },
            query={"value": "value"},
        )
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_find_companies_v1(self, client: Openregister) -> None:
        response = client.search.with_raw_response.find_companies_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_find_companies_v1(self, client: Openregister) -> None:
        with client.search.with_streaming_response.find_companies_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(CompanySearch, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_find_person_v1(self, client: Openregister) -> None:
        search = client.search.find_person_v1()
        assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_find_person_v1_with_all_params(self, client: Openregister) -> None:
        search = client.search.find_person_v1(
            filters=[
                {
                    "field": "date_of_birth",
                    "keywords": ["string"],
                    "max": "max",
                    "min": "min",
                    "value": "value",
                    "values": ["string"],
                }
            ],
            pagination={
                "page": 0,
                "per_page": 0,
            },
            query={"value": "value"},
        )
        assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_find_person_v1(self, client: Openregister) -> None:
        response = client.search.with_raw_response.find_person_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_find_person_v1(self, client: Openregister) -> None:
        with client.search.with_streaming_response.find_person_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_lookup_company_by_url(self, client: Openregister) -> None:
        search = client.search.lookup_company_by_url(
            url="https://example.com",
        )
        assert_matches_type(SearchLookupCompanyByURLResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_lookup_company_by_url(self, client: Openregister) -> None:
        response = client.search.with_raw_response.lookup_company_by_url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchLookupCompanyByURLResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_lookup_company_by_url(self, client: Openregister) -> None:
        with client.search.with_streaming_response.lookup_company_by_url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchLookupCompanyByURLResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_autocomplete_companies_v1(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.autocomplete_companies_v1(
            query="query",
        )
        assert_matches_type(SearchAutocompleteCompaniesV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete_companies_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.search.with_raw_response.autocomplete_companies_v1(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchAutocompleteCompaniesV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete_companies_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.search.with_streaming_response.autocomplete_companies_v1(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchAutocompleteCompaniesV1Response, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_find_companies_v0(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.find_companies_v0()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_find_companies_v0_with_all_params(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.find_companies_v0(
            active=True,
            incorporation_date="incorporation_date",
            legal_form="ag",
            page=0,
            per_page=0,
            query="query",
            register_court="register_court",
            register_number="register_number",
            register_type="HRB",
        )
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_find_companies_v0(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.search.with_raw_response.find_companies_v0()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_find_companies_v0(self, async_client: AsyncOpenregister) -> None:
        async with async_client.search.with_streaming_response.find_companies_v0() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(CompanySearch, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_find_companies_v1(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.find_companies_v1()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_find_companies_v1_with_all_params(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.find_companies_v1(
            filters=[
                {
                    "field": "status",
                    "keywords": ["string"],
                    "max": "max",
                    "min": "min",
                    "value": "value",
                    "values": ["string"],
                }
            ],
            location={
                "latitude": 0,
                "longitude": 0,
                "radius": 0,
            },
            pagination={
                "page": 0,
                "per_page": 0,
            },
            query={"value": "value"},
        )
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_find_companies_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.search.with_raw_response.find_companies_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(CompanySearch, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_find_companies_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.search.with_streaming_response.find_companies_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(CompanySearch, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_find_person_v1(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.find_person_v1()
        assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_find_person_v1_with_all_params(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.find_person_v1(
            filters=[
                {
                    "field": "date_of_birth",
                    "keywords": ["string"],
                    "max": "max",
                    "min": "min",
                    "value": "value",
                    "values": ["string"],
                }
            ],
            pagination={
                "page": 0,
                "per_page": 0,
            },
            query={"value": "value"},
        )
        assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_find_person_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.search.with_raw_response.find_person_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_find_person_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.search.with_streaming_response.find_person_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchFindPersonV1Response, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_lookup_company_by_url(self, async_client: AsyncOpenregister) -> None:
        search = await async_client.search.lookup_company_by_url(
            url="https://example.com",
        )
        assert_matches_type(SearchLookupCompanyByURLResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_lookup_company_by_url(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.search.with_raw_response.lookup_company_by_url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchLookupCompanyByURLResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_lookup_company_by_url(self, async_client: AsyncOpenregister) -> None:
        async with async_client.search.with_streaming_response.lookup_company_by_url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchLookupCompanyByURLResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
