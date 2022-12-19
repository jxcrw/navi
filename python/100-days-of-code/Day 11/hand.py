#!/usr/bin/env python3
"""Class for Blackjack game"""

from card import Card


class Hand():
    """A Blackjack hand of at least two cards."""
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def __str__(self):
        cards_pretty = " ".join([str(card) for card in self.cards])
        values_raw = list(self.determine_values())
        values_raw.sort()
        if len(values_raw) == 2:
            values_pretty = f"   ({' or '.join([str(value) for value in values_raw])})"
        else:
            values_pretty = f"   ({values_raw.pop()})"
        return cards_pretty + values_pretty

    def add_card(self, card: Card):
        """Add a card to the hand."""
        self.cards.append(card)

    def determine_values(self) -> set[int]:
        """Determine the Blackjack value of the hand. Returns set of possible hand values."""
        value_aces_lo = self._determine_value(1)
        value_aces_hi = self._determine_value(11)
        return {value_aces_lo, value_aces_hi}

    def is_bust(self):
        """Determines whether the hand is a bust."""
        min_value = min(self.determine_values())
        return min_value > 21

    def max_value(self):
        """Get the maximum possible value of the hand."""
        value_max = max(self.determine_values())
        return value_max

    # ┌─────────────────────────────────────────────────────────────────────────────
    # │ Private Helper Functions
    # └─────────────────────────────────────────────────────────────────────────────
    def _determine_value(self, value_ace) -> int:
        """Determine the value of the hand with the specified ace value."""
        value = 0
        for card in self.cards:
            if not card.visible:
                pass
            elif card.is_number_card():
                value += int(card.rank)
            elif card.is_face_card():
                value += 10
            elif card.is_ace():
                value += value_ace
        return value
