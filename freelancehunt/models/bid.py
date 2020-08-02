#!usr/bin/python3
"""Bid object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 3119168,
      "type": "bid",
      "attributes": {
        "days": 25,
        "safe_type": "employer",
        "budget": {
          "amount": 18000,
          "currency": "UAH"
        },
        "comment": "I can help you with this problem.",
        "status": "active",
        "is_hidden": false,
        "is_winner": false,
        "freelancer": {
          "id": 191397,
          "type": "freelancer",
          "login": "NeoSeo",
          "first_name": "Maxim",
          "last_name": "P.",
          "avatar": {
            "small": {
              "url": "https://content.freelancehunt.com/profile/photo/50/NeoSeo.png",
              "width": 50,
              "height": 50
            },
            "large": {
              "url": "https://content.freelancehunt.com/profile/photo/225/NeoSeo.png",
              "width": 255,
              "height": 255
            }
          },
          "self": "http://api.freelancehunt.com/v2/freelancers/191397"
        },
        "project": {
          "id": 299172,
          "type": "project",
          "name": "Project with bids",
          "status": {
            "id": 11,
            "name": "Open for proposals"
          },
          "safe_type": "employer",
          "budget": {
            "amount": 2300,
            "currency": "UAH"
          },
          "self": "http://api.freelancehunt.com/v2/projects/299172"
        },
        "attachment": null,
        "published_at": "2018-04-15T23:44:05+03:00"
      }
    },

"""
from __future__ import annotations
from typing import Type

from ..core import FreelancehuntObject

from .budget import BudgetInfo
from .user import Freelancer
from .project import Project


__all__ = ('Bid',)


class Bid(FreelancehuntObject):
    """Provide operations with Bid API object.

    :var int id: bid unique identifier
    :var str ~.status: bid current status
    :var int days: days estimated by freelancer for complete this project
    :var str safe_type: type of payment method (for safe)
    :var str comment: comment from freelancer about this project
    :var str currency: freelancer currency for bid
    :var bool is_hidden: mark hidden from others bid
    :var bool is_winner: mark winner bid
    :var Freelancer ~.freelancer: bid creator information
    :var BudgetInfo budget: estimated budget for this project
    :var Project ~.project: related project information
    """

    def __init__(
        self,
        id: int,
        status: str,
        days: int,
        safe_type: str,
        comment: str,
        currency: str,
        is_hidden: bool,
        is_winner: bool,
        freelancer: Freelancer,
        budget: BudgetInfo,
        project: Project,
        **kwargs
    ):
        """Create object to provide operations with Bid API object.

        :param id: bid unique identifier
        :param status: bid current status
        :param days: days estimated by freelancer for complete this project
        :param safe_type: type of payment method (for safe)
        :param comment: comment from freelancer about this project
        :param currency: freelancer currency for bid
        :param is_hidden: mark hidden from others bid
        :param is_winner: mark winner bid
        :param freelancer: bid creator information
        :param budget: estimated budget for this project
        :param project: related project information
        """
        super().__init__()
        self.id = id
        self.status = status
        self.days = days
        self.safe_type = safe_type
        self.comment = comment
        self.currency = currency
        self.is_hidden = is_hidden
        self.is_winner = is_winner
        self.freelancer = freelancer
        self.budget = budget
        self.project = project
        self.other = kwargs

    def revoke(self) -> bool:
        """Revoke your bid.

        .. note:: Only for Freelancer and your own bid.

        :return: status of operation.
        :rtype: bool
        """
        url = f"/projects/{self.project.id}/bids/{self.id}/revoke"
        return self._post(url)

    def restore(self) -> bool:
        """Restore your bid.

        :return: status of operation.
        :rtype: bool
        """
        url = f"/projects/{self.project.id}/bids/{self.id}/restore"
        return self._post(url)

    def reject(self) -> bool:
        """Reject this bid.

        .. note:: Only for Employer and your own project.

        :return: status of operation.
        :rtype: bool
        """
        url = f"/projects/{self.project.id}/bids/{self.id}/reject"
        return self._post(url)

    def choose(self, comment: str) -> bool:
        """Choose this bid.

        .. note:: Only for Employer and your own project.

        :param comment: comment for winner to start dialog with freelancer.
        :type comment: str
        :return: status of operation.
        :rtype: bool
        """
        url = f"/projects/{self.project.id}/bids/{self.id}/choose"
        return self._post(url, payload={"comment": comment})

    @classmethod
    def de_json(cls, **data) -> Type[BudgetInfo]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `Bid`
        """
        if not data:
            return None

        data["budget"] = BudgetInfo.de_json(**data["budget"])
        data["freelancer"] = Freelancer.de_json(**data["freelancer"])
        data["project"] = Project.de_json(**data["project"])
        return cls(**data)
