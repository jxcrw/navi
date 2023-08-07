#!/usr/bin/env python3
"""Scratch code from Python Testing with Pytest"""

def testpass():
    assert (1, 2, 3) == (1, 2, 3)

def test_fail():
    assert (1, 2, 3) == (3, 2, 1)
