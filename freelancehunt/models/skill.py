#!usr/bin/python3
"""Skill object representation.

Documentation example:

.. code-block:: javascript

    {
        "id": 108,
        "name": "Architectural design"
    }
"""
from typing import Type

from ..core import FreelancehuntObject


__all__ = ('Skill',)


class Skill(FreelancehuntObject):
    """Provide operations with Skill.

    :var int id: skill unique identifier
    :var str name: skill name
    """

    def __init__(self, id: int, name: str, **kwargs):
        """Create object to provide operations with Skill.

        :param int id: skill unique identifier
        :param str name: skill name
        """
        super().__init__()
        self.id = id
        self.name = name

    @classmethod
    def de_json(cls, **data) -> Type["Skill"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `Skill`
        """
        if not data:
            return None

        return cls(**data)
