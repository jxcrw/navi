#!/usr/bin/env python3
"""Unit tests for Card class"""

import pytest
from api import Card


@pytest.mark.xfail()
def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    assert c1 == c2


@pytest.mark.xfail()
def test_explicit_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    if c1 != c2:
        pytest.fail("they don't match")


if __name__ == "__main__":
    test_equality_fail()
