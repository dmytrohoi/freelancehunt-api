#!usr/bin/python3
"""`Freelancehunt Documentation - Cities API <https://apidocs.freelancehunt.com/?version=latest#65a2a9b4-b52d-4706-8c54-990600b58c2b>`_."""
from __future__ import annotations
from typing import List, Optional

from ..core import FreelancehuntObject

from ..models.city import City


__all__ = ('Cities',)


class Cities(FreelancehuntObject):
    """Provide operations with Cities API part.

    .. note:: This module contains static content. It may be `update()`, but loaded info does not change on the API side.

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    :param int country_id: API-related country identifier to get cities of it
    """

    def __init__(self, country_id: int, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Cities API part.

        :param country_id: the desired country to get cities.
        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)
        self.country_id = country_id

        self._url = f'/cities/{self.country_id}'

    def update(self) -> None:
        """Update static information from API."""
        cities_data = self._get(self._url)
        self._cities = [
            City.de_json(**city)
            for city in cities_data
        ]

    @property
    def list(self) -> List[City]:
        """Get list of all cities.

        :return: list of cities.
        """
        if not hasattr(self, '_cities'):
            self.update()
        return self._cities

    def get(self, city_id: int) -> City:
        """Get the desired city by city_id.

        :param city_id: id of the desired city
            (https://apidocs.freelancehunt.com/?version=latest#65a2a9b4-b52d-4706-8c54-990600b58c2b).
        :return: the desired city.
        """
        return filter(lambda city: city.id == city_id, self.list)

    def find(self, text: str) -> List[City]:
        """Find the names of the cities that contain the desired text.

        :param text: the desired text that need to be in an city name.
        :return: list of cities with an text in name.
        """
        return list(filter(lambda country: text in country.name, self.list))
