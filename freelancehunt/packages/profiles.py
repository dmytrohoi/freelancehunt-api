#!usr/bin/python3
"""#TODO: Write comments."""
from ..core import FreelancehuntObject
from ..models.user import UserEntity, FreelancerEntity, EmployerEntity

__all__ = [
    'Profiles',
]


class Profiles(FreelancehuntObject):

    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)

    @property
    def my_profile(self):
        responce = self._get('/my/profile')
        return UserEntity.de_json(**responce)

    def get_freelancers_list(self, country_id=None, city_id=None,
                             skill_id=None, login=None, pages=1):
        filters = {
            'country_id': country_id,
            'city_id': city_id,
            'skill_id': skill_id,
            'login': login
        }
        responce = self._multi_page_get('/freelancers', filters, pages)
        return [FreelancerEntity.de_json(**data) for data in responce]

    def get_employers_list(self, country_id=None, city_id=None, login=None,
                           pages=1):
        filters = {
            'country_id': country_id,
            'city_id': city_id,
            'login': login
        }
        responce = self._multi_page_get('/employers', filters, pages)
        return [EmployerEntity.de_json(**data) for data in responce]

    def get_freelancer_datails(self, profile_id):
        responce = self._get(f'/freelancers/{profile_id}')
        return FreelancerEntity.de_json(**responce)

    def get_employer_datails(self, profile_id):
        responce = self._get(f'/employers/{profile_id}')
        return EmployerEntity.de_json(**responce)
