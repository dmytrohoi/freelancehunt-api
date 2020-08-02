#!usr/bin/python3
"""All custom errors."""


__all__ = (
    'UnexpectedError',
    'AuthenticationError',
    'ValidationError',
    'APIRespondingError',
    'NotEmployerError',
)


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
