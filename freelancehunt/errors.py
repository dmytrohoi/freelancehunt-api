#!usr/bin/python3
"""#TODO: Write comments."""


__all__ = [
    'UnexpectedError',
    'AuthenticationError',
    'ValidationError',
    'APIRespondingError',
    'NotEmployerError'
]


class Error(Exception):
    """Base class for errors in this module."""
    pass


class UnexpectedError(Error):
    """Error not recognized by framework."""
    pass


class AuthenticationError(Error):
    """Authentication error raised by API server."""
    pass


class ValidationError(Error):
    """Some fields in POST data is not validated by server."""
    pass


class APIRespondingError(Error):
    """FreelanceHunt API is not responding now."""
    pass


class NotEmployerError(Error):
    """Client are not employer."""
    pass


class BadRequestError(Error):
    """Bad request to server."""
    pass
