#!usr/bin/python3
"""#TODO: Write comments."""
from datetime import datetime

from .base import FreelancehuntObject
from .user import EmployerEntity, FreelancerEntity
from .skills import SkillEntity

from .errors import BadRequestError

__all__ = [
    'Projects',
    'ProjectEntity'
]


class Projects(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)

    @property
    def list(self):
        """List of last 10 projects."""
        return self.get()

    def get(self, skills=None, employer_id=None, only_for_plus=None, pages=1):
        """
        Get projects with filter and from multiple pages.

        Args:
            skills (int, str, list):
            employer_id (int):
            only_for_plus (bool):
            page (int, tuple or list):

        Return:
            list:

        """
        filters = {
            "employer_id": employer_id
        }
        if only_for_plus:
            filters.update({
                "only_for_plus": int(only_for_plus)
            })
        # Get skills as: int, str, Skill object, or list of str/int/Skill obj
        if skills:
            # One SkillEntity passed
            if isinstance(skills, SkillEntity):
                skills_filter_str = str(skills.id)

            # Stringify single value
            elif isinstance(skills, (str, int)):
                skills_filter_str = str(skills)

            # List object passed
            elif isinstance(skills, list):
                if isinstance(skills[0], SkillEntity):
                    skills = [skill.id for skill in skills]
                # Stringify all values in list
                skill_list = [str(skill_id) for skill_id in skills]
                skills_filter_str = ','.join(skill_list)
            # Add skill_id to filters dict
            filters.update({"skill_id": skills_filter_str})

        responce = self._multi_page_get('/projects', filters, pages)
        return [ProjectEntity.de_json(**data) for data in responce]

    @property
    def my_projects(self):
        """
        Get my projects list (10 objects).

        NOTE: ONLY FOR EMPLOYER!
        Bad request raises when you are not Employer.

        """
        responce = self._get("/my/projects")
        return [ProjectEntity.de_json(**data) for data in responce]

    def get_project(self, project_id):
        """
        Get specific project by id.

        Arguments:
            project_id (int): id of the desired project.

        Return:
            Project object: the desired project object.

        """
        responce = self._get(f"/projects/{project_id}")
        return ProjectEntity.de_json(**responce)

    def create_project(self, information):
        pass


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
