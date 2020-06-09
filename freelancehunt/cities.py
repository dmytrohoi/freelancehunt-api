#!usr/bin/python3
"""#TODO: Write comments."""
from .base import FreelancehuntObject


__all__ = [
    'Cities',
    'CityEntity'
]


class Cities(FreelancehuntObject):
    """"""

    def __init__(self, country_id, token=None, **kwargs):
        super().__init__(token, **kwargs)
        self.country_id = country_id

    def update(self):
        responce = self._get(f'/cities/{self.country_id}')
        self._cities = [
            CityEntity.de_json(**city)
            for city in responce
        ]

    @property
    def list(self):
        if not hasattr(self, '_cities'):
            self.update()
        return self._cities

    def get(self, city_id):
        filtered_list = filter(lambda city: city.id == city_id, self.list)
        if len(filtered_list) < 1:
            raise ValueError(f'City with id "{city_id}" not found')

        return filtered_list[0]

    def find(self, text):
        filtered_list = filter(lambda country: text in country.name, self.list)
        if len(filtered_list) < 1:
            raise ValueError(f'City with text "{text}" in name not found')

        return filtered_list


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
