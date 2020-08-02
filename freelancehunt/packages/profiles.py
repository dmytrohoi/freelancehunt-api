#!usr/bin/python3
"""`Freelancehunt Documentation - Profiles API <https://apidocs.freelancehunt.com/?version=latest#7dfb1bc1-4d54-46d8-9c01-75b7a32f3db6>`_."""
from typing import List, Optional, Tuple, Union
from ..core import FreelancehuntObject
from ..models.user import Profile, Freelancer, Employer


__all__ = ('Profiles',)


class Profiles(FreelancehuntObject):
    """Provide operations with Profiles API part.

    .. warning:: For directly usage please set `token` argument.

    :param str token: your API token, optional
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        """Create object to provide operations with Profiles API part.

        :param token: your API token (only for directly usage, not inside Client class), defaults to None
        """
        super().__init__(token, **kwargs)

    @property
    def my_profile(self) -> Union[Employer, Freelancer]:
        """Get my profile information.

        :return: information of your account
        """
        responce = self._get('/my/profile')
        return Profile.de_json(**responce)

    def get_freelancers_list(
        self,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        skill_id: Optional[int] = None,
        login: Optional[str] = None,
        pages: Optional[Union[int, Tuple[int], List[int]]] = 1
    ) -> List[Freelancer]:
        """Get filtered freelancer profiles.

        :param country_id: freelancer from country (API-related Country identifier), defaults to None
        :param city_id: freelancer from city (API-related City identifier), defaults to None
        :param skill_id: freelancer skill (API-related Skill identifier), defaults to None
        :param login: with the desired login, defaults to None
        :param pages: number of pages, defaults to 1
        :return: list of filtered freelancer profiles
        """
        filters = {
            'country_id': country_id,
            'city_id': city_id,
            'skill_id': skill_id,
            'login': login
        }
        responce = self._multi_page_get('/freelancers', filters, pages)
        return [Freelancer.de_json(**data) for data in responce]

    def get_employers_list(
        self,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        login: Optional[str] = None,
        pages: Optional[Union[int, Tuple[int], List[int]]] = 1
    ) -> List[Employer]:
        """Get filtered employer profiles.

        :param country_id: employer from country (API-related Country identifier), defaults to None
        :param city_id: employer from city (API-related City identifier), defaults to None
        :param login: with the desired login, defaults to None
        :param pages: number of pages, defaults to 1
        :return: list of filtered employer profiles
        """
        filters = {
            'country_id': country_id,
            'city_id': city_id,
            'login': login
        }
        responce = self._multi_page_get('/employers', filters, pages)
        return [Employer.de_json(**data) for data in responce]

    def get_freelancer_datails(self, profile_id: int) -> Freelancer:
        """Get information about freelancer by identifier.

        :param profile_id: the desired profile identifier
        """
        responce = self._get(f'/freelancers/{profile_id}')
        return Freelancer.de_json(**responce)

    def get_employer_datails(self, profile_id: int) -> Employer:
        """Get information about employer by identifier.

        :param profile_id: the desired profile identifier
        """
        responce = self._get(f'/employers/{profile_id}')
        return Employer.de_json(**responce)
