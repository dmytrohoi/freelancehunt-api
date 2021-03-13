#!usr/bin/python3
"""TODO: Write comments."""
from freelancehunt import Requester


class Requester:
    """TODO: Write comments."""
    # Object singleton
    __requester = None
    # Public attributes
    token = None
    limit = None
    request_date = None
    # Private attributes
    __basic_url = "https://api.freelancehunt.com/v2"
    __headers = None

    def __init__(self, token, language='en', **kwargs):
        pass

    def request(self, request_type, url, filters=None, payload=None):
        pass

    def _set_current_limit(self, headers):
        pass

    def get_requester(cls, token=None, **kwargs):
        pass
