#!usr/bin/python3
"""`Freelancehunt Documentation - Threads API <https://apidocs.freelancehunt.com/?version=latest#a313684a-aa56-4f67-bb4c-5ba014c43006>`_."""
from typing import List, Optional, Tuple, Union

from ..core import FreelancehuntObject

from ..models.thread import Thread


__all__ = ('Threads',)


class Threads(FreelancehuntObject):
    """Provide operations with Threads API part.

    .. warning:: For directly usage please set `token` argument.

        **token** (`str`) your API token, optional

    """

    def __init__(self, **kwargs):
        """Create object to provide operations with Threads API part."""
        super().__init__(**kwargs)

    def get_threads(self, pages: Union[int, Tuple[int], List[int]] = 1) -> List[Thread]:
        """Get list of threads.

        :param Union[int, Tuple[int], List[int]] pages: count of pages to get, defaults to 1
        """
        responce = self._multi_page_get("/threads", pages=pages)
        return [Thread.de_json(**data) for data in responce]

    def create_thread(self, to_profile_id: int, subject: str, message_html: str) -> Thread:
        """Create new thread.

        :param int to_profile_id: recipient profile id.
        :param str subject: thread subject.
        :param str message_html: the first thread's message.
        :return: created thread.
        """
        thread = {
            "subject": subject,
            "message_html": message_html,
            "to_profile_id": to_profile_id
        }
        responce = self._post("/threads", thread)
        return Thread.de_json(**responce)

    def create_support_request(self, subject: str, message_html: str) -> Thread:
        """Create new support request.

        :param str subject: thread subject.
        :param str message_html: the first thread's message.
        :return: created support request thread.
        """
        thread = {
            "subject": subject,
            "message_html": message_html,
        }
        responce = self._post("/threads/action/support", thread)
        return Thread.de_json(**responce)
