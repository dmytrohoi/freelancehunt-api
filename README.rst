FreelanceHunt API framework
-------------------------------

.. image:: https://github.com/dmytrohoi/freelancehunt-api/workflows/lint-test-coverage/badge.svg
  :target: https://github.com/dmytrohoi/freelancehunt-api/actions?workflow=lint-test-coverage

.. image:: https://codecov.io/gh/dmytrohoi/freelancehunt-api/branch/master/graph/badge.svg?token=TZWKUPK6D0
  :target: https://codecov.io/gh/dmytrohoi/freelancehunt-api

.. image:: https://img.shields.io/github/v/tag/dmytrohoi/freelancehunt-api?style=flat
  :target: https://github.com/dmytrohoi/freelancehunt-api/tags

.. image:: https://img.shields.io/pypi/pyversions/freelancehunt-api
  :alt: PyPI - Python Version
  :target: https://pypi.org/project/freelancehunt-api/

.. image:: https://img.shields.io/pypi/v/freelancehunt-api
  :alt: PyPI
  :target: https://pypi.org/project/freelancehunt-api/

.. image:: https://img.shields.io/github/v/release/dmytrohoi/freelancehunt-api
  :alt: GitHub release (latest by date)
  :target: https://github.com/dmytrohoi/freelancehunt-api/releases

.. image:: https://img.shields.io/github/license/dmytrohoi/freelancehunt-api
  :target: https://github.com/dmytrohoi/freelancehunt-api/tree/master/LICENSE

.. image:: https://readthedocs.org/projects/freelancehunt-api-python/badge/?version=latest
  :target: https://freelancehunt-api-python.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

============
Overview
============

> **!! DANGER !!: NOT FOR PRODUCTION USE!**

A framework for working with the `FreelanceHunt API <https://apidocs.freelancehunt.com/>`_.

**Requirements**:
  - Python 3.8
  - Requests

**In progress:**

- [ ] Threads API
- [ ] Thread representation
- [ ] Tests

=============
Installation
=============

To install use:

::

  pip install freelancehunt-api

===============
Documentation
===============

Quick usage:

.. code:: python

    from freelancehunt import FreelanceHuntClient

    fl = FreelanceHuntClient('YOUR_API_TOKEN')
    my_profile = fl.profiles.my_profile
    print(my_profile.full_name)
    #...

The freelancehunt-api documentation `available here <https://freelancehunt-api-python.readthedocs.io/>`_.

===================
The Current Version
===================

Now active version is: `0.1.0`

===============
Licence
===============

The freelancehunt-api is `MIT licenced <https://github.com/dmytrohoi/freelancehunt-api/tree/master/LICENSE>`_
