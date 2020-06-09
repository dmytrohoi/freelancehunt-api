#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt import Cities
from freelancehunt.cities import CityEntity


class Cities:
    """"""

    def __init__(self, country_id, token=None, **kwargs):
        pass

    def update(self):
        pass

    #property
    def list(self):
        pass

    def get(self, city_id):
        pass

    def find(self, text):
        pass


class CityEntity:

    def __init__(self, id, name, **kwargs):
        pass

    #classmethod
    def de_json(cls, **data):
        pass
