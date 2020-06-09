#!usr/bin/python3
"""#TODO: Write comments."""
from .base import FreelancehuntObject


__all__ = [
    'Reviews'
    'ReviewEntity'
]

class Reviews(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)


class ReviewEntity(FreelancehuntObject):

    def __init__(self, **kwargs):
        super().__init__()

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        # NOTE: Not implemented yet
        return cls(**data)
