from typing import List
from dataclasses import dataclass


def filter_list_by_attr(objs: List["FreelancehuntObject"], attr: str) -> List["FreelancehuntObject"]:
    """Filters list by a object attribute.

    :param objs: list of objects to filter.
    :param attr: the attribute to be contained in the object.
    :return: list of filtered objects.
    """
    return list(filter(lambda obj: getattr(obj, attr), objs))


@dataclass
class StatusCodes:
    """HTTP status codes."""
    SUCCESS = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTH = 401
    NOT_FOUND = 404
    UNPROCESSABLE = 422
