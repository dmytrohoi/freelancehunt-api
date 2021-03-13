#!usr/bin/python3
"""`Freelancehunt Documentation - Feed API <https://apidocs.freelancehunt.com/?version=latest#d229fc5c-e10a-41ff-97fc-2c5129f4b3da>`_."""
from typing import List, Optional

from ..core import FreelancehuntObject

from ..models.feed import FeedMessage

from ..utils import common as utils

__all__ = ('Feed',)


class Feed(FreelancehuntObject):
    """Provide operations with Feed API part.

    .. warning:: For directly usage please set `token` argument.

        **token** (`str`) your API token, optional

    """

    _latest_feed = []

    def __init__(self, **kwargs):
        """Creates object to provide operations with Feed API part."""
        super().__init__(**kwargs)

    def update(self):
        """Get latest feed information."""
        responce = self._get('/my/feed')
        self._latest_feed = [
            FeedMessage.de_json(**message)
            for message in responce
        ]

    def read(self):
        """Mark feed as read."""
        return self._post('/my/feed/read')

    @property
    def projects(self) -> List[FeedMessage]:
        """Get all messages with linked project in feed."""
        return utils.filter_list_by_attr(self.list, '_project')

    @property
    def contests(self) -> List[FeedMessage]:
        """Get all messages with linked contest in feed."""
        return utils.filter_list_by_attr(self.list, '_contest')

    def get_new(self) -> List[FeedMessage]:
        """Get all new notifications in feed."""
        return utils.filter_list_by_attr(self.list, 'is_new')

    @property
    def list(self) -> List[FeedMessage]:
        """Get all feed messages."""
        if not self._latest_feed:
            self.update()
        return self._latest_feed
