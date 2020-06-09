#!usr/bin/python3
"""Basic classes for API objects."""
from .utils import Requester


__all__ = [
    'FreelancehuntObject'
]


class FreelancehuntObject:
    """Parent class for all parts of API."""
    requester = None

    def __init__(self, token=None, **kwargs):
        self.requester = Requester.get_requester(token, **kwargs)

    def _get(self, url, filters=None, page=None):
        if page:
            filters.update({'page[number]': page})
        result = self.requester.request("GET", url=url, filters=filters)
        return self.__parse_data(result["data"])

    def _multi_page_get(self, url, filters=None, pages=None):
        if pages is None or isinstance(pages, int):
            min_page_num = 1
            max_page_num = pages or 1
        elif isinstance(pages, (list, tuple)) and len(pages) == 2:
            min_page_num = pages[0]
            max_page_num = pages[1]

        result = []
        for page in range(min_page_num, max_page_num + 1):
            result += self._get(url, filters, page)
        return result

    def _post(self, url, payload=None):
        result = self.requester.request("POST", url=url, payload=payload)
        data = result.get("data")
        if data:
            return self.__parse_data(data)

    def __parse_data(self, data: dict):
        if isinstance(data, list):
            return [self.__parse_data(info) for info in data]

        basic_data = {
            "id": data.pop("id"),
            "type": data.pop("type", None),
            "links": data.pop("links", None)
        }
        attributes = data.get("attributes")
        if attributes:
            basic_data.update(**attributes)
        else:
            basic_data.update(**data)
        return basic_data

    def _filter_list_by_attr(self, objects, attribute):
        return list(filter(lambda obj: getattr(obj, attribute), objects))
