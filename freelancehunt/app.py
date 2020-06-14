#!usr/bin/python3
"""Main file of FreelanceHunt API framework."""
from datetime import datetime, timedelta

from .base import FreelancehuntObject
from .utils import Requester

from .projects import Projects
from .feed import Feed
from .profiles import Profiles
from .threads import Threads
from .contests import Contests
from .countries import Countries
from .skills import Skills

from .errors import AuthenticationError


__all__ = [
    'FreelanceHuntClient'
]


class FreelanceHuntClient(FreelancehuntObject):
    """
    Basic API client for FreelanceHunt.

    Args:
        token (str): Token for access to Freelancehunt API
            (https://freelancehunt.com/my/api)

    """
    def __init__(self, token, **kwargs):
        """TODO: Write comments."""
        super().__init__(token, **kwargs)

    # API Parts
    @property
    def projects(self):
        """Represent the Projects part of Freelancehunt API."""
        if not hasattr(self, '_projects'):
            self._projects = Projects()
        return self._projects

    @property
    def feed(self):
        """TODO: Write comments."""
        if not hasattr(self, '_feed'):
            self._feed = Feed()
        return self._feed

    @property
    def profiles(self):
        """TODO: Write comments."""
        if not hasattr(self, '_profiles'):
            self._profiles = Profiles()
        return self._profiles

    @property
    def threads(self):
        """TODO: Write comments."""
        if not hasattr(self, '_threads'):
            self._threads = Threads()
        return self._threads

    @property
    def contests(self):
        """TODO: Write comments."""
        if not hasattr(self, '_contests'):
            self._contests = Contests()
        return self._contests

    # Static data
    @property
    def countries(self):
        """TODO: Write comments."""
        if not hasattr(self, '_countries'):
            self._countries = Countries()
        return self._countries

    @property
    def skills(self):
        """TODO: Write comments."""
        if not hasattr(self, '_skills'):
            self._skills = Skills()
        return self._skills

    # Additional attributes and functions
    @property
    def is_token_valid(self):
        """TODO: Write comments."""
        try:
            # Make one request to API
            self.skills.update()
        except AuthenticationError:
            return False
        return True

    @property
    def remaining_limit(self):
        """TODO: Write comments."""
        return self.requester.limit

    @property
    def left_time_limit_update(self):
        """
        Second to update remaining API limits.

        Return:
            int: count of second to next limitation update.

        """
        last_request_datetime = self.requester.request_date
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
