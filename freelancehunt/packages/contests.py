#!usr/bin/python3
"""`Freelancehunt Documentation - Contests API <https://apidocs.freelancehunt.com/?version=latest#28c10a97-5d31-4857-b526-39466229c885>`_."""
from freelancehunt.models.skill import Skill
from typing import List, Optional, Tuple, Union
from ..core import FreelancehuntObject

from ..models.contest import Contest


__all__ = ('Contests',)


class Contests(FreelancehuntObject):
    """Provide operations with Contests API part.

    .. warning:: For directly usage please set `token` argument.

        **token** (`str`) your API token, optional

    """

    def __init__(self, **kwargs):
        """Create object to provide operations with Contests API part."""
        super().__init__(**kwargs)

    def get_list(self,
                 pages: Union[int, Tuple[int], List[int]] = 1,
                 skills: Optional[
                     Union[int, str, Skill, List[Skill],
                           List[int], Tuple[Skill], Tuple[int]]
                 ] = None,
                 employer_id: Optional[int] = None) -> List[Contest]:
        """Get contests with filter and from multiple pages.

        :param skills: filter by skills
        :param employer_id: contests from employer with id
        :param pages: number of pages to get, defaults - 1
        """
        filters = {}
        if employer_id:
            filters.update({
                "employer_id": employer_id
            })

        # Get skills as: int, str, Skill object, or list of str/int/Skill obj
        if skills:
            # One Skill passed
            if isinstance(skills, Skill):
                skills_filter_str = str(skills.id)

            # Stringify single value
            elif isinstance(skills, int):
                skills_filter_str = str(skills)

            # List object passed
            elif isinstance(skills, list):
                if isinstance(skills[0], Skill):
                    skills = [skill.id for skill in skills]
                # Stringify all values in list
                skill_list = [str(skill_id) for skill_id in skills]
                skills_filter_str = ','.join(skill_list)
            elif isinstance(skills, str):
                skills_filter_str = skills
            else:
                raise ValueError('Unaccepted type of "skills" param.')

            # Add skill_id to filters dict
            filters.update({"skill_id": skills_filter_str})

        responce = self._multi_page_get('/contests', filters, pages)
        return [Contest.de_json(**data) for data in responce]

    def my_contests(self,
                    skills: Optional[
                        Union[int, str, Skill, List[Skill],
                              List[int], Tuple[Skill], Tuple[int]]
                    ] = None,
                    status_id: Optional[int] = None,
                    pages: Union[int, Tuple[int], List[int]] = 1) -> List[Contest]:
        """Get my contests list (up to 10 objects per page).

        .. note: ONLY FOR EMPLOYER!

        :param skills: filter by skills
        :param status_id: contests with the desired status
        :param pages: number of pages, defaults to 1
        :raise BadRequest: raises when you are not Employer.
        """
        filters = {}
        if status_id:
            filters.update({
                "status_id": status_id
            })

        # Get skills as: int, str, Skill object, or list of str/int/Skill obj
        if skills:
            # One Skill passed

            if isinstance(skills, Skill):
                skills_filter_str = str(skills.id)

            # Stringify single value
            elif isinstance(skills, int):
                skills_filter_str = str(skills)

            # List object passed
            elif isinstance(skills, list):
                if isinstance(skills[0], Skill):
                    skills = [skill.id for skill in skills]
                # Stringify all values in list
                skill_list = [str(skill_id) for skill_id in skills]
                skills_filter_str = ','.join(skill_list)
            elif isinstance(skills, str):
                skills_filter_str = skills
            else:
                raise ValueError('Unaccepted type of "skills" param.')

            # Add skill_id to filters dict
            filters.update({"skill_id": skills_filter_str})

        responce = self._multi_page_get("/my/contests", pages=pages)
        return [Contest.de_json(**data) for data in responce]

    def get_contest(self, contest_id: int) -> Contest:
        """Get specific contest by id.

        :param project_id: id of the desired project.
        :return: the desired project object.
        """
        responce = self._get(f"/contests/{contest_id}")
        return Contest.de_json(**responce)
