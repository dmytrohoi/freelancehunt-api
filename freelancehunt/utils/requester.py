#!usr/bin/python3
"""Requests singleton."""
from typing import Type
import requests
from datetime import datetime
from simplejson.errors import JSONDecodeError

from .errors import AuthenticationError, ValidationError, APIRespondingError, \
                   NotEmployerError, UnexpectedError


__all__ = ('Requester',)


class Requester:
    """Provides requests to API. Singleton."""

    # Object singleton
    __requester = None
    # Public attributes
    token = None
    limit = None
    request_date = None
    # Private attributes
    __basic_url = "https://api.freelancehunt.com/v2"
    __headers = None

    def __new__(cls, token=None, *args, **kwargs):
        """Get or create Requester singleton object.

        :param Optional[str] token: user personal access token.
        :return: Requester object.
        :rtype: Requester
        """
        if not cls.__requester and not token:
            raise AttributeError(
                'Requester object not found, please give your API token '
                'to initiate it.'
            )
        elif token:
            cls.__requester = super().__new__(*args, **kwargs)
        return cls.__requester



    def __init__(self, token, language='en', **kwargs):
        """Set general parameters for all requests.

        :param str token: user personal access token.
        :param str language: language of responced data, default to 'en'.
        """
        self.token = token
        self.__headers = {'Authorization': f'Bearer {self.token}'}
        if language in ['en', 'ru', 'uk']:
            self.__headers['Accept-Language'] = language

    def request(self, request_type, url, filters=None, payload=None, headers={}, files=None) -> dict:
        """Make request to API and handle results.

        :param str request_type: request type ("POST", "GET", "PATCH" or "DEL").
        :param Optional[dict] filters: get parameter query, default to None.
        :param Optional[dict] payload: get parameter query, default to None.
        :param Optional[dict] headers: custom headers for request, default to None.
        :param Optional[dict] files: files to post attachment, default to None.
        :return: JSON responce data in dict
        :rtype: dict
        """
        # Serialize object of dataclasses to JSON
        if payload and not isinstance(payload, dict):
            payload = payload.__dict__
        # Make filters params for GET requests
        if filters and request_type == "GET":
            # Skip no value filters
            allowed_filters = {
                name: value
                for name, value in filters.items()
                if value
            }
            if allowed_filters:
                # Pop page number
                page_num = allowed_filters.pop('page[number]')
                filters = {
                    f'filter[{name}]': param
                    for name, param in allowed_filters.items()
                }
                # Add page filter to params
                if page_num:
                    filters.update({'page[number]': page_num})
            else:
                filters = None

        request_headers = self.__headers.copy()
        request_headers.update(headers)

        request_url = self.__basic_url + url

        if payload:
            data = {'json': payload}
        elif files:
            data = {'files': files}
        else:
            data = {}

        responce = requests.request(
            method=request_type,
            url=request_url,
            params=filters,
            headers=request_headers,
            **data
        )

        json_data = None
        if request_type not in ["DELETE"]:
            # No value in some POST request
            try:
                json_data = responce.json()
            except JSONDecodeError as E:
                if request_type != "POST":
                    raise E
                json_data = {}

        # Handling errors
        self._handle_errors(responce.status_code, request_url, json_data)

        # Set requests limit
        self._set_current_limit(responce.headers)

        return json_data

    def _handle_errors(self, status_code, request_url, json_data):
        """
        Handle errors in responce data and throw custom API error for some
        common types of error.

        :param int status_code: responce status code for request.
        :param str request_url: url for request.
        :param dict json_data: responce data in dictionary.
        """
        # No errors found and no content returned
        if status_code // 100 == 2:
            return

        # Specific error messages constants
        API_NOT_RESPONDING = "Version 2 is not supported"
        # Error attributes shortcuts
        error_title = json_data.get("error")["title"]
        error_detail = json_data["error"].get("detail")

        # Not employer errors check
        if status_code == 400 and '/my/projects' in request_url:
            # TODO: Check all possible restricted urls
            raise NotEmployerError("Look's like you are not employer.")

        # Unauthorized
        elif status_code == 401:
            raise AuthenticationError(
                "Please check your token, look's like is not valid:",
                error_title, error_detail
            )
        # Validation error for POST data
        elif status_code == 422:
            raise ValidationError(error_title, error_detail)
        # Check API availability error
        elif status_code == 404 and error_detail == API_NOT_RESPONDING:
            raise APIRespondingError(
                "API not responding now, please try again later."
            )
        else:
            raise UnexpectedError(error_title, error_detail)

    def _set_current_limit(self, headers):
        """Store API limitation from responce headers.

        :param dict headers: responce headers.
        """
        date_pattern = "%a, %d %b %Y %H:%M:%S %Z"
        self.request_date = datetime.strptime(headers.get("Date"), date_pattern)
        self.limit = int(headers.get("X-RateLimit-Remaining"))

    @classmethod
    def get_requester(cls, token=None, **kwargs) -> Type["Requester"]:
        """Get or create Requester singleton object.

        .. note: a method of implementing singleton pattern.

        :param Optional[str] token: user personal access token.
        :return: Requester object.
        :rtype: Requester
        """
        if not cls.__requester and not token:
            raise AttributeError(
                'Requester object not found, please give your API token '
                'to initiate it.'
            )
        elif not cls.__requester or token:
            cls.__requester = cls(token, **kwargs)
        return cls.__requester
