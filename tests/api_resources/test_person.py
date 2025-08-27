# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types import PersonGetDetailsV1Response, PersonGetHoldingsV1Response

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPerson:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_details_v1(self, client: Openregister) -> None:
        person = client.person.get_details_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PersonGetDetailsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_details_v1(self, client: Openregister) -> None:
        response = client.person.with_raw_response.get_details_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonGetDetailsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_details_v1(self, client: Openregister) -> None:
        with client.person.with_streaming_response.get_details_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonGetDetailsV1Response, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_details_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `person_id` but received ''"):
            client.person.with_raw_response.get_details_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_holdings_v1(self, client: Openregister) -> None:
        person = client.person.get_holdings_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PersonGetHoldingsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_holdings_v1(self, client: Openregister) -> None:
        response = client.person.with_raw_response.get_holdings_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonGetHoldingsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_holdings_v1(self, client: Openregister) -> None:
        with client.person.with_streaming_response.get_holdings_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonGetHoldingsV1Response, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_holdings_v1(self, client: Openregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `person_id` but received ''"):
            client.person.with_raw_response.get_holdings_v1(
                "",
            )


class TestAsyncPerson:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        person = await async_client.person.get_details_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PersonGetDetailsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.person.with_raw_response.get_details_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonGetDetailsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.person.with_streaming_response.get_details_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonGetDetailsV1Response, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_details_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `person_id` but received ''"):
            await async_client.person.with_raw_response.get_details_v1(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        person = await async_client.person.get_holdings_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PersonGetHoldingsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.person.with_raw_response.get_holdings_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonGetHoldingsV1Response, person, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.person.with_streaming_response.get_holdings_v1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonGetHoldingsV1Response, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_holdings_v1(self, async_client: AsyncOpenregister) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `person_id` but received ''"):
            await async_client.person.with_raw_response.get_holdings_v1(
                "",
            )
