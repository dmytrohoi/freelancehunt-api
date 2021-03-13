#!usr/bin/python3
"""All custom errors."""
from .common import StatusCodes

__all__ = (
    'UnexpectedError',
    'AuthenticationError',
    'ValidationError',
    'APIRespondingError',
    'NotEmployerError',
)


def handle_errors(status_code: int, request_url: str, json_data: dict):
    """
    Handle errors in responce data and throw custom API error for some
    common types of error.

    :param status_code: responce status code for request.
    :param request_url: URL to request.
    :parma json_data: responce data in dictionary.
    """
    # No errors found and no content returned
    if status_code in [StatusCodes.SUCCESS, StatusCodes.CREATED, StatusCodes.NO_CONTENT]:
        return

    # Specific error messages constants
    API_NOT_RESPONDING = "Version 2 is not supported"
    # Error attributes shortcuts
    error_title = json_data.get("error")["title"]
    error_detail = json_data["error"].get("detail")

    # Not employer errors check
    if status_code == StatusCodes.BAD_REQUEST and '/my/projects' in request_url:
        # TODO: Check all possible restricted urls
        raise NotEmployerError("Look's like you are not employer.")

    # Unauthorized
    elif status_code == StatusCodes.UNAUTH:
        raise AuthenticationError(
            "Please check your token, look's like is not valid:",
            error_title, error_detail
        )
    # Validation error for POST data
    elif status_code == StatusCodes.UNPROCESSABLE:
        raise ValidationError(error_title, error_detail)
    # Check API availability error
    elif status_code == StatusCodes.NOT_FOUND and error_detail == API_NOT_RESPONDING:
        raise APIRespondingError(
            "API not responding now, please try again later."
        )
    else:
        raise UnexpectedError(error_title, error_detail)


class FreelancehuntError(Exception):
    """Base class for errors in this module."""
    pass


class UnexpectedError(FreelancehuntError):
    """Error not recognized by framework."""
    pass


class AuthenticationError(FreelancehuntError):
    """Authentication error raised by API server."""
    pass


class ValidationError(FreelancehuntError):
    """Some fields in POST data is not validated by server."""
    pass


class APIRespondingError(FreelancehuntError):
    """FreelanceHunt API is not responding now."""
    pass


class NotEmployerError(FreelancehuntError):
    """Client are not employer."""
    pass


class BadRequestError(FreelancehuntError):
    """Bad request to server."""
    pass
