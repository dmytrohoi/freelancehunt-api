#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt import Countries
from freelancehunt.countries import CountryEntity


class Countries:

    def __init__(self, token=None, **kwargs):
        pass

    def update(self):
        pass

    #property
    def list(self):
        pass

    def get(self, country_id=None, iso_code=None):
        pass

    def find(self, text):
        pass

    #property
    def cities(self):
        pass


class CountryEntity:

    def __init__(self, id, iso2, name, **kwargs):
        pass

    #classmethod
    def de_json(cls, **data):
        pass
