#!usr/bin/python3
"""`Freelancehunt Documentation - Contests API <https://apidocs.freelancehunt.com/?version=latest#28c10a97-5d31-4857-b526-39466229c885>`_."""
from typing import Optional
from ..core import FreelancehuntObject

from ..models.contest import Contest


__all__ = ('Contests',)


class Contests(FreelancehuntObject):
    """Provide operations with Contests API part.

    .. note:: NOT IMPLEMENTED YET!

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Contests API part.

        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)

