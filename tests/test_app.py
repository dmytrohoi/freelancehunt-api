#!usr/bin/python3
"""Tests for FreelancehuntClient class."""
import os
import logging

import pytest

from freelancehunt import FreelanceHuntClient

from freelancehunt.projects import Projects
from freelancehunt.feed import Feed
from freelancehunt.profiles import Profiles
from freelancehunt.threads import Threads
from freelancehunt.contests import Contests

from freelancehunt.countries import Countries
from freelancehunt.skills import Skills


logger = logging.getLogger(__name__)

token = os.environ['TOKEN']


@pytest.fixture(scope="function", params=[token])
def client(request):
    client = FreelanceHuntClient(request.param)
    logger.info(f'Started client with {request.param}')
    return client


class TestFreelancehuntClient:

    def test_projects(self, client: FreelanceHuntClient):
        assert isinstance(client.projects, Projects)

    def test_feed(self, client: FreelanceHuntClient):
        assert isinstance(client.feed, Feed)

    def test_profiles(self, client: FreelanceHuntClient):
        assert isinstance(client.profiles, Profiles)

    def test_threads(self, client: FreelanceHuntClient):
        assert isinstance(client.threads, Threads)

    def test_contests(self, client: FreelanceHuntClient):
        assert isinstance(client.contests, Contests)

    def test_skills(self, client: FreelanceHuntClient):
        assert isinstance(client.skills, Skills)

    def test_countries(self, client: FreelanceHuntClient):
        assert isinstance(client.countries, Countries)

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
