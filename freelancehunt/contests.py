#!usr/bin/python3
"""#TODO: Write comments."""
from datetime import datetime

from .base import FreelancehuntObject
from .user import EmployerEntity, FreelancerEntity


__all__ = [
    'Contests',
    'ContestEntity'
]


class Contests(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        """TODO: Write comments."""
        super().__init__(token, **kwargs)


class ContestEntity(FreelancehuntObject):

    def __init__(self, id, name=None, budget=None, status=None,
                 description=None, description_html=None, skills=None,
                 final_started_at=None, employer=None, application_count=None,
                 freelancer=None, updates=None, published_at=None, links=None,
                 duration_days=None, **kwargs):
        super().__init__()
        self.id = id
        self.name = name
        self.budget = budget
        self.skills = skills
        self.status = status
        self.description = description
        self.description_html = description_html
        self.application_count = application_count
        self.employer = employer
        self.freelancer = freelancer
        self.updates = updates
        self.duration_days = duration_days
        self.final_started_at = datetime.fromisoformat(final_started_at) \
                                if final_started_at is not None else None
        self.published_at = datetime.fromisoformat(published_at) \
                            if published_at is not None else None
        self.links = links

        # Custom attributes
        self.api_url = f"/contests/{self.id}"

    def load_details(self):
        responce = self._get(self.api_url)
        self = self.de_json(**responce)
        return self

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        data["employer"] = EmployerEntity.de_json(**data["employer"])
        if data["freelancer"]:
            data["freelancer"] = FreelancerEntity.de_json(**data["freelancer"])
        return cls(**data)
