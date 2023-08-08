#!/usr/bin/env python3
"""Unit tests for DB"""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from api import Card, CardsDB


@pytest.fixture(scope="module")
def temp_db():
    """Create temp DB in temp dir."""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = CardsDB(db_path)
        yield db               # ↑↑↑ Setup   Teardown ↓↓↓
        db.close()


@pytest.fixture(scope="function")
def db(temp_db):
    """Ensure that DB is empty."""
    temp_db.delete_all()
    return temp_db


@pytest.fixture(scope="function")
def cards():
    """List of different Card objects"""
    return [
        Card("write book", "Brian", "done"),
        Card("edit book", "Katie", "done"),
        Card("write 2nd edition", "Brian", "todo"),
        Card("edit 2nd edition", "Katie", "todo"),
    ]


@pytest.fixture(scope="function")
def prepopulated_db(db, cards):
    """CardsDB object that's been populated with 'cards'"""
    for c in cards:
        db.add_card(c)
    return db


def test_empty(db):
    assert db.count() == 0


def test_add_two(db):
    db.add_card(Card("first"))
    db.add_card(Card("second"))
    assert db.count() == 2


def test_add_three(db):
    db.add_card(Card("first"))
    db.add_card(Card("second"))
    db.add_card(Card("third"))
    assert db.count() == 3


def test_add_some(db, cards):
    count_expected = len(cards)
    for c in cards:
        db.add_card(c)
    assert db.count() == count_expected


def test_prepopulated(prepopulated_db):
    assert prepopulated_db.count() > 0
