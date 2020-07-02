#!usr/bin/python3
"""Tests for FreelancehuntClient class."""
import os
import logging

import pytest

from freelancehunt import FreelanceHuntClient

from freelancehunt import (
    Projects,
    Feed,
    Profiles,
    Threads,
    Contests,
    Countries,
    Skills
)


logger = logging.getLogger(__name__)

token = os.environ['TOKEN']


@pytest.fixture(scope="function", params=[token])
def client(request):
    client = FreelanceHuntClient(request.param)
    logger.info(f'Started client with {request.param}')
    return client


class TestFreelancehuntClient:

    @pytest.mark.parametrize('args, kwargs, expected', [
        pytest.param([token], {}, True, id="valid_args"),
        pytest.param([], {'token': token}, True, id="valid_kwargs"),
        pytest.param([], {}, False, id="without_args")
    ])
    def test_init(self, args, kwargs, expected):
        try:
            FreelanceHuntClient(*args, **kwargs)
        except Exception as E:
            assert not expected, f'Client has been initialized: {E}'
        else:
            assert expected, 'Client not initialized'

    def test_projects(self, client: FreelanceHuntClient):
        # Not initialized before
        # and check that it has been initialized
        assert isinstance(client.projects, Projects) \
            and hasattr(client, '_projects') and client.projects

    def test_feed(self, client: FreelanceHuntClient):
        assert isinstance(client.feed, Feed) and hasattr(client, '_feed') \
            and client.feed

    def test_profiles(self, client: FreelanceHuntClient):
        assert isinstance(client.profiles, Profiles) \
            and hasattr(client, '_profiles') and client.profiles

    def test_threads(self, client: FreelanceHuntClient):
        assert isinstance(client.threads, Threads) \
            and hasattr(client, '_threads') and client.threads

    def test_contests(self, client: FreelanceHuntClient):
        assert isinstance(client.contests, Contests) \
            and hasattr(client, '_contests') and client.contests

    def test_skills(self, client: FreelanceHuntClient):
        assert isinstance(client.skills, Skills) \
            and hasattr(client, '_skills') and client.skills

    def test_countries(self, client: FreelanceHuntClient):
        assert isinstance(client.countries, Countries) \
            and hasattr(client, '_countries') and client.countries

    def test_remaining_limit(self, client: FreelanceHuntClient):
        assert client.remaining_limit is None

        # Make one request
        client.is_token_valid

        limit = client.remaining_limit
        assert isinstance(limit, int) and 0 <= limit <= 1200

    def test_left_time_limit_update(self, client: FreelanceHuntClient):
        try:
            client.left_time_limit_update
        except ValueError:
            assert True
        else:
            assert False

        # Make one request
        client.is_token_valid

        left_time = client.left_time_limit_update
        assert isinstance(left_time, int) and 0 <= left_time <= 3600

    @pytest.mark.parametrize('client, expected', [
        pytest.param(token, True, id="valid_token"),
        pytest.param('IS_NOT_VALID_TOKEN', False, id="invalid_token")
    ], indirect=True)
    def test_is_token_valid(self, client: FreelanceHuntClient, expected: bool):
        assert client.is_token_valid == expected, 'Token not valid'
