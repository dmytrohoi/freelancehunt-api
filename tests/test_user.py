#!usr/bin/python3
"""#TODO: Write comments."""
from freelancehunt.models.user import Profile
from freelancehunt.models.user import Employer
from freelancehunt.models.user import Freelancer


class UserEntity:
    def __init__(self, id, login, type, first_name, last_name, avatar=None,
                 birth_date=None, created_at=None, cv=None, cv_html=None,
                 rating=None, rating_position=None, arbitrages=None,
                 positive_reviews=None, negative_reviews=None,
                 plus_ends_at=None, is_plus_active=None, is_online=None,
                 visited_at=None, location=None, verification=None,
                 contacts=None, status=None, skills=None, links=None,
                 **kwargs):
        pass

    #property
    def full_name(self):
        pass

    #property
    def profile_url(self):
        pass

    #property
    def reviews(self):
        pass

    def load_details(self):
        pass

    def de_json(cls, **data):
        pass

class EmployerEntity():

    def __str__(self):
        pass

class FreelancerEntity:

    def __str__(self):
        pass
