#!usr/bin/python3
"""Basic classes for API objects."""
from __future__ import annotations
from typing import List, Optional, Tuple, Union

from requests.models import Response

from .utils.requester import Requester


__all__ = ('FreelancehuntObject',)


class FreelancehuntObject:
    """Core class for all parts of API."""

    _requester = None

    def __init__(self, token: str = None, **kwargs):
        self._requester = Requester.get_requester(token, **kwargs)

    def _get(
        self,
        url: str,
        filters: Optional[dict] = None,
        page: Optional[int] = None
    ) -> dict:
        if page is not None and not isinstance(page, int):
            raise ValueError("Invalid page value {page}".format(page=page))
        elif page:
            filters.update({'page[number]': page})

        result = self._requester.request("GET", url=url, filters=filters)
        return self.__parse_data(result["data"])

    def _multi_page_get(
        self,
        url: str,
        filters: Optional[dict] = None,
        pages: Optional[Union[int, Tuple[int], List[int]]] = None
    ) -> List[dict]:
        if pages is None or isinstance(pages, int):
            min_page_num = 1
            max_page_num = pages or 1
        elif isinstance(pages, (list, tuple)) and len(pages) == 2:
            min_page_num, max_page_num = pages
        else:
            raise ValueError("Invalid pages value {pages}".format(pages=pages))

        result = []
        for page in range(min_page_num, max_page_num + 1):
            result += self._get(url, filters, page)
        return result

    def _post(self, url: str, payload: Optional[dict] = None) -> dict:
        result: Response = self._requester.request("POST", url=url, payload=payload)
        data = result.get("data")
        if not data and result.status_code != 200:
            raise ValueError('Post responce data not found!')
        elif not data:
            return True
        return self.__parse_data(data)

    def __parse_data(self, data: Optional[Union[dict, list]]) -> Optional[Union[dict, list]]:
        if isinstance(data, list):
            return [self.__parse_data(info) for info in data]

        basic_data = {
            "id": data.pop("id"),
            "type": data.pop("type", None),
            "links": data.pop("links", None)
        }
        attributes: dict = data.get("attributes", {})
        if attributes:
            basic_data.update(**attributes)
        else:
            basic_data.update(**data)
        return basic_data

    @staticmethod
    def _filter_list_by_attr(objects: List[FreelancehuntObject],
                             attribute: str) -> list:
        return list(filter(lambda obj: getattr(obj, attribute), objects))
