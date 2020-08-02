#!usr/bin/python3
"""Profile object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 77278,
      "type": "freelancer",
      "attributes": {
        "login": "Artemkins",
        "first_name": "Артём",
        "last_name": "Yacuk",
        "avatar": {
          "small": {
            "url": "https://content.freelancehunt.com/profile/photo/50/Artemkins.png",
            "width": 50,
            "height": 50
          },
          "large": {
            "url": "https://content.freelancehunt.com/profile/photo/225/Artemkins.png",
            "width": 255,
            "height": 255
          }
        },
        "birth_date": null,
        "created_at": "2014-09-08T15:21:45+03:00",
        "cv": null,
        "cv_html": null,
        "rating": 31597,
        "rating_position": 1,
        "arbitrages": 0,
        "positive_reviews": 295,
        "negative_reviews": 0,
        "plus_ends_at": null,
        "is_plus_active": true,
        "is_online": false,
        "visited_at": null,
        "location": {
          "country": {
            "id": 1,
            "name": "Ukraine"
          },
          "city": {
            "id": 3184,
            "name": "Kharkiv"
          }
        },
        "verification": {
          "identity": true,
          "birth_date": false,
          "phone": true,
          "website": false,
          "wmid": false,
          "email": false
        },
        "contacts": null,
        "status": {
          "id": 10,
          "name": "Available for hire"
        },
        "skills": [
          {
            "id": 14,
            "name": "Search engine optimization",
            "rating_position": 0
          },
          {
            "id": 127,
            "name": "Contextual advertising",
            "rating_position": 0
          },
          {
            "id": 131,
            "name": "Social media marketing",
            "rating_position": 0
          }
        ]
      },
      "links": {
        "self": {
          "api": "https://api.freelancehunt.com/v2/freelancers/77278",
          "web": "https://freelancehunt.com/freelancer/Artemkins.html"
        },
        "reviews": "https://api.freelancehunt.com/v2/freelancers/77278/reviews"
      }
    }
"""
from datetime import datetime
from typing import List, Optional, Type

from ..core import FreelancehuntObject

from ..models.skill import Skill
from ..models.country import Country
from ..models.city import City


__all__ = ('Profile', 'Employer', 'Freelancer',)


