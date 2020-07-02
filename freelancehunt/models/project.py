#!usr/bin/python3
"""#TODO: Write comments."""
from datetime import datetime

from ..core import FreelancehuntObject
from .user import EmployerEntity, FreelancerEntity
from .skill import SkillEntity

from ..utils.errors import BadRequestError


__all__ = ('ProjectEntity',)


class ProjectEntity(FreelancehuntObject):

    def __init__(self, id, name=None, budget=None, safe_type=None, status=None,
                 description=None, description_html=None, skills=None,
                 expired_at=None, employer=None,  bid_count=None,
                 is_remote_job=None, is_premium=None, is_only_for_plus=None,
                 is_personal=None, freelancer=None, updates=None,
                 location=None, published_at=None, links=None, **kwargs):
        super().__init__()
        self.id = id
        self.name = name
        self.budget = budget
        self.safe_type = safe_type
        self.skills = skills
        self.description = description
        self.description_html = description_html
        self.bid_count = bid_count
        self.is_remote_job = is_remote_job
        self.is_premium = is_premium
        self.is_only_for_plus = is_only_for_plus
        self.is_personal = is_personal
        self.employer = employer
        self.freelancer = freelancer
        self.updates = updates
        self.location = location
        self.expired_at = datetime.fromisoformat(expired_at) \
                          if expired_at is not None else None
        self.published_at = datetime.fromisoformat(published_at) \
                            if published_at is not None else None
        self._links = links

        self._status = status
        # Custom attributes
        self.api_url = f"/projects/{self.id}"

    @property
    def status(self):
        return self._status["name"]

    @property
    def status_code(self):
        return self._status["id"]

    def close(self):
        try:
            self._post(self.api_url + '/close')
        except BadRequestError:
            return False
        return True

    def reopen(self):
        try:
            self._post(self.api_url + '/reopen')
        except BadRequestError:
            return False
        return True

    def extend(self, expired_at: datetime):
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
        return self._links["web"]

    def load_details(self):
        responce = self._get(self.api_url)
        self = self.de_json(**responce)
        return self

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        # NOTE: Can be None for plus_only projects
        employer = data.get("employer")
        if employer:
            data["employer"] = EmployerEntity.de_json(**data["employer"])

        freelancer = data.get("freelancer")
        if freelancer:
            data["freelancer"] = FreelancerEntity.de_json(**data["freelancer"])
        return cls(**data)

    def __str__(self):
        employer = self.employer.full_name \
                   if getattr(self, 'employer') is not None \
                   else 'Secret (Plus accounts only)'
        return f'Project #{self.id} by {employer} ({self.status})'

    def __repr__(self):
        employer = self.employer.id \
                   if getattr(self, 'employer') is not None \
                   else 'Secret (Plus accounts only)'
        return f'<freelancehunt.Project #{self.id} (Employer '\
               f'#{employer} Status: {self.status_code})>'
