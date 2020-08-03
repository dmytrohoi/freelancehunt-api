#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt import Feed
from freelancehunt.models.feed import FeedMessage


class Feed:

    def __init__(self, token=None, **kwargs):
        pass

    def update(self):
        pass

    def read(self):
        pass

    #property
    def projects(self):
        pass

    #property
    def contests(self):
        pass

    def get_new(self):
        pass

    #property
    def list(self):
        pass


class FeedEntity:

    def __init__(self, id, message_from, message, created_at, is_new,
                 project=None, contest=None, **kwargs):
        pass

    #property
    def project(self):
        pass

    #property
    def contest(self):
        pass

    #classmethod
    def de_json(cls, **data):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
