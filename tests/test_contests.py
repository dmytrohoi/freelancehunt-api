#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt import Contests
from freelancehunt.models.contest import ContestEntity


class Contests:

    def __init__(self, token=None, **kwargs):
        pass


class ContestEntity:

    def __init__(self, id, name=None, budget=None, status=None,
                 description=None, description_html=None, skills=None,
                 final_started_at=None, employer=None, application_count=None,
                 freelancer=None, updates=None, published_at=None, links=None,
                 duration_days=None, **kwargs):
        pass

    def load_details(self):
        pass

    #classmethod
    def de_json(cls, **data):
        pass
