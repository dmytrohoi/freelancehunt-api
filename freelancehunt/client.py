#!usr/bin/python3
"""Main file of FreelanceHunt API framework."""
from datetime import datetime, timedelta

from .core import FreelancehuntObject

from .packages.projects import Projects
from .packages.feed import Feed
from .packages.profiles import Profiles
from .packages.threads import Threads
from .packages.contests import Contests
from .packages.countries import Countries
from .packages.skills import Skills

from .utils.errors import AuthenticationError


__all__ = ('FreelanceHuntClient',)


class FreelanceHuntClient(FreelancehuntObject):
    """
    Basic API client for FreelanceHunt.

    :param str token: Token for access to Freelancehunt API
            (https://freelancehunt.com/my/api)

    """
    def __init__(self, token, **kwargs):
        """Initialization of FreelanceHuntClient object.

        :param str token: user personal access token
        :param dict kwargs: language (str): language of responced data,
            can be: 'uk', 'ru' or 'en' (default: 'en').

        """
        super().__init__(token, **kwargs)

    # API Parts
    @property
    def projects(self) -> Projects:
        """The Projects part of Freelancehunt API."""
        if not hasattr(self, '_projects'):
            self._projects = Projects()
        return self._projects

    @property
    def feed(self) -> Feed:
        """The Feed part of Freelancehunt API."""
        if not hasattr(self, '_feed'):
            self._feed = Feed()
        return self._feed

    @property
    def profiles(self) -> Profiles:
        """The Profiles part of Freelancehunt API."""
        if not hasattr(self, '_profiles'):
            self._profiles = Profiles()
        return self._profiles

    @property
    def threads(self) -> Threads:
        """The Threads part of Freelancehunt API."""
        if not hasattr(self, '_threads'):
            self._threads = Threads()
        return self._threads

    @property
    def contests(self) -> Contests:
        """The Contests part of Freelancehunt API."""
        if not hasattr(self, '_contests'):
            self._contests = Contests()
        return self._contests

    # Static data
    @property
    def countries(self) -> Countries:
        """The Countries part of Freelancehunt API."""
        if not hasattr(self, '_countries'):
            self._countries = Countries()
        return self._countries

    @property
    def skills(self) -> Skills:
        """The Skills part of Freelancehunt API."""
        if not hasattr(self, '_skills'):
            self._skills = Skills()
        return self._skills

    # Additional attributes and functions
    @property
    def is_token_valid(self) -> bool:
        """Check that is token valid."""
        try:
            # Make one request to API
            # NOTE: Need to refactoring
            self.skills.update()
        except AuthenticationError:
            return False
        return True

    @property
    def remaining_limit(self) -> int:
        """Current remaining requests limitation."""
        return self._requester.limit

    @property
    def left_time_limit_update(self) -> int:
        """Second to update remaining API limits."""
        last_request_datetime = self._requester.request_date
        if last_request_datetime is None:
            raise ValueError("No requests found.")

        last_request_hour = last_request_datetime.replace(
            microsecond=0,
            second=0,
            minute=0
        )
        update_datetime = last_request_hour + timedelta(hours=1)
        seconds_left = update_datetime.timestamp() - datetime.utcnow().timestamp()
        return int(seconds_left) if seconds_left > 0 else 0
