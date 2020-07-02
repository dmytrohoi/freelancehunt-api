#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject
from ..models.country import CountryEntity

from .cities import Cities

__all__ = ('Countries',)


class Countries(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)

    def update(self):
        responce = self._get('/countries')
        self._countries = [
            CountryEntity.de_json(**country)
            for country in responce
        ]

    @property
    def list(self):
        if not hasattr(self, '_countries'):
            self.update()
        return self._countries

    def get(self, country_id=None, iso_code=None):
        if not country_id and not iso_code:
            raise ValueError("Choose one of keyword parameter to get: "
                             "'country_id' or 'iso_code'")
        if country_id:
            attr = 'id'
            check = country_id
        else:
            attr = 'iso2'
            check = iso_code

        filtered_list = list(filter(lambda c: getattr(c, attr) == check,
                                    self.list))
        if len(filtered_list) < 1:
            raise ValueError(f'Country with {attr} "{check}" not found')
        return filtered_list[0]

    def find(self, text):
        filtered_list = list(filter(lambda c: text in c.name, self.list))
        if len(filtered_list) < 1:
            raise ValueError(f'Country with text {text} not found')
        return filtered_list

    @property
    def cities(self):
        if not hasattr(self, '_cities'):
            self._cities = Cities(self.id)
        return self._cities
