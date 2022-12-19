#!/usr/bin/env python3
"""Number guessing game"""

import random

LOGO = """
   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|                                                                                                                                                                           
"""

TURNS_EASY = 10
TURNS_HARD = 5
THE_NUMBER_MAX = 100

MSG_WIN = "\nThat was it! You win!"
MSG_LOSE = "You're out of guesses. You lose!"
MSG_HIGH = "Too high!"
MSG_LOW = "Too low!"

def evaluate_guess(guess, true_number):
    if guess == true_number:
        evaluation = MSG_WIN
    elif guess > true_number:
        evaluation = MSG_HIGH
    elif guess < true_number:
        evaluation = MSG_LOW
    return evaluation

# ─────────────────────────────────────────────────────────────────────────────

print(LOGO)
print("Welcome to Guess the Number!\n")

difficulty = input("Choose a difficulty ('easy' or 'hard'): ")
attempts_remaining = (TURNS_EASY if difficulty == 'easy' else TURNS_HARD)

print("I'm thinking of a number between 0 and 100. You have to guess it!")
the_number = random.choice(range(THE_NUMBER_MAX + 1))

end_game_flag = False
while not end_game_flag:
    print(f"\nYou have {attempts_remaining} attempts remaining to guess the number.")
    user_guess = float(input("Make a guess: "))

    evaluation = evaluate_guess(user_guess, the_number)
    print(f"{evaluation}")
    if evaluation == MSG_WIN:
        end_game_flag = True
    else:
        attempts_remaining -= 1

    if attempts_remaining == 0:
        print(f"\n{MSG_LOSE}")
        end_game_flag = True
