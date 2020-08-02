#!usr/bin/python3
"""`Freelancehunt Documentation - Projects API <https://apidocs.freelancehunt.com/?version=latest#54939f33-1e54-4953-b199-a63893886fed>`_."""
from typing import List, Optional, Tuple, Union

from ..core import FreelancehuntObject

from ..models.skill import Skill
from ..models.project import Project


__all__ = ('Projects',)


class Projects(FreelancehuntObject):
    """Provide operations with Projects API part.

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Projects API part.

        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)

    def get_list(self,
                 pages: Union[int, Tuple[int], List[int]] = 1,
                 only_for_plus: bool = False,
                 skills: Optional[
                     Union[int, str, Skill, List[Skill],
                           List[int], Tuple[Skill], Tuple[int]]
                 ] = None,
                 employer_id: Optional[int] = None) -> List[Project]:
        """Get projects with filter and from multiple pages.

        :param skills: filter by skills
        :param employer_id: projects from employer with id
        :param only_for_plus: filter only for plus if False, get otherwise, defaults is False
        :param pages: number of pages to get, defaults - 1
        """
        filters = {}
        if employer_id:
            filters.update({
                "employer_id": employer_id
            })

        if only_for_plus:
            filters.update({
                "only_for_plus": int(only_for_plus)
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

        responce = self._multi_page_get('/projects', filters, pages)
        return [Project.de_json(**data) for data in responce]

    def my_projects(self, pages: Union[int, Tuple[int], List[int]] = 1) -> List[Project]:
        """Get my projects list (10 objects).

        .. note: ONLY FOR EMPLOYER!

        :param pages: number of pages, defaults to 1
        :raise BadRequest: raises when you are not Employer.
        """
        responce = self._multi_page_get("/my/projects", pages=pages)
        return [Project.de_json(**data) for data in responce]

    def get_project(self, project_id: int) -> Project:
        """Get specific project by id.

        :param project_id: id of the desired project.
        :return: the desired project object.
        """
        responce = self._get(f"/projects/{project_id}")
        return Project.de_json(**responce)

    def create_project(self, information: dict) -> Project:
        """Create new project on site.

        TBD: Implement a convenient way to create a project.

        .. note: ONLY FOR EMPLOYER! Can be used only by verified profiles.

        :param information: required and optional params of new project
                (link: https://apidocs.freelancehunt.com/?version=latest#ff11ae15-05af-4ee8-ae7c-155cd137506f)
        :return: representation of created project.
        """
        responce = self._post("/projects", payload=information)
        return Project.de_json(**responce)

