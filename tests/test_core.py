#!usr/bin/python3
"""Basic classes for API objects."""
from freelancehunt.core import FreelancehuntObject


class FreelancehuntObject:
    """Parent class for all parts of API."""
    requester = None

    def __init__(self, token=None, **kwargs):
        pass

    def _get(self, url, filters=None, page=None):
        pass

    def _multi_page_get(self, url, filters=None, pages=None):
        pass

    def _post(self, url, payload=None):
        pass

    def __parse_data(self, data: dict):
        pass
