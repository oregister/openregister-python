# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types import (
    CompanyRetrieveResponse,
    CompanyRetrieveContactResponse,
    CompanyListShareholdersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompany:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Openregister) -> None:
        company = client.company.retrieve(
            company_id="company_id",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Openregister) -> None:
        company = client.company.retrieve(
            company_id="company_id",
            documents=True,
            financials=True,
            history=True,
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Openregister) -> None:
        response = client.company.with_raw_response.retrieve(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Openregister) -> None:
        with client.company.with_streaming_response.retrieve(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.retrieve(
                company_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_shareholders(self, client: Openregister) -> None:
        company = client.company.list_shareholders(
            "company_id",
        )
        assert_matches_type(CompanyListShareholdersResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_shareholders(self, client: Openregister) -> None:
        response = client.company.with_raw_response.list_shareholders(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyListShareholdersResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_shareholders(self, client: Openregister) -> None:
        with client.company.with_streaming_response.list_shareholders(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyListShareholdersResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_shareholders(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.list_shareholders(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_contact(self, client: Openregister) -> None:
        company = client.company.retrieve_contact(
            "company_id",
        )
        assert_matches_type(CompanyRetrieveContactResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_contact(self, client: Openregister) -> None:
        response = client.company.with_raw_response.retrieve_contact(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveContactResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_contact(self, client: Openregister) -> None:
        with client.company.with_streaming_response.retrieve_contact(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveContactResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_contact(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.retrieve_contact(
                "",
            )


class TestAsyncCompany:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.retrieve(
            company_id="company_id",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.retrieve(
            company_id="company_id",
            documents=True,
            financials=True,
            history=True,
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.retrieve(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.retrieve(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.retrieve(
                company_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_shareholders(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.list_shareholders(
            "company_id",
        )
        assert_matches_type(CompanyListShareholdersResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_shareholders(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.list_shareholders(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyListShareholdersResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_shareholders(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.list_shareholders(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyListShareholdersResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_shareholders(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.list_shareholders(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_contact(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.retrieve_contact(
            "company_id",
        )
        assert_matches_type(CompanyRetrieveContactResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_contact(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.retrieve_contact(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveContactResponse, company, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_contact(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.retrieve_contact(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveContactResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_contact(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.retrieve_contact(
                "",
            )
