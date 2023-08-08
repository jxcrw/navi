#!/usr/bin/env python3
"""Unit tests for DB"""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from api import Card, CardsDB


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Fixtures
# └─────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def temp_db():
    """Create temp DB in temp dir."""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = CardsDB(db_path)
        yield db               # ↑↑↑ Setup   Teardown ↓↓↓
        db.close()


@pytest.fixture(scope="session")
def temp_db_builtin(tmp_path_factory): # ← Builtin fixture.
    """Create temp DB in temp dir."""
    db_path = tmp_path_factory.mktemp("cards_db")
    db = CardsDB(db_path)
    yield db
    db.close()


@pytest.fixture(scope="function")
def db(temp_db):                  # ← Fixture scaffolding.
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
def prepopulated_db(db, cards):    # ← Fixture that uses multiple other fixtures.
    """CardsDB object that's been populated with 'cards'"""
    for c in cards:
        db.add_card(c)
    return db


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Basic Tests
# └─────────────────────────────────────────────────────────────────────────────
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


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Parameterization
# └─────────────────────────────────────────────────────────────────────────────
def test_finish_naive(db):
    cards = [
        Card("write a book", state="done"),
        Card("second edition", state="in prog"),
        Card("create a course", state="todo"),
    ]
    for c in cards:
        index = db.add_card(c)
        db.finish(index)
        card = db.get_card(index)
        assert card.state == "done"


@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_finish(db, start_state):
    c = Card("write a book", state=start_state)
    index = db.add_card(c)
    db.finish(index)
    card = db.get_card(index)
    assert card.state == "done"


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("write a book", "done"),
        ("second edition", "in prog"),
        ("create a course", "todo"),
    ],
)
def test_finish_with_summaries(db, start_summary, start_state):
    initial_card = Card(summary=start_summary, state=start_state)
    index = db.add_card(initial_card)
    db.finish(index)
    card = db.get_card(index)
    assert card.state == "done"


@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param

def test_finish_fixture_parameterization(db, start_state):
    c = Card("write a book", state=start_state)
    index = db.add_card(c)
    db.finish(index)
    card = db.get_card(index)
    assert card.state == "done"
