#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject

from ..models.skill import SkillEntity

__all__ = ('Skills',)


class Skills(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)

    def update(self):
        responce = self._get('/skills')
        self._skills = [
            SkillEntity.de_json(**skill)
            for skill in responce
        ]

    @property
    def list(self):
        if not hasattr(self, '_skills'):
            self.update()
        return self._skills

    def get(self, skill_id):
        filtered_list = list(filter(lambda sk: sk.id == skill_id, self.list))
        if len(filtered_list) < 1:
            raise ValueError(f'Skill with id {skill_id} not found')

        return filtered_list[0]

    def find(self, text):
        filtered_list = list(filter(lambda sk: text in sk.name, self.list))
        if len(filtered_list) < 1:
            raise ValueError(f'Skill with text {text} not found')

        return filtered_list
