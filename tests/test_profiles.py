#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt import Profiles


class Profiles:

    def __init__(self, token=None, **kwargs):
        pass

    #property
    def my_profile(self):
        pass

    def get_freelancers_list(self, country_id=None, city_id=None,
                             skill_id=None, login=None, pages=1):
        pass

    def get_employers_list(self, country_id=None, city_id=None, login=None,
                           pages=1):
        pass

    def get_freelancer_datails(self, profile_id):
        pass

    def get_employer_datails(self, profile_id):
        pass
