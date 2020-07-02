#!usr/bin/python3
"""#TODO: Write comments."""
from datetime import datetime

from ..core import FreelancehuntObject

from .user import UserEntity
from .project import ProjectEntity
from .contest import ContestEntity


__all__ = ('FeedEntity',)


class FeedEntity(FreelancehuntObject):

    def __init__(self, id, message_from, message, created_at, is_new,
                 project=None, contest=None, **kwargs):
        super().__init__()
        self.id = id
        self.message_from = message_from
        self.message = message
        self.is_new = is_new
        self.created_at = datetime.fromisoformat(created_at)
        self._project = project
        self._contest = contest

    @property
    def project(self):
        if self._project is not None:
            self._project = self._project.load_details()
        return self._project

    @property
    def contest(self):
        if self._contest is not None:
            self._contest = self._contest.load_details()
        return self._contest

    @classmethod
    def de_json(cls, **data):
        if not data:
            return None

        data["message_from"] = UserEntity.de_json(**data.pop("from"))

        links = data.get("links")
        if links:
            if "project" in links:
                project_id = links["project"].split('/')[-1]
                data["project"] = ProjectEntity(project_id)
                data["type"] = "project"
            elif "contest" in links:
                contest_id = links["contest"].split('/')[-1]
                data["contest"] = ContestEntity(contest_id)
                data["type"] = "contest"

        return cls(**data)

    def __str__(self):
        if getattr(self, '_project'):
            additional_info = f'(Project #{self._project.id})'
        elif getattr(self, '_contest'):
            additional_info = f'(Contest #{self._contest.id})'
        else:
            additional_info = '(Not linked)'

        return f'Feed Notification #{self.id} ' + additional_info

    def __repr__(self):
        if getattr(self, '_project'):
            additional_info = f'(Project #{self._project.id})'
        elif getattr(self, '_contest'):
            additional_info = f'(Contest #{self._contest.id})'
        else:
            additional_info = '(Not linked)'

        return f'<freelancehunt.FeedObject #{self.id} {additional_info}>'
