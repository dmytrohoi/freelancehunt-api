#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject

from ..models.feed import FeedEntity


__all__ = ('Feed',)


class Feed(FreelancehuntObject):
    """"""
    _latest_feed = []

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)

    def update(self):
        """Get latest feed information."""
        responce = self._get('/my/feed')
        self._latest_feed = [
            FeedEntity.de_json(**message)
            for message in responce
        ]

    def read(self):
        """Mark feed as read."""
        return self._post('/my/feed/read')

    @property
    def projects(self):
        """Get all projects in feed."""
        return self._filter_list_by_attr(self.list, '_project')

    @property
    def contests(self):
        """Get all contests in feed."""
        return self._filter_list_by_attr(self.list, '_contest')

    def get_new(self):
        """Get all new notifications in feed."""
        return self._filter_list_by_attr(self.list, 'is_new')

    @property
    def list(self):
        if not self._latest_feed:
            self.update()
        return self._latest_feed
