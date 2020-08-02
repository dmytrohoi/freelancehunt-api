#!usr/bin/python3
"""Project object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 299165,
      "type": "project",
      "attributes": {
        "name": "Looking for Full stack developer",
        "description": "Backend must be PHP like Yii or Laravel.",
        "description_html": "<p>Backend must be PHP like Yii or Laravel.</p>",
        "skills": [
          {
            "id": 56,
            "name": "1C"
          }
        ],
        "status": {
          "id": 11,
          "name": "Open for proposals"
        },
        "budget": {
          "amount": 2300,
          "currency": "UAH"
        },
        "bid_count": 1,
        "is_remote_job": false,
        "is_premium": false,
        "is_only_for_plus": false,
        "location": null,
        "safe_type": "employer",
        "is_personal": null,
        "employer": {
          "id": 23476,
          "type": "employer",
          "login": "hello-world",
          "first_name": "Михаил",
          "last_name": "К.",
          "avatar": {
            "small": {
              "url": "https://content.freelancehunt.com/profile/photo/50/hello-world.png",
              "width": 50,
              "height": 50
            },
            "large": {
              "url": "https://content.freelancehunt.com/profile/photo/225/hello-world.png",
              "width": 255,
              "height": 255
            }
          },
          "self": "https://api.freelancehunt.com/v2/employers/23476"
        },
        "freelancer": null,
        "updates": [],
        "published_at": "2019-03-25T19:51:53+02:00",
        "expired_at": "2019-04-01T16:51:53+03:00"
      },
      "links": {
        "self": {
          "api": "https://api.freelancehunt.com/v2/projects/299165",
          "web": "https://freelancehunt.com/project/looking-for-full-stack-developer/299165.html"
        },
        "comments": "https://api.freelancehunt.com/v2/projects/299165/comments",
        "bids": "https://api.freelancehunt.com/v2/projects/299165/bids"
      }
    }
"""
from __future__ import annotations
from datetime import datetime

from typing import List, Optional, Type

from ..core import FreelancehuntObject
from .user import Employer, Freelancer
from .skill import Skill
from .budget import BudgetInfo

from ..utils.errors import BadRequestError


__all__ = ('Project',)


