#!usr/bin/python3
"""City object representation.

Documentation example:

.. code-block:: javascript

    {
        "id": 2627,
        "name": "Авдеевка"
    },
"""
from __future__ import annotations
from typing import Type

from ..core import FreelancehuntObject


__all__ = ('City',)


class City(FreelancehuntObject):
    """Provide operations with City.

    :var int id: city API identifier
    :var str name: city name
    """

    def __init__(self, id: int, name: str, **kwargs):
        """Create object to provide operations with City.

        :param id: city API identifier
        :param name: city name
        """
        super().__init__()
        self.id = id
        self.name = name

    @classmethod
    def de_json(cls, **data) -> Type[City]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `City`
        """
        if not data:
            return None

        return cls(**data)
