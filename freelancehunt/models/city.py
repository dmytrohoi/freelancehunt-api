#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject


__all__ = ('CityEntity',)


class CityEntity(FreelancehuntObject):

    def __init__(self, id, name, **kwargs):
        super().__init__()
        self.id = id
        self.name = name

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        return cls(**data)
