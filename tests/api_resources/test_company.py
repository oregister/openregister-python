# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types import (
    CompanyGetOwnersV1Response,
    CompanyGetContactV0Response,
    CompanyGetDetailsV1Response,
    CompanyGetHoldingsV1Response,
    CompanyGetFinancialsV1Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompany:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_contact_v0(self, client: Openregister) -> None:
        company = client.company.get_contact_v0(
            "company_id",
        )
        assert_matches_type(CompanyGetContactV0Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_contact_v0(self, client: Openregister) -> None:
        response = client.company.with_raw_response.get_contact_v0(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyGetContactV0Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_contact_v0(self, client: Openregister) -> None:
        with client.company.with_streaming_response.get_contact_v0(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyGetContactV0Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_contact_v0(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.get_contact_v0(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_details_v1(self, client: Openregister) -> None:
        company = client.company.get_details_v1(
            company_id="company_id",
        )
        assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_details_v1_with_all_params(self, client: Openregister) -> None:
        company = client.company.get_details_v1(
            company_id="company_id",
            realtime=True,
        )
        assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_details_v1(self, client: Openregister) -> None:
        response = client.company.with_raw_response.get_details_v1(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_details_v1(self, client: Openregister) -> None:
        with client.company.with_streaming_response.get_details_v1(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_details_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.get_details_v1(
                company_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_financials_v1(self, client: Openregister) -> None:
        company = client.company.get_financials_v1(
            "company_id",
        )
        assert_matches_type(CompanyGetFinancialsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_financials_v1(self, client: Openregister) -> None:
        response = client.company.with_raw_response.get_financials_v1(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyGetFinancialsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_financials_v1(self, client: Openregister) -> None:
        with client.company.with_streaming_response.get_financials_v1(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyGetFinancialsV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_financials_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.get_financials_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_holdings_v1(self, client: Openregister) -> None:
        company = client.company.get_holdings_v1(
            "company_id",
        )
        assert_matches_type(CompanyGetHoldingsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_holdings_v1(self, client: Openregister) -> None:
        response = client.company.with_raw_response.get_holdings_v1(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyGetHoldingsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_holdings_v1(self, client: Openregister) -> None:
        with client.company.with_streaming_response.get_holdings_v1(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyGetHoldingsV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_holdings_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.get_holdings_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_owners_v1(self, client: Openregister) -> None:
        company = client.company.get_owners_v1(
            company_id="company_id",
        )
        assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_owners_v1_with_all_params(self, client: Openregister) -> None:
        company = client.company.get_owners_v1(
            company_id="company_id",
            realtime=True,
        )
        assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_owners_v1(self, client: Openregister) -> None:
        response = client.company.with_raw_response.get_owners_v1(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_owners_v1(self, client: Openregister) -> None:
        with client.company.with_streaming_response.get_owners_v1(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_owners_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.company.with_raw_response.get_owners_v1(
                company_id="",
            )


class TestAsyncCompany:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_contact_v0(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.get_contact_v0(
            "company_id",
        )
        assert_matches_type(CompanyGetContactV0Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_contact_v0(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.get_contact_v0(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyGetContactV0Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_contact_v0(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.get_contact_v0(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyGetContactV0Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_contact_v0(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.get_contact_v0(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.get_details_v1(
            company_id="company_id",
        )
        assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_details_v1_with_all_params(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.get_details_v1(
            company_id="company_id",
            realtime=True,
        )
        assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.get_details_v1(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.get_details_v1(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyGetDetailsV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.get_details_v1(
                company_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_financials_v1(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.get_financials_v1(
            "company_id",
        )
        assert_matches_type(CompanyGetFinancialsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_financials_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.get_financials_v1(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyGetFinancialsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_financials_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.get_financials_v1(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyGetFinancialsV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_financials_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.get_financials_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.get_holdings_v1(
            "company_id",
        )
        assert_matches_type(CompanyGetHoldingsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.get_holdings_v1(
            "company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyGetHoldingsV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.get_holdings_v1(
            "company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyGetHoldingsV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.get_holdings_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_owners_v1(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.get_owners_v1(
            company_id="company_id",
        )
        assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_owners_v1_with_all_params(self, async_client: AsyncOpenregister) -> None:
        company = await async_client.company.get_owners_v1(
            company_id="company_id",
            realtime=True,
        )
        assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_owners_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.company.with_raw_response.get_owners_v1(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_owners_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.company.with_streaming_response.get_owners_v1(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyGetOwnersV1Response, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_owners_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.company.with_raw_response.get_owners_v1(
                company_id="",
            )
