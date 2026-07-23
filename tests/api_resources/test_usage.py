# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from openregister import Openregister, AsyncOpenregister
from openregister.types import UsageGetCreditsV1Response

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_credits_v1(self, client: Openregister) -> None:
        usage = client.usage.get_credits_v1()
        assert_matches_type(UsageGetCreditsV1Response, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_credits_v1(self, client: Openregister) -> None:
        response = client.usage.with_raw_response.get_credits_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetCreditsV1Response, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_credits_v1(self, client: Openregister) -> None:
        with client.usage.with_streaming_response.get_credits_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetCreditsV1Response, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_credits_v1(self, async_client: AsyncOpenregister) -> None:
        usage = await async_client.usage.get_credits_v1()
        assert_matches_type(UsageGetCreditsV1Response, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_credits_v1(self, async_client: AsyncOpenregister) -> None:
        response = await async_client.usage.with_raw_response.get_credits_v1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetCreditsV1Response, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_credits_v1(self, async_client: AsyncOpenregister) -> None:
        async with async_client.usage.with_streaming_response.get_credits_v1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetCreditsV1Response, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
