#!usr/bin/python3
"""`Freelancehunt Documentation - Countries API <https://apidocs.freelancehunt.com/?version=latest#d781d975-810f-47d6-b267-5179ed8a5562>`_."""
from typing import List, Optional

from ..core import FreelancehuntObject

from ..models.country import Country

from .cities import Cities


__all__ = ('Countries',)


class Countries(FreelancehuntObject):
    """Provide operations with Countries API part.

    .. note:: This module contains static content. It may be `update()`,
              but loaded info does not change on the API side.

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Countries API part.

        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)

    def update(self):
        """Update static information from API."""
        responce = self._get('/countries')
        self._countries = [
            Country.de_json(**country)
            for country in responce
        ]

    @property
    def list(self) -> List[Country]:
        """Get list of all countries.

        :return: list of countries
        """
        if not hasattr(self, '_countries'):
            self.update()
        return self._countries

    def get(self,
            country_id: Optional[int] = None,
            iso_code: Optional[str] = None) -> Country:
        """Get the filtered country.

        .. warning: At least one of the parameters is required.

        :param country_id: the desired API-related country id, defaults to None
        :param iso_code: the desired ISO code of country, defaults to None
        :raises AttributeError: No one of parameters filled
        :raises ValueError: Contry not found
        :return: the desired country
        """
        if not country_id and not iso_code:
            raise AttributeError("Choose one of keyword parameter to get: "
                             "'country_id' or 'iso_code'")
        if country_id:
            attr = 'id'
            check = country_id
        else:
            attr = 'iso2'
            check = iso_code

        filtered_list = list(filter(lambda c: getattr(c, attr) == check,
                                    self.list))
        if not filtered_list:
            raise ValueError(f'Country with {attr} "{check}" not found')
        return filtered_list.pop()

    def find(self, text: str) -> List[Country]:
        """Find countries with the desired text.

        :param text: text in country name
        :raises ValueError: No countries found
        :return: list of countries with an text in name
        """
        filtered_list = list(filter(lambda c: text in c.name, self.list))
        if not filtered_list:
            raise ValueError(f'Country with text {text} not found')
        return filtered_list

    @property
    def cities(self) -> Cities:
        """Cities linked to this Country.

        :return: object for manipulate with Cities API part
        """
        if not hasattr(self, '_cities'):
            self._cities = Cities(self.id)
        return self._cities
