#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt import Projects
from freelancehunt.models.project import ProjectEntity


class Projects:

    def __init__(self, token=None, **kwargs):
        pass

    #property
    def list(self):
        pass

    def get(self, skills=None, employer_id=None, only_for_plus=None, pages=1):
        pass

    #property
    def my_projects(self):
        pass

    def get_project(self, project_id):
        pass

    def create_project(self, information):
        pass

class ProjectEntity:

    def __init__(self, id, name=None, budget=None, safe_type=None, status=None,
                 description=None, description_html=None, skills=None,
                 expired_at=None, employer=None,  bid_count=None,
                 is_remote_job=None, is_premium=None, is_only_for_plus=None,
                 is_personal=None, freelancer=None, updates=None,
                 location=None, published_at=None, links=None, **kwargs):
        pass

    #property
    def status(self):
        pass

    #property
    def status_code(self):
        pass

    def close(self):
        pass

    def reopen(self):
        pass

    def extend(self, expired_at):
        pass

    #property
    def link(self):
        pass

    def load_details(self):
        pass

    def de_json(cls, **data):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
