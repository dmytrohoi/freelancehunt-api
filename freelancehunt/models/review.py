#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject


__all__ = [
    'ReviewEntity'
]


class ReviewEntity(FreelancehuntObject):

    def __init__(self, **kwargs):
        super().__init__()

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        # NOTE: Not implemented yet
        return cls(**data)
