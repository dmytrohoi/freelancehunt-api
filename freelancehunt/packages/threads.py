#!usr/bin/python3
"""`Freelancehunt Documentation - Threads API <https://apidocs.freelancehunt.com/?version=latest#a313684a-aa56-4f67-bb4c-5ba014c43006>`_."""
from typing import Optional

from ..core import FreelancehuntObject


__all__ = ('Threads',)


class Threads(FreelancehuntObject):
    """Provide operations with Threads API part.

    .. note:: NOT IMPLEMENTED YET!

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Threads API part.

        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)
