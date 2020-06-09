#!usr/bin/python3
"""#TODO: Write comments."""
from .base import FreelancehuntObject


__all__ = [
    'Threads',
    'ThreadEntity'
]


class Threads(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)


class ThreadEntity(FreelancehuntObject):

    def __init__(self, **kwargs):
        super().__init__()
