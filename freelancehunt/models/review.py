#!usr/bin/python3
"""Review object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 90500,
      "type": "review",
      "attributes": {
        "published_at": "2019-04-25T15:02:19+03:00",
        "is_pending": false,
        "pending_ends_at": null,
        "comment": "Everything is perfect!",
        "grades": {
          "quality": 10,
          "professionalism": 10,
          "cost": 10,
          "connectivity": 10,
          "schedule": 10,
          "total": 10
        },
        "from": {
          "id": 38444,
          "type": "employer",
          "login": "jeweller",
          "first_name": "Oleg",
          "last_name": "V.",
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
        "project": {
          "id": 299178,
          "type": "project",
          "name": "Project with response review(good)",
          "status": {
            "id": 21,
            "name": "Project complete"
          },
          "safe_type": "employer",
          "budget": {
            "amount": 1001,
            "currency": "UAH"
          },
          "self": "https://api.freelancehunt.com/v2/projects/299178"
        }
      }
    }
"""
from datetime import datetime
from typing import Optional, Type, Union

from ..core import FreelancehuntObject

from .user import Employer, Freelancer, Profile
from .project import Project


__all__ = ('Review',)


class Review(FreelancehuntObject):
    """Create object to provide operations with Project.

    :var int id: review unique identifier
    :var datetime published_at: string representation of the publish date
    :var str comment: comment from creator
    :var dict grades: grades of work quality
    :var Union[Employer,Freelancer] creator: review creator information
    :var bool is_pending: sign that the project is pending
    :var Optional[datetime] pending_ends_at: string representation of the pending date, defaults to None
    :var Optional[Project] ~.project: related project object, defaults to None
    """

    def __init__(self,
                 id: int,
                 published_at: str,
                 comment: str,
                 is_pending: bool,
                 grades: dict,
                 creator: Union[Employer, Freelancer],
                 pending_ends_at: Optional[str] = None,
                 project: Optional[Project] = None,
                 **kwargs):
        """Create object to provide operations with Project.

        :param int id: review unique identifier
        :param str published_at: string representation of the publish date
        :param str comment: comment from creator
        :param dict grades: grades of work quality
        :param Union[Employer, Freelancer] creator: review creator information
        :param bool is_pending: sign that the project is pending
        :param Optional[str] pending_ends_at: string representation of the pending date, defaults to None
        :param Optional[Project] project: related project object, defaults to None
        """
        super().__init__()
        self.id = id
        self.published_at = datetime.fromisoformat(published_at)
        self.comment = comment
        self.is_pending = is_pending
        self.grades = grades
        self.creator = creator
        self.pending_ends_at = (
            datetime.fromisoformat(pending_ends_at) if pending_ends_at else None
        )
        self.project = project
        self.other = kwargs

    @classmethod
    def de_json(cls, **data) -> Type["Review"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        """
        if not data:
            return None

        data["creator"] = Profile.de_json(**data["from"])

        project_info = data.get("project")
        if project_info:
            data["project"] = Project.de_json(**project_info)
        return cls(**data)
