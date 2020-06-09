#!usr/bin/python3
"""Common fixtures to use in tests."""
import logging
import pytest


logger = logging.getLogger(__name__)


# Indirect passing
@pytest.fixture
def expected(request):
    return request.param
