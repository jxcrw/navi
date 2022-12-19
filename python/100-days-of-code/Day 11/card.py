#!/usr/bin/env python3
"""Class for Blackjack game"""

from constants import *


class Card():
    """A standard playing card."""
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.visible = True

    def __str__(self):
        if self.visible:
            return self.rank + self.suit
        else:
            return "[]"

    def is_number_card(self):
        """Determine whether the card is a number card."""
        return self.rank in ranks_numbers

    def is_face_card(self):
        """Determine whether the card is a face card."""
        return self.rank in ranks_faces

    def is_ace(self):
        """Determine whether the card is an ace."""
        return self.rank in ranks_aces
