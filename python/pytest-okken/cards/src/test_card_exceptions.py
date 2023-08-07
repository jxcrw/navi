#!/usr/bin/env python3
"""Unit tests for Card class"""

import pytest
from api import CardsDB


def test_no_path_raises_exception():
    with pytest.raises(TypeError):
        CardsDB()


def test_raises_with_info():
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        CardsDB()


def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        CardsDB()
    expected = "missing 1 required positional argument"
    assert expected in str(exc_info.value)
