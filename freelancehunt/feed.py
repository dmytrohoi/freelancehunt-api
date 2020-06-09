#!usr/bin/python3
"""#TODO: Write comments."""
from datetime import datetime

from .base import FreelancehuntObject
from .user import UserEntity
from .projects import ProjectEntity
from .contests import ContestEntity


__all__ = [
    'Feed',
    'FeedEntity'
]


class Feed(FreelancehuntObject):
    """"""
    _latest_feed = []

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)

    def update(self):
        """Get latest feed information."""
        responce = self._get('/my/feed')
        self._latest_feed = [
            FeedEntity.de_json(**message)
            for message in responce
        ]

    def read(self):
        """Mark feed as read."""
        return self._post('/my/feed/read')

    @property
    def projects(self):
        """Get all projects in feed."""
        return self._filter_list_by_attr(self.list, '_project')

    @property
    def contests(self):
        """Get all contests in feed."""
        return self._filter_list_by_attr(self.list, '_contest')

    def get_new(self):
        """Get all new notifications in feed."""
        return self._filter_list_by_attr(self.list, 'is_new')

    @property
    def list(self):
        if not self._latest_feed:
            self.update()
        return self._latest_feed


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
