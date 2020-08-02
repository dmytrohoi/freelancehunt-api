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
from ..core import FreelancehuntObject


__all__ = ('Thread',)


class Thread(FreelancehuntObject):
    """Provide operations with Thread.

    .. note:: NOT IMPLEMENTED YET!
    """

    def __init__(self, **kwargs):
        # TODO: Comment
        super().__init__(**kwargs)

    # TODO: Not implemented yet