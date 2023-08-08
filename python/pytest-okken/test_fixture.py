#!/usr/bin/env python3
"""Simple fixture demo"""

import pytest


@pytest.fixture()
def my_data():
    """Prep data for testing."""
    return 42


def test_data(my_data):
	"""Use prepped data in test."""
	assert my_data == 42
