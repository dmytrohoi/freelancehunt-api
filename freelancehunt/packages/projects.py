#!usr/bin/python3
"""#TODO: Write comments."""
from datetime import datetime

from ..core import FreelancehuntObject

from ..models.skill import SkillEntity
from ..models.project import ProjectEntity


__all__ = ('Projects',)


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

