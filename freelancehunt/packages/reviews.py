#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject


__all__ = ('Reviews',)


class Reviews(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)

