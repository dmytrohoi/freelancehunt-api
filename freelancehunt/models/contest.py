#!usr/bin/python3
"""Contest object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 1390,
      "type": "contest",
      "attributes": {
        "name": "New contest",
        "description": "Transferring party — The Customers and the Contractors owning confidential information and personal data transferred by them to the Website Administration during registration and use of the Service.",
        "description_html": "<p>Transferring party — The Customers and the Contractors owning confidential information and personal data transferred by them to the Website Administration during registration and use of the Service.</p>",
        "skill": {
          "id": 9,
          "name": "Icon"
        },
        "status": {
          "id": 140,
          "name": "Final"
        },
        "budget": {
          "amount": 1002,
          "currency": "UAH"
        },
        "application_count": 1,
        "published_at": "2019-04-08T17:05:25+03:00",
        "duration_days": 5,
        "final_started_at": "2019-04-13T17:05:25+03:00",
        "freelancer": null,
        "employer": {
          "id": 38444,
          "type": "employer",
          "login": "jeweller",
          "first_name": "Oleg",
          "last_name": "Vinnik",
          "avatar": {
            "small": {
              "url": "https://content.freelancehunt.com/profile/photo/50/jeweller.png",
              "width": 50,
              "height": 50
            },
            "large": {
              "url": "https://content.freelancehunt.com/profile/photo/225/jeweller.png",
              "width": 255,
              "height": 255
            }
          },
          "self": "https://api.freelancehunt.com/v2/employers/38444"
        },
        "updates": []
      },
      "links": {
        "self": {
          "api": "https://api.freelancehunt.com/v2/contests/1390",
          "web": "https://freelancehunt.com/contest/new-contest/1390.html"
        },
        "comments": "https://api.freelancehunt.com/v2/contests/1390/comments",
        "applications": "https://api.freelancehunt.com/v2/contests/1390/applications"
      }
    }

"""
from __future__ import annotations
from typing import List, Optional, Type
from datetime import datetime

from ..core import FreelancehuntObject

from .user import Employer, Freelancer
from .skill import Skill
from .budget import BudgetInfo


__all__ = ('Contest',)


class Contest(FreelancehuntObject):
    """Provide operations with Contest.

    :var int id: contest unique identifier
    :var Optional[str] name: contest title name, defaults to None
    :var Optional[BudgetInfo] budget: budget of contest, defaults to None
    :var Optional[str] ~.status: current contest status, defaults to None
    :var Optional[str] description: description text, defaults to None
    :var Optional[str] description_html: description text in html formatting, defaults to None
    :var Optional[List[Skill]] ~.skills: required skill for freelancer, defaults to None
    :var Optional[str] final_started_at: string representation of the closing date, defaults to None
    :var Optional[Employer] ~.employer: employer information object, defaults to None
    :var Optional[int] application_count: count of application, defaults to None
    :var Optional[Freelancer] ~.freelancer: freelancer information object, defaults to None
    :var Optional[list] updates: list of all contest updates, defaults to None
    :var Optional[str] published_at: string representation of the publish date, defaults to None
    :var Optional[dict] links: linked URL, defaults to None
    :var Optional[int] duration_days: contest duration in days, defaults to None
    """

    def __init__(
        self,
        id: int,
        name: Optional[str] = None,
        budget: Optional[BudgetInfo] = None,
        status: Optional[str] = None,
        description: Optional[str] = None,
        description_html: Optional[str] = None,
        skills: Optional[List[Skill]] = None,
        final_started_at: Optional[str] = None,
        employer: Optional[Employer] = None,
        application_count: Optional[int] = None,
        freelancer: Optional[Freelancer] = None,
        updates: Optional[list] = None,
        published_at: Optional[str] = None,
        links: Optional[dict] = None,
        duration_days: Optional[int] = None,
        **kwargs
    ):
        """Create object to provide operations with Contest.

        :param int id: contest unique identifier
        :param Optional[str] name: contest title, defaults to None
        :param Optional[BudgetInfo] budget: budget of contest, defaults to None
        :param Optional[str] status: current contest status, defaults to None
        :param Optional[str] description: description text, defaults to None
        :param Optional[str] description_html: description text in html formatting, defaults to None
        :param Optional[List[Skill]] skills: required skill for the executor, defaults to None
        :param Optional[str] final_started_at: string representation of the closing date, defaults to None
        :param Optional[Employer] employer: employer information object, defaults to None
        :param Optional[int] application_count: count of application, defaults to None
        :param Optional[Freelancer] freelancer: contest executor information, defaults to None
        :param Optional[list] updates: list of all contest updates, defaults to None
        :param Optional[str] published_at: string representation of the publish date, defaults to None
        :param Optional[dict] links: URLs related to contest, defaults to None
        :param Optional[int] duration_days: contest duration in days, defaults to None
        """
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.description_html = description_html
        self.application_count = application_count
        self.updates = updates
        self.duration_days = duration_days
        self.final_started_at = (
            datetime.fromisoformat(final_started_at) if final_started_at else None
        )
        self.published_at = (
            datetime.fromisoformat(published_at) if published_at else None
        )
        self.other = kwargs
        self.links = links
        # Framework objects
        self.employer = employer
        self.freelancer = freelancer
        self.budget = budget
        self.skills = skills
        # Will be parsed to objects
        self._status = status
        # Custom attributes
        self.api_url = f"/contests/{self.id}"

    @property
    def status(self) -> str:
        """Get status of this contest."""
        return self._status["name"]

    @property
    def status_code(self) -> int:
        """Get status code of this contest."""
        return self._status["id"]

    def load_details(self):
        """Load details about current Contest and reload all attributes."""
        responce = self._get(self.api_url)
        new = self.de_json(**responce)
        self.__dict__ = new.__dict__

    @classmethod
    def de_json(cls, **data: Optional[dict]) -> Type["Contest"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class
        """
        if not data:
            return None

        data["skills"] = [Skill.de_json(**skill) for skill in data["skills"]]
        data["employer"] = Employer.de_json(**data["employer"])
        data["budget"] = BudgetInfo.de_json(**data["budget"])
        if data["freelancer"]:
            data["freelancer"] = Freelancer.de_json(**data["freelancer"])
        return cls(**data)

    def __getattribute__(self, name):
        """Auto load_details() if the desired attribute is None."""
        if name.startswith("__") or name not in self.__dict__:
            return object.__getattribute__(self, name)

        value = self.__dict__[name]
        if value is None:
            self.load_details()
            value = self.__dict__[name]
        return value
