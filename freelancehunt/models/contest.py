#!usr/bin/python3
"""Main file of FreelanceHunt API framework."""
from __future__ import annotations
from typing import List, Optional, Type
from datetime import datetime

from ..core import FreelancehuntObject

from .user import EmployerEntity, FreelancerEntity
from .skill import SkillEntity

__all__ = [
    'ContestEntity'
]

class ContestEntity(FreelancehuntObject):

    def __init__(
        self,
        id_: int,
        name: Optional[str] = None,
        budget: Optional[dict] = None,
        status: Optional[str] = None,
        description: Optional[str] = None,
        description_html: Optional[str] = None,
        skills: Optional[List[SkillEntity]] = None,
        final_started_at: Optional[str] = None,
        employer: Optional[EmployerEntity] = None,
        application_count: Optional[str] = None,
        freelancer: Optional[FreelancerEntity] = None,
        updates: Optional[list] = None,
        published_at: Optional[str] = None,
        links: Optional[dict] = None,
        duration_days: Optional[int] = None,
        **kwargs
    ):

        super().__init__()
        self.id = id_
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
        """Load details about current Contest and reload all attributes.

        :return: None
        :rtype: None
        """
        responce = self._get(self.api_url)
        self = self.de_json(**responce)
        return self

    @classmethod
    def de_json(cls, **data: [None, dict]) -> Type[ContestEntity]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: ContestEntity
        """
        if not data:
            return None

        data["skills"] = [SkillEntity.de_json(**skill) for skill in data["skills"]]
        data["employer"] = EmployerEntity.de_json(**data["employer"])
        if data["freelancer"]:
            data["freelancer"] = FreelancerEntity.de_json(**data["freelancer"])
        return cls(**data)
