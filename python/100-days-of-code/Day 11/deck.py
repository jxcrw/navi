#!/usr/bin/env python3
"""Class for Blackjack game"""

import random

from card import Card
from constants import *


class Deck():
    """A deck of 52 standard playing cards."""
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks_all]

    def shuffle(self):
        """Shuffle the cards in the deck."""
        random.shuffle(self.cards)

    def next(self) -> Card:
        """Deal the next card from the deck."""
        next_card = self.cards.pop(0)
        return next_card