class Project(FreelancehuntObject):
    """Provide operations with Project.

    :var int id: project unique identifier
    :var Optional[str] name: project title, defaults to None
    :var Optional[Employer] ~.employer: project creator information, defaults to None
    :var Optional[Freelancer] ~.freelancer: project executor information, defaults to None
    :var Optional[BudgetInfo] budget: budget of project, defaults to None
    :var Optional[str] safe_type: type of safe proposed by the employer, defaults to None
    :var Optional[dict] ~.status: project status information, defaults to None
    :var Optional[str] description:  description text, defaults to None
    :var Optional[str] description_html: description text in html formatting, defaults to None
    :var Optional[List[Skill]] ~.skills: required skills for the executor, defaults to None
    :var Optional[int] bid_count: count of bids, defaults to None
    :var Optional[bool] is_remote_job: sign that the project is remote job, defaults to None
    :var Optional[bool] is_premium: sign that the project only for premium, defaults to None
    :var Optional[bool] is_only_for_plus: sign that the project only for Plus accounts, defaults to None
    :var Optional[bool] is_personal: sign that the project is private, defaults to None
    :var Optional[dict] updates: project updates, defaults to None
    :var Optional[dict] location: required location for the executor, defaults to None
    :var Optional[datetime] expired_at: string representation of the expire date, defaults to None
    :var Optional[datetime] published_at: string representation of the publish date, defaults to None
    :var Optional[dict] links: URLs related to project, defaults to None
    """

    def __init__(self,
                 id: int,
                 name: Optional[str] = None,
                 employer: Optional[Employer] = None,
                 freelancer: Optional[Freelancer] = None,
                 budget: Optional[BudgetInfo] = None,
                 safe_type: Optional[str] = None,
                 status: Optional[dict] = None,
                 description: Optional[str] = None,
                 description_html: Optional[str] = None,
                 skills: Optional[list] = None,
                 bid_count: Optional[int] = None,
                 is_remote_job: Optional[bool] = None,
                 is_premium: Optional[bool] = None,
                 is_only_for_plus: Optional[bool] = None,
                 is_personal: Optional[bool] = None,
                 updates: Optional[dict] = None,
                 location: Optional[dict] = None,
                 expired_at: Optional[str] = None,
                 published_at: Optional[str] = None,
                 links: Optional[dict] = None,
                 **kwargs):
        """Create object to provide operations with Project.

        :param int id: project unique identifier
        :param Optional[str] name: project title, defaults to None
        :param Optional[Employer] employer: project creator information, defaults to None
        :param Optional[Freelancer] freelancer: project executor information, defaults to None
        :param Optional[BudgetInfo] budget: budget of project, defaults to None
        :param Optional[str] safe_type: type of safe proposed by the employer, defaults to None
        :param Optional[dict] status: project status information, defaults to None
        :param Optional[str] description:  description text, defaults to None
        :param Optional[str] description_html: description text in html formatting, defaults to None
        :param Optional[List[Skill]] skills: required skills for the executor, defaults to None
        :param Optional[int] bid_count: count of bids, defaults to None
        :param Optional[bool] is_remote_job: sign that the project is remote job, defaults to None
        :param Optional[bool] is_premium: sign that the project only for premium, defaults to None
        :param Optional[bool] is_only_for_plus: sign that the project only for Plus accounts, defaults to None
        :param Optional[bool] is_personal: sign that the project is private, defaults to None
        :param Optional[dict] updates: project updates, defaults to None
        :param Optional[dict] location: required location for the executor, defaults to None
        :param Optional[str] expired_at: string representation of the expire date, defaults to None
        :param Optional[str] published_at: string representation of the publish date, defaults to None
        :param Optional[dict] links: URLs related to project, defaults to None
        """
        super().__init__()
        # Raw attributes
        self.id = id
        self.name = name
        self.safe_type = safe_type
        self.description = description
        self.description_html = description_html
        self.bid_count = bid_count
        self.is_remote_job = is_remote_job
        self.is_premium = is_premium
        self.is_only_for_plus = is_only_for_plus
        self.is_personal = is_personal
        self.expired_at = (
            datetime.fromisoformat(expired_at) if expired_at else None
        )
        self.published_at = (
            datetime.fromisoformat(published_at) if published_at else None
        )
        self.updates = updates
        self.location = location  # TODO: Make parsing for this attribute
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
        self.api_url = f"/projects/{self.id}"

    @property
    def status(self) -> str:
        """Get current project status."""
        return self._status["name"]

    @property
    def status_code(self) -> int:
        """Get code of current project status."""
        return self._status["id"]

    @property
    def bids(self) -> List[Optional[Type["Bid"]]]:
        """Get all bids for this project."""
        return self.get_bids()

    @property
    def active_bids(self) -> List[Optional[Type["Bid"]]]:
        """Get active bids for this project."""
        return self.get_bids(status="active")

    @property
    def winner_bid(self) -> Optional[Type["Bid"]]:
        """Get winner bid for this project."""
        winner_bid_list = self.get_bids(is_winner=True)
        return None if not winner_bid_list else winner_bid_list.pop()

    def get_bids(
        self,
        status: Optional[str] = None,
        is_winner: bool = False
    ) -> List[Optional[Type["Bid"]]]:
        """Get filtered bids for this project.

        :param status: status of desired bids
        :param is_winner: get only winner bid
        """
        from .bid import Bid
        filters = {}

        if is_winner:
            filters.update({"is_winner": 1})
        elif status:
            filters.update({"status": status})

        raw_bids = self._get(self.api_url + "/bids", filters=filters)
        return [Bid.de_json(**bid) for bid in raw_bids]

    def close(self):
        """Close project without winner.

        .. note:: For employer account and your own project.
        """
        try:
            self._post(self.api_url + '/close')
        except BadRequestError:
            return False
        return True

    def reopen(self):
        """Reopen project.

        .. note:: For employer account and your own project.
        """
        try:
            self._post(self.api_url + '/reopen')
        except BadRequestError:
            return False
        return True

    def extend(self, expired_at: datetime):
        """Extend project end date.

        .. note:: For employer account and your own project.
        """
        payload = {
            "expired_at": expired_at.isoformat()
        }
        try:
            self._post(self.api_url + '/extend', payload=payload)
        except BadRequestError:
            return False
        return True

    @property
    def link(self):
        """Get direct project link."""
        return self._links["web"]

    def load_details(self):
        """Load details about current Project and reload all attributes."""
        responce = self._get(self.api_url)
        new = self.de_json(**responce)
        self.__dict__ = new.__dict__

    @classmethod
    def de_json(cls, **data) -> Type["Project"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `Project`
        """
        if not data:
            return None

        # NOTE: Can be None for plus_only projects
        employer = data.get("employer")
        if employer:
            data["employer"] = Employer.de_json(**employer)

        freelancer = data.get("freelancer")
        if freelancer:
            data["freelancer"] = Freelancer.de_json(**freelancer)

        budget = data.get("budget")
        if budget:
            data["budget"] = BudgetInfo.de_json(**budget)

        skills = data.get("skills")
        if skills:
            data["skills"] = [Skill.de_json(**skill) for skill in skills]

        self_ = data.pop("self", None)
        if self_:
            links = data.get("links", {})
            links.update({"self": self_})
            data["links"] = links
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

    def __str__(self):
        employer = self.employer.full_name \
                   if getattr(self, 'employer') is not None \
                   else 'Secret (Plus accounts only) or Not loaded yet'
        return f'Project #{self.id} by {employer} ({self.status})'

    def __repr__(self):
        employer = self.employer.id \
                   if getattr(self, 'employer') is not None \
                   else 'Secret (Plus accounts only) or Not loaded yet'
        return f'<freelancehunt.Project #{self.id} (Employer '\
               f'#{employer} Status: {self.status_code})>'
