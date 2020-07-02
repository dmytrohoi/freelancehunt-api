#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject


__all__ = ('CountryEntity',)


class CountryEntity(FreelancehuntObject):

    def __init__(self, id, iso2, name, **kwargs):
        super().__init__()
        self.id = id
        self.iso2 = iso2
        self.name = name

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        return cls(**data)
