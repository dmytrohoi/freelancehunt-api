#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject

from ..models.contest import ContestEntity

__all__ = [
    'Contests'
]


class Contests(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        """TODO: Write comments."""
        super().__init__(token, **kwargs)

