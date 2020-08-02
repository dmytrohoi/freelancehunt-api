#!usr/bin/python3
"""Country object representation.

Documentation example:

.. code-block:: javascript

    {
        "id": 4,
        "iso2": "AU",
        "name": "Австралия"
    },
"""
from typing import Optional

from ..core import FreelancehuntObject


__all__ = ('Country',)


class Country(FreelancehuntObject):
    """Provide operations with Country.

    :var int id: country API identifier
    :var str iso2: ISO format of country identifier, defaults to None (for Profile "country" var)
    :var str name: country name
    """

    def __init__(self, id: int, name: str, iso2: Optional[str] = None, **kwargs):
        """Create object to provide operations with Country.

        :param id: country API identifier
        :param iso2: ISO format of country identifier
        :param name: country name
        """
        super().__init__()
        self.id = id
        self.iso2 = iso2
        self.name = name

    @classmethod
    def de_json(cls, **data):
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: Country
        """
        if not data:
            return None

        return cls(**data)
