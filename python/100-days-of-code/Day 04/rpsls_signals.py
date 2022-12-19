#!/usr/bin/env python3
"""Definitions of the RPSLS game signals"""

from rpsls_resources import *

class Signal:
    """Base class for representing RPSLS game signals."""
    def __init__(self, name, ascii_art, vlt_dict):
        self.name = name
        self.ascii_art = ascii_art
        self.vlt_dict = vlt_dict # vlt = victory, loss, tie

    def determine_result(self, signal):
        """Determine the RPSLS game result against `signal`."""
        result = self.vlt_dict[signal.name]
        return result

# ─────────────────────────────────────────────────────────────────────────────

class Rock(Signal):
    def __init__(self):
        super().__init__(name_rock, ascii_rock, vlt_dict_rock)

class Paper(Signal):
    def __init__(self):
        super().__init__(name_paper, ascii_paper, vlt_dict_paper)

class Scissors(Signal):
    def __init__(self):
        super().__init__(name_scissors, ascii_scissors, vlt_dict_scissors)

class Lizard(Signal):
    def __init__(self):
        super().__init__(name_lizard, ascii_lizard, vlt_dict_lizard)

class Spock(Signal):
    def __init__(self):
        super().__init__(name_spock, ascii_spock, vlt_dict_spock)
