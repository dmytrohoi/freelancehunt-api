#!usr/bin/python3
"""`Freelancehunt Documentation - Bids API <https://apidocs.freelancehunt.com/?version=latest#d327b03a-1ab8-4c5f-b060-63a8216c1d4e>`_."""
from __future__ import annotations
from typing import List, Optional

from ..core import FreelancehuntObject

from ..models.bid import Bid


__all__ = ('Bids',)


class Bids(FreelancehuntObject):
    """Provide operations with Bids API part.

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Bids API part.

        :param str token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)

    def get_project_bids(self,
                         project_id: int,
                         status: Optional[str] = None,
                         is_winner: bool = False) -> List[Bid]:
        """Get filtered projects bid.

        :param project_id: project where find bids
        :param status: get bids with the desired status or all (None), defaults to None
        :param is_winner: get winner bid or all (False), defaults to False
        :return: list of filtered bids
        """
        filters = {}

        if is_winner:
            filters.update({"is_winner": 1})
        elif status:
            filters.update({"status": status})

        raw_bids = self._get(f"/projects/{project_id}/bids", filters=filters)
        return [Bid.de_json(**bid) for bid in raw_bids]

    def get_my_bids(self,
                    project_id: Optional[int] = None,
                    status: Optional[str] = None) -> List[Bid]:
        """Get my filtered bids.

        :param project_id: get bid for the desired project or all (None), defaults to None
        :param status: get bids with the desired status, defaults to None
        :return: list of my filtered bids
        """
        filters = {}

        if project_id:
            filters.update({"project_id": project_id})
        elif status:
            filters.update({"status": status})

        raw_bids = self._get("/my/bids", filters=filters)
        return [Bid.de_json(**bid) for bid in raw_bids]

    @property
    def my_active_bids(self) -> List[Bid]:
        """Get my active bids.

        :return: list of my active bids
        """
        return self.get_my_bids(status="active")

    def revoke_bid(self, project_id: int, bid_id: int) -> bool:
        """Revoke your bid.

        .. note:: Only for Freelancer and your own bid.

        :param project_id: get bid for the desired project
        :param bid_id: bid identifier
        :return: status of operation
        """
        url = f"/projects/{project_id}/bids/{bid_id}/revoke"
        return bool(self._post(url))

    def restore_bid(self, project_id: int, bid_id: int) -> bool:
        """Restore your bid.

        :param project_id: get bid for the desired project
        :param bid_id: bid identifier
        :return: status of operation
        """
        url = f"/projects/{project_id}/bids/{bid_id}/restore"
        return bool(self._post(url))

    def reject(self, project_id: int, bid_id: int) -> bool:
        """Reject this bid.

        .. note:: Only for Employer and your own project.

        :param project_id: get bid for the desired project
        :param bid_id: bid identifier
        :return: status of operation
        """
        url = f"/projects/{project_id}/bids/{bid_id}/reject"
        return self._post(url)

    def choose(self, project_id: int, bid_id: int, comment: str) -> bool:
        """Choose this bid.

        .. note:: Only for Employer and your own project.

        :param project_id: get bid for the desired project
        :param bid_id: bid identifier
        :param comment: comment for winner to start dialog with freelancer
        :return: status of operation
        """
        url = f"/projects/{project_id}/bids/{bid_id}/choose"
        return bool(self._post(url, payload={"comment": comment}))
