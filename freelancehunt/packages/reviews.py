#!usr/bin/python3
"""`Freelancehunt Documentation - Reviews API <https://apidocs.freelancehunt.com/?version=latest#ffd08d46-6b1e-416f-be75-e6cb583df5c0>`_."""
from typing import List, Optional, Type

from ..core import FreelancehuntObject

from ..models.review import Review

__all__ = ('Reviews',)


class Reviews(FreelancehuntObject):
    """Provide operations with Reviews API part.

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Reviews API part.

        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)

    def get_reviews(self, profile_type: str, profile_id: int) -> List[Type["Review"]]:
        """Get reviews of the desired profile.

        :param profile_type: type of the desired profile, can be "freelancer" or "employer"
        :param profile_id: identifier of the desired profile
        :return: profile reviews
        """
        responce = self._get(f'/{profile_type}s/{profile_id}/reviews')
        return [Review.de_json(**data) for data in responce]

    def get_my_reviews(self) -> List[Type["Review"]]:
        """Get reviews of my profile.

        :return: profile reviews
        """
        responce = self._get('/my/reviews')
        return [Review.de_json(**data) for data in responce]