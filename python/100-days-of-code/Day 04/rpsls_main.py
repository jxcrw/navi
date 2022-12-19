#!/usr/bin/env python3
"""Rock paper scissors lizard Spock game"""

import random
from rpsls_resources import name_rock, name_paper, name_scissors, name_lizard, name_spock
from rpsls_signals import Rock, Paper, Scissors, Lizard, Spock

SIGNALS = {name_rock: Rock(),
           name_paper: Paper(),
           name_scissors: Scissors(),
           name_lizard: Lizard(),
           name_spock: Spock()}

if __name__ == '__main__':
    # Determine user signal
    user_signal_raw = input("Rock, Paper, Scissors, Lizard, Spock...").strip().title()
    user_signal = SIGNALS[user_signal_raw]
    print(user_signal.ascii_art)

    # Determine computer signal
    computer_signal = random.choice(list(SIGNALS.values()))
    print(f"Computer chose: {computer_signal.name}\n{computer_signal.ascii_art}")

    # Determine and output game result
    game_result = user_signal.determine_result(computer_signal)
    print(game_result)
