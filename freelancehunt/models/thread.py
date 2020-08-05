#!usr/bin/python3
"""Thread object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 2237325,
      "type": "thread",
      "attributes": {
        "subject": "Workspace for project High-budget project",
        "first_post_at": "2019-02-21T14:12:35+02:00",
        "last_post_at": "2019-02-21T14:12:35+02:00",
        "messages_count": 1,
        "is_unread": false,
        "has_attachments": false,
        "participants": {
          "from": {
            "id": 340096,
            "type": "employer",
            "login": "ledpodarok",
            "first_name": "Anatoliy",
            "last_name": "S.",
            "avatar": {
              "small": {
                "url": "https://content.freelancehunt.com/profile/photo/50/ledpodarok.png",
                "width": 50,
                "height": 50
              },
              "large": {
                "url": "https://content.freelancehunt.com/profile/photo/225/ledpodarok.png",
                "width": 255,
                "height": 255
              }
            },
            "self": "http://api.freelancehunt.com/v2/employers/340096"
          },
          "to": {
            "id": 3166,
            "type": "freelancer",
            "login": "raznomir",
            "first_name": "Mikhail",
            "last_name": "Tereshchenko",
            "avatar": {
              "small": {
                "url": "https://content.freelancehunt.com/profile/photo/50/raznomir.png",
                "width": 50,
                "height": 50
              },
              "large": {
                "url": "https://content.freelancehunt.com/profile/photo/225/raznomir.png",
                "width": 255,
                "height": 255
              }
            },
            "self": "http://api.freelancehunt.com/v2/freelancers/3166"
          }
        }
      },
      "links": {
        "self": {
          "api": "http://api.freelancehunt.com/v2/threads/2237325",
          "web": "http://freelancehunt.com/mailbox/read/thread/2237325"
        }
      }
    }
"""
from datetime import datetime
from typing import List, Tuple, Type, Union

from ..core import FreelancehuntObject
from ..utils.errors import BadRequestError

from .user import Profile
from .threadmessage import ThreadMessage


__all__ = ('Thread',)


class Thread(FreelancehuntObject):
    """Provide operations with Thread.

    :param int id: thread unique identifier
    :param str subject: thread subject text
    :param datetime first_post_at: the first message date
    :param datetime last_post_at: the last message date
    :param int messages_count: count of messages in thread
    :param bool is_unread: sign that the thread is unread
    :param bool has_attachments: sign that the thread has attachments
    :param Profile sender: thread creator information
    :param Profile recipient: thread recipient information
    """

    def __init__(self,
                 id: int,
                 subject: str,
                 first_post_at: str,
                 last_post_at: str,
                 messages_count: int,
                 is_unread: bool,
                 has_attachments: bool,
                 sender: Profile,
                 recipient: Profile,
                 **kwargs):
        """Create object to provide operations with Thread.

        :param int id: thread unique identifier
        :param str subject: thread subject text
        :param str first_post_at: string representation of the first message date
        :param str last_post_at: string representation of the last message date
        :param int messages_count: count of messages in thread
        :param bool is_unread: sign that the thread is unread
        :param bool has_attachments: sign that the thread has attachments
        :param Profile sender: thread creator information
        :param Profile recipient: thread recipient information
        """
        super().__init__(**kwargs)
        self.id = id
        self.subject = subject
        self.first_post_at = datetime.fromisoformat(first_post_at)
        self.last_post_at = datetime.fromisoformat(last_post_at)
        self.messages_count = messages_count
        self.is_unread = is_unread
        self.has_attachments = has_attachments
        # Framework objects
        self.sender = sender
        self.recipient = recipient
        # Custom attributes
        self.api_url = f"/threads/{self.id}"

    def get_messages(self, pages: Union[int, Tuple[int], List[int]] = 1) -> List[ThreadMessage]:
        responce = self._multi_page_get(self.api_url, pages=pages)
        return [ThreadMessage.de_json(**data) for data in responce]

    def answer(self, message_html: str):
        message = self._post(self.api_url, payload={"message_html": message_html})
        if not message:
            raise BadRequestError(
                f"Message not send to '{self.api_url}' with text '{message_html}'!"
            )

        message.update({"thread": {"id": self.id}})
        return ThreadMessage.de_json(**message)

    @classmethod
    def de_json(cls, **data) -> Type["Thread"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `Thread`
        """
        if not data:
            return None

        participants = data["participants"]

        sender = participants.get("from")
        if sender:
            data["sender"] = Profile.de_json(**sender)

        recipient = participants.get("to")
        if recipient:
            data["recipient"] = Profile.de_json(**recipient)

        return cls(**data)

