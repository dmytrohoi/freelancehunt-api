#!usr/bin/python3
"""#TODO: Write comments."""
from datetime import datetime

from .base import FreelancehuntObject
from .reviews import ReviewEntity


__all__ = [
    'UserEntity',
    'EmployerEntity',
    'FreelancerEntity'
]


class UserEntity(FreelancehuntObject):
    def __init__(self, id, login, type, first_name, last_name, avatar=None,
                 birth_date=None, created_at=None, cv=None, cv_html=None,
                 rating=None, rating_position=None, arbitrages=None,
                 positive_reviews=None, negative_reviews=None,
                 plus_ends_at=None, is_plus_active=None, is_online=None,
                 visited_at=None, location=None, verification=None,
                 contacts=None, status=None, skills=None, links=None,
                 **kwargs):
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
        self.plus_ends_at = plus_ends_at
        self.is_plus_active = is_plus_active
        self.is_online = is_online
        self.location = location
        self.verification = verification
        self.contacts = contacts
        self.status = status
        self.skills = skills
        self.birth_date = datetime.fromisoformat(birth_date) \
                          if birth_date is not None else None
        self.created_at = datetime.fromisoformat(created_at) \
                          if created_at is not None else None
        self.visited_at = datetime.fromisoformat(visited_at) \
                          if visited_at is not None else None
        self.links = links

        # Custom attributes
        self.api_url = f"/{self.type}s/{self.id}"

    @property
    def full_name(self):
        if not self.first_name and not self.last_name:
            return None
        return f"{self.first_name} {self.last_name}"

    @property
    def profile_url(self):
        return f"https://freelancehunt.com/{self.type}/{self.login}.html"

    @property
    def reviews(self):
        if not hasattr(self, '_reviews'):
            responce = self._get(self.api_url + '/reviews')
            self._reviews = [ReviewEntity.de_json(**data) for data in responce]
        return self._reviews

    def load_details(self):
        responce = self._get(self.api_url)
        self = self.de_json(**responce)
        return self

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        # Normalize links attribute
        data["links"] = {"self": {"api": data.pop("self")}} \
                        if data.get("self") else data.get('links') or {}

        if cls is UserEntity:
            if data["type"] == "freelancer":
                return FreelancerEntity(**data)
            elif data["type"] == "employer":
                return EmployerEntity(**data)
        return cls(**data)


class EmployerEntity(UserEntity):

    def __str__(self):
        return f'Employer {self.id} ({self.full_name})'


class FreelancerEntity(UserEntity):

    def __str__(self):
        return f'Freelancer {self.id} ({self.full_name})'
