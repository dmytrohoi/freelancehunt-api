#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt import Skills
from freelancehunt.models.skill import Skill


class Skills:

    def __init__(self, token=None, **kwargs):
        pass

    def update(self):
        pass

    #property
    def list(self):
        pass

    def get(self, skill_id):
        pass

    def find(self, text):
        pass

class SkillEntity:

    def __init__(self, id, name, **kwargs):
        pass

    def de_json(cls, **data):
        pass
