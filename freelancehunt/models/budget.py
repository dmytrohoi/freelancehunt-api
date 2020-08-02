#!usr/bin/python3
"""Budget object representation.

Documentation example:

.. code-block:: javascript

    "budget": {
        "amount": 2500,
        "currency": "UAH"
    },
"""
from __future__ import annotations
from typing import Type

from ..core import FreelancehuntObject


__all__ = ('BudgetInfo',)


class BudgetInfo(FreelancehuntObject):
    """Provide operations with Budget.

    :var int amount: amount of budget
    :var str currency: current currency
    """

    def __init__(
        self,
        amount: int,
        currency: str,
        **kwargs
    ):
        """Create object to provide operations with Budget.

        :param amount: amount of budget
        :param currency: current currency
        """
        super().__init__()
        self.amount = amount
        self.currency = currency

    @property
    def is_uah(self) -> bool:
        """
        Check that currency is Ukrainian Hryvnia.

        :return: True if currency is hryvnia, False otherwise
        :rtype: bool
        """
        return self.currency == "UAH"

    @property
    def is_rub(self) -> bool:
        """Check that currency is Russian Ruble.

        :return: True if currency is ruble, False otherwise
        :rtype: bool
        """
        return self.currency == "RUB"

    @classmethod
    def de_json(cls, **data) -> Type["BudgetInfo"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `BudgetInfo`
        """
        if not data:
            return None

        return cls(**data)
