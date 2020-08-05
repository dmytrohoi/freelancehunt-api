#!usr/bin/python3
"""ThreadMessage object representation.

Documentation example:

.. code-block:: javascript

    {
      "id": 67,
      "type": "message",
      "attributes": {
        "message": "I choose you!",
        "message_html": "I choose you!",
        "posted_at": "2019-04-03T09:33:05+03:00",
        "attachments": [],
        "participants": {
          "from": {
            "id": 38444,
            "type": "employer",
            "login": "jeweller",
            "first_name": "Oleg",
            "last_name": "V.",
            "avatar": {
              "small": {
                "url": "https://content.freelancehunt.com/profile/photo/50/jeweller.png",
                "width": 50,
                "height": 50
              },
              "large": {
                "url": "https://content.freelancehunt.com/profile/photo/225/jeweller.png",
                "width": 255,
                "height": 255
              }
            },
            "self": "https://api.freelancehunt.com/v2/employers/38444"
          },
          "to": {
            "id": 5725,
            "type": "freelancer",
            "login": "alex_yar",
            "first_name": "Andrey",
            "last_name": "Y.",
            "avatar": {
              "small": {
                "url": "https://content.freelancehunt.com/profile/photo/50/alex_yar.png",
                "width": 50,
                "height": 50
              },
              "large": {
                "url": "https://content.freelancehunt.com/profile/photo/225/alex_yar.png",
                "width": 255,
                "height": 255
              }
            },
            "self": "https://api.freelancehunt.com/v2/freelancers/5725"
          }
        }
      }
    }
"""
from datetime import datetime
from typing import Type, Optional

from ..core import FreelancehuntObject
from ..utils.errors import BadRequestError

from .user import Profile


__all__ = ('ThreadMessage',)


class ThreadMessage(FreelancehuntObject):
    """Provide operations with ThreadMessage.

    :param int id: thread unique identifier
    :param str message: message text
    :param str message_html: message text in html
    :param datetime posted_at: the message post date
    :param dict attachments: message's attachments
    :param Profile sender: message creator information
    :param Profile recipient: message recipient information
    """

    def __init__(self,
                 id: int,
                 posted_at: str,
                 message: str,
                 message_html: str,
                 sender: Profile,
                 recipient: Profile,
                 attachments: Optional[list] = None,
                 thread: Optional[dict] = None,
                 **kwargs):
        """Create object to provide operations with ThreadMessage.

        :param int id: thread unique identifier
        :param str message: message text
        :param str message_html: message text in html
        :param str posted_at: string representation of the message post date
        :param dict attachments: message's attachments
        :param Profile sender: message creator information
        :param Profile recipient: message recipient information
        """
        super().__init__(**kwargs)
        self.id = id
        self.posted_at = datetime.fromisoformat(posted_at)
        self.message = message
        self.message_html = message_html
        self.attachments = attachments  # TODO: Implement attachments parsing
        # Framework objects
        self.sender = sender
        self.recipient = recipient
        # Will be parsed to objects
        self._thread = thread
        # Custom attributes
        self._create_msg_url = f"/threads/{self._thread.get('id')}" if self._thread else None

    def answer(self, message_html: str) -> Type["ThreadMessage"]:
        """Answer to this message in current thread.

        :param str message_html: message text to send
        :raises ValueError: Thread not linked to this message!
        :raises BadRequestError: Message not sended!
        :return: new message object
        """
        if not self._create_msg_url:
            raise ValueError('Thread not linked to this message!')

        message = self._post(self._create_msg_url, {"message_html": message_html})
        if not message:
            raise BadRequestError(
                f"Message not send to '{self._create_msg_url}' with text '{message_html}'!"
            )

        message.update({"thread": self._thread})
        return ThreadMessage.de_json(**message)

    @classmethod
    def de_json(cls, **data) -> Type["ThreadMessage"]:
        """Parse json data from API responce and make object of this class.

        :return: object of this class.
        :rtype: `ThreadMessage`
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

        meta = data.get("meta")
        if meta:
            data["thread"] = meta["thread"]
        return cls(**data)

