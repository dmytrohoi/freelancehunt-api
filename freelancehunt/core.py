#!usr/bin/python3
"""Basic classes for API objects."""
from __future__ import annotations
from typing import ByteString, Dict, List, Optional, Tuple, Union

from .utils.requester import Requester


__all__ = ('FreelancehuntObject',)


class FreelancehuntObject:
    """Core class for all parts of API."""

    _requester: Requester = None

    def __init__(self, token: str = None, **kwargs):
        """Create new FreelancehuntObject and add new Requester.

        :param str token: user personal access token
        :param dict kwargs: can be:
            language - language of responced data, default to 'en'
        """
        self._requester = Requester(token, **kwargs)

    def _get(
        self,
        url: str,
        filters: Optional[dict] = None,
        page: Optional[int] = None
    ) -> dict:
        """Make GET request to the desired url.

        :param str url: the desired url
        :param Optional[dict] filters: send additional filters GET query, defaults to None
        :param Optional[int] page: select the desired page (regarding pagination), defaults to None
        :raises ValueError: Invalid page value (regarding pagination)
        :return: parsed JSON response.
        :rtype: dict
        """
        if page is not None and not isinstance(page, int):
            raise ValueError("Invalid page value {page}".format(page=page))
        elif page:
            if filters is None:
                filters = {}
            filters.update({'page[number]': page})

        result = self._requester.request("GET", url=url, filters=filters)
        return self.__parse_data(result["data"], result.get("meta"))

    def _multi_page_get(
        self,
        url: str,
        filters: Optional[dict] = None,
        pages: Optional[Union[int, Tuple[int], List[int]]] = None
    ) -> List[dict]:
        """Make multiple GET requests to the desired url to use pagination.

        :param str url: the desired url
        :param Optional[dict] filters: send additional filters GET query, defaults to None
        :param page: select the desired page (regarding pagination), defaults to None
        :type pages: Optional[Union[int, Tuple[int], List[int]]], optional
        :raises ValueError: Invalid page value (regarding pagination)
        :return: parsed JSON response.
        :rtype: List[dict]
        """
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
        """Make POST request to the desired url.

        :param str url: the desired url
        :param Optional[dict] filters: send additional filters GET query, defaults to None
        :param Optional[dict] payload: information to send, defaults to None
        :return: parsed JSON response, or `True` if no data in response.
        :rtype: Union[dict, bool]
        """
        result = self._requester.request(
            "POST",
            url=url,
            payload=payload
        )
        data = result.get("data")
        if not data:
            return True
        return self.__parse_data(data, result.get("meta"))

    def _delete(self, url: str) -> bool:
        """Make DELETE request to the desired url.

        :param str url: the desired url
        :return: `True` if request success.
        :rtype: bool
        """
        self._requester.request("DELETE", url=url)
        return True

    def _post_attachment(
        self,
        url: str,
        files: Dict[str, ByteString],
        payload: Optional[dict] = None
    ) -> Union[dict, bool]:
        """Make POST request with files to the desired url.

        :param str url: the desired url
        :param files: files to send
        :type files: Dict[str, ByteString]
        :param payload: some additional post information, defaults to None
        :type payload: Optional[dict], optional
        :raises ValueError: Post attachment response data not found and error occurs!
        :return: parsed JSON response, or `True` if data not available.
        :rtype: Union[dict, bool]
        """
        result = self._requester.request(
            "POST",
            url=url,
            payload=payload,
            files=files,
            # headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        data = result.get("data")
        if not data:
            return True
        return self.__parse_data(data, result.get("meta"))

    def _patch(self, url: str, payload: Optional[dict] = None) -> dict:
        """Make PATCH request to the desired url.

        :param str url: the desired url
        :param Optional[dict] filters: send additional filters GET query, defaults to None
        :param Optional[dict] payload: information to send, defaults to None
        :return: parsed JSON response, or `True` if no data in response.
        :rtype: Union[dict, bool]
        """
        result = self._requester.request(
            "PATCH",
            url=url,
            payload=payload
        )
        data = result.get("data")
        if not data:
            return True
        return self.__parse_data(data, result.get("meta"))

    def __parse_data(
        self,
        data: Optional[Union[dict, list]],
        meta: Optional[dict]
    ) -> Optional[Union[dict, list]]:
        """Parse API response to get essential information.

        :param  Optional[Union[dict, list]] data: raw information from API
        :param Optional[dict] meta: meta information from API
        :return: filtered and normalized information for framework
        :rtype: Optional[Union[dict, list]]
        """
        if isinstance(data, list):
            return [self.__parse_data(info, meta) for info in data]

        basic_data = {
            "id": data.pop("id"),
            "type": data.pop("type", None),
            "links": data.pop("links", None)
        }

        # Available in Thread.get_message() for ThreadMessages objects
        # to preserve parent's Thread object
        if meta:
            basic_data.update({"meta": meta})

        attributes: dict = data.get("attributes", {})
        if attributes:
            basic_data.update(**attributes)
        else:
            basic_data.update(**data)
        return basic_data
