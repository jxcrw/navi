#!/usr/bin/env python3
"""Class for Blackjack game"""

from hand import Hand


class Dealer():
    """Encapsulates the play logic of a Blackjack dealer."""
    def __init__(self, hand: Hand):
        self.hand = hand

    def wants_hit(self):
        """Returns True if dealer wants another card, False otherwise."""
        hand_values = self.hand.determine_values()
        if (17 <= max(hand_values) <= 21) or (17 <= min(hand_values) <= 21):
            return False
        else:
            return True
