#!usr/bin/python3
"""Feed message object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 1555675871044,
      "type": "feed",
      "attributes": {
        "from": {
          "id": 4,
          "type": "employer",
          "login": "freelancehunt",
          "first_name": "Freelancehunt",
          "last_name": "",
          "avatar": {
            "small": {
              "url": "https://content.freelancehunt.com/profile/photo/50/freelancehunt.png",
              "width": 50,
              "height": 50
            },
            "large": {
              "url": "https://content.freelancehunt.com/profile/photo/225/freelancehunt.png",
              "width": 255,
              "height": 255
            }
          },
          "self": "https://api.freelancehunt.com/v2/employers/4"
        },
        "message": "<img src=\"https://freelancehunt.com/static/images/fugu/new-text.png\" width=\"16\" height=\"16\"/> New message for you.",
        "created_at": "2019-04-19T12:11:11+00:00",
        "is_new": false
      }
    }
"""
from datetime import datetime
from typing import Optional, Type, Union

from ..core import FreelancehuntObject

from .user import Employer, Freelancer, Profile
from .project import Project
from .contest import Contest


__all__ = ('FeedMessage',)


class FeedMessage(FreelancehuntObject):
    """Provide operations with Feed message.

    :var int id: feed message unique identifier
    :var Union[Employer,Freelancer] message_from: message sender user object
    :var str message: the feed message text
    :var str created_at: string representation of the creation date
    :var bool is_new: sign that the message is new
    :var Optional[Project] ~.project: linked project object, defaults to None
    :var Optional[Contest] ~.contest: linked contest object, defaults to None
    """

    def __init__(self,
                 id: int,
                 message_from: Union[Employer, Freelancer],
                 message: str,
                 created_at: str,
                 is_new: bool,
                 project: Optional[Project] = None,
                 contest: Optional[Contest] = None,
                 **kwargs):
        """Create object to provide operations with Feed message.

        :param int id: feed message unique identifier
        :param Union[Employer, Freelancer] message_from: message sender user object
        :param str message: text of feed message
        :param str created_at: string representation of the creation date
        :param bool is_new: check that message is new
        :param Optional[Project] project: linked project object, defaults to None
        :param Optional[Contest] contest: linked contest object, defaults to None
        """
        super().__init__()
        self.id = id
        self.message_from = message_from
        self.message = message
        self.is_new = is_new
        self.created_at = datetime.fromisoformat(created_at)
        self._project = project
        self._contest = contest

    @property
    def sender(self) -> Union[Employer, Freelancer]:
        """Load and get sender information."""
        self.message_from.load_details()
        return self.message_from

    @property
    def type(self) -> str:
        """Check type of Feed message.

        :return: type of Feed message: "project", "contest" or "message".
        """
        if self._project:
            return "project"
        elif self._contest:
            return "contest"
        return "message"

    @property
    def is_project(self) -> bool:
        """Check that Feed message linked to some project."""
        return self.type == "project"

    @property
    def is_contest(self) -> bool:
        """Check that Feed message linked to some contest."""
        return self.type == "contest"

    @property
    def project(self) -> Optional[Project]:
        """Represent the Project linked to this Feed message.

        :return: object of linked Project or None.
        """
        if self._project is not None:
            self._project = self._project.load_details()
        return self._project

    @property
    def contest(self) -> Optional[Contest]:
        """Represent the Contest linked to this Feed message.

        :return: object of linked Contest or None.
        """
        if self._contest is not None:
            self._contest = self._contest.load_details()
        return self._contest

    @classmethod
    def de_json(cls, **data) -> Type["FeedMessage"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `FeedMessage`
        """
        if not data:
            return None

        data["message_from"] = Profile.de_json(**data.pop("from"))

        links = data.get("links")
        if links:
            if "project" in links:
                project_id = links["project"].split('/')[-1]
                data["project"] = Project(project_id)
                data["type"] = "project"
            elif "contest" in links:
                contest_id = links["contest"].split('/')[-1]
                data["contest"] = Contest(contest_id)
                data["type"] = "contest"

        return cls(**data)

    def __str__(self) -> str:
        if self.is_project:
            additional_info = f'(Project #{self._project.id})'
        elif self.is_contest:
            additional_info = f'(Contest #{self._contest.id})'
        else:
            additional_info = '(Not linked)'

        return f'Feed Notification #{self.id} ' + additional_info

    def __repr__(self) -> str:
        if self.is_project:
            additional_info = f'(Project #{self._project.id})'
        elif self.is_contest:
            additional_info = f'(Contest #{self._contest.id})'
        else:
            additional_info = '(Not linked)'

        return f'<freelancehunt.FeedObject #{self.id} {additional_info}>'