class Profile(FreelancehuntObject):
    """Provide operations with Profile.

    .. note:: Information will be loaded by :py:func:`load_details` if attribute is `None`

    :var int ~.id: unique profile identifier
    :var str login: profile login name
    :var str ~.type: type of account
    :var str first_name: user first name
    :var str last_name: user last name
    :var dict avatar: avatars information, defaults to None
    :var datetime birth_date: string representation of the birth date, defaults to None
    :var str created_at: string representation of the profile create date, defaults to None
    :var str cv: profile summary information, defaults to None
    :var str cv_html: profile summary information in html formatting, defaults to None
    :var int rating: user rating points, defaults to None
    :var int rating_position: user rating position, defaults to None
    :var int arbitrages: count of arbitrages, defaults to None
    :var int positive_reviews: count of positive reviews, defaults to None
    :var int negative_reviews: count of negative reviews, defaults to None
    :var Optional[datetime] plus_ends_at: string representation of the "Plus" status end date, defaults to None
    :var bool is_plus_active: sign that the user has active a "Plus" status, defaults to None
    :var bool is_online: sign that the user is online, defaults to None
    :var datetime visited_at: string representation of the last visited date, defaults to None
    :var dict verification: verification statuses, defaults to None
    :var dict contacts: user contacts (links), defaults to None
    :var List[Skill] ~.skills: user skills, defaults to None
    :var dict links: URLs related to profile, defaults to None
    """

    def __init__(self,
                 id: int,
                 login: str,
                 type: str,
                 first_name: str,
                 last_name: str,
                 avatar: Optional[dict] = None,
                 birth_date: Optional[str] = None,
                 created_at: Optional[str] = None,
                 cv: Optional[str] = None,
                 cv_html: Optional[str] = None,
                 rating: Optional[int] = None,
                 rating_position: Optional[int] = None,
                 arbitrages: Optional[int] = None,
                 positive_reviews: Optional[int] = None,
                 negative_reviews: Optional[int] = None,
                 plus_ends_at: Optional[str] = None,
                 is_plus_active: Optional[bool] = None,
                 is_online: Optional[bool] = None,
                 visited_at: Optional[int] = None,
                 location: Optional[dict] = None,
                 verification: Optional[dict] = None,
                 contacts: Optional[dict] = None,
                 status: Optional[dict] = None,
                 skills: Optional[List[Skill]] = None,
                 links: Optional[dict] = None,
                 **kwargs):
        """Create object to provide operations with Profile.

        :param int id: unique profile identifier
        :param str login: profile login name
        :param str type: type of account
        :param str first_name: user first name
        :param str last_name: user last name
        :param Optional[dict] avatar: avatars information, defaults to None
        :param Optional[str] birth_date: string representation of the birth date, defaults to None
        :param Optional[str] created_at: string representation of the profile create date, defaults to None
        :param Optional[str] cv: profile summary information, defaults to None
        :param Optional[str] cv_html: profile summary information in html formatting, defaults to None
        :param Optional[int] rating: user rating points, defaults to None
        :param Optional[int] rating_position: user rating position, defaults to None
        :param Optional[int] arbitrages: count of arbitrages, defaults to None
        :param Optional[int] positive_reviews: count of positive reviews, defaults to None
        :param Optional[int] negative_reviews: count of negative reviews, defaults to None
        :param Optional[str] plus_ends_at: string representation of the "Plus" status end date, defaults to None
        :param Optional[bool] is_plus_active: sign that the user has active a "Plus" status, defaults to None
        :param Optional[bool] is_online: sign that the user is online, defaults to None
        :param Optional[int] visited_at: string representation of the last visited date, defaults to None
        :param Optional[dict] location: user location, defaults to None
        :param Optional[dict] verification: verification statuses, defaults to None
        :param Optional[dict] contacts: user contacts (links), defaults to None
        :param Optional[dict] status: current availability status, defaults to None
        :param Optional[List[Skill]] skills: user skills, defaults to None
        :param Optional[dict] links: URLs related to profile, defaults to None
        """
        super().__init__()
        self.id = id
        self.login = login
        self.type = type
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        self.cv = cv
        self.cv_html = cv_html
        self.rating = rating
        self.rating_position = rating_position
        self.arbitrages = arbitrages
        self.positive_reviews = positive_reviews
        self.negative_reviews = negative_reviews
        self.is_plus_active = is_plus_active
        self.is_online = is_online
        self.verification = verification
        self.contacts = contacts
        self.links = links
        # Framework objects
        self.skills = skills
        # Will be parsed to objects
        self._status = status
        self._location = location
        # Datetimes
        self.birth_date = (
            datetime.fromisoformat(birth_date)
            if birth_date is not None else None
        )
        self.created_at = (
            datetime.fromisoformat(created_at)
            if created_at is not None else None
        )
        self.visited_at = (
            datetime.fromisoformat(visited_at)
            if visited_at is not None else None
        )
        self.plus_ends_at = (
            datetime.fromisoformat(plus_ends_at)
            if plus_ends_at is not None else None
        )
        # Custom attributes
        self._api_url = f"/{self.type}s/{self.id}"

    @property
    def status(self) -> str:
        """Get current profile status."""
        if not self._status:
            return
        return self._status["name"]

    @property
    def status_code(self) -> int:
        """Get code of profile status."""
        if not self._status:
            return
        return self._status["id"]

    @property
    def country(self) -> Country:
        """Get user country."""
        if not self._location:
            return
        return Country.de_json(**self._location.get("country"))

    @property
    def city(self) -> City:
        """Get user city."""
        if not self._location:
            return
        return City.de_json(**self._location.get("city"))

    @property
    def full_name(self) -> str:
        """Get the full name for the current profile.

        :return: full name of the user
        """
        if not self.first_name and not self.last_name:
            return None
        return f"{self.first_name} {self.last_name}"

    @property
    def profile_url(self) -> str:
        """Get public profile URL.

        :return: public URL for the user
        """
        return f"https://freelancehunt.com/{self.type}/{self.login}.html"

    @property
    def reviews(self) -> List[Type["Review"]]:
        """Get reviews of this profile."""
        from .review import Review
        if not hasattr(self, '_reviews'):
            responce = self._get(self._api_url + '/reviews')
            self._reviews = [Review.de_json(**data) for data in responce]
        return self._reviews

    def load_details(self):
        """Load details about current User and reload all attributes."""
        responce = self._get(self._api_url)
        new = self.de_json(**responce)
        self.__dict__ = new.__dict__

    @classmethod
    def de_json(cls, **data) -> Type["Profile"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        """
        if not data:
            return None

        # Normalize links attribute
        data["links"] = {
            "self": {"api": data.pop("self")}
        } if data.get("self") else data.get('links') or {}
        skills = data.get("skills")

        if skills:
            data["skills"] = [Skill.de_json(**skill) for skill in skills]

        if cls is Profile:
            if data["type"] == "freelancer":
                return Freelancer(**data)
            elif data["type"] == "employer":
                return Employer(**data)
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


class Employer(Profile):
    """Provide operations with Employer profile."""

    def __str__(self):
        return f'Employer {self.id} ({self.full_name})'


class Freelancer(Profile):
    """Provide operations with Freelancer profile."""

    def __str__(self):
        return f'Freelancer {self.id} ({self.full_name})'
