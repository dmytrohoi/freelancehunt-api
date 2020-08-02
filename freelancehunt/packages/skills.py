#!usr/bin/python3
"""`Freelancehunt Documentation - Skills API <https://apidocs.freelancehunt.com/?version=latest#bd98872f-122d-4904-8195-3e3fb2c36340>`_."""
from typing import List, Optional

from ..core import FreelancehuntObject

from ..models.skill import Skill

__all__ = ('Skills',)


class Skills(FreelancehuntObject):
    """Provide operations with Skills API part.

    .. note:: This module contains static content. It may be `update()`, but loaded info does not change on the API side.

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Skills API part.

        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)

    def update(self):
        """Update static information from API."""
        responce = self._get('/skills')
        self._skills = [
            Skill.de_json(**skill)
            for skill in responce
        ]

    @property
    def list(self) -> List[Skill]:
        """Get list of all skills.

        :return: list of skills
        """
        if not hasattr(self, '_skills'):
            self.update()
        return self._skills

    def get(self, skill_id: int) -> Skill:
        """Get the desired skill by API-related identifier.

        :param skill_id: identifier of the desired skill.
        :return: the desired skill
        """
        filtered_list = list(filter(lambda sk: sk.id == skill_id, self.list))
        if len(filtered_list) < 1:
            raise ValueError(f'Skill with id {skill_id} not found')

        return filtered_list[0]

    def find(self, text: str) -> List[Skill]:
        """Find the names of the skill that contain the desired text.

        :param text: the desired text that need to be in an skill name.
        :raises ValueError: Skill not found.
        :return: list of skills with an text in name.
        """
        filtered_list = list(filter(lambda sk: text in sk.name, self.list))
        if len(filtered_list) < 1:
            raise ValueError(f'Skill with text {text} not found')

        return filtered_list
