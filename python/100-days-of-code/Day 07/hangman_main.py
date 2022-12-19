#!/usr/bin/env python3
"""Hangman game"""

import random

from hangman_words import WORD_LIST
from hangman_art import logo, lives_art_dict

# Initialize game
print(logo)
mystery_word = random.choice(WORD_LIST)
game_board = ["_" for c in mystery_word]
end_of_game = False
user_lives = 6
previous_guesses = set()
print(' '.join(game_board) + '\n')

while not end_of_game:
    # Get guess from user
    user_guess_letter = input("Guess a letter: ").strip().lower()

    if user_guess_letter in previous_guesses:
        print("You guessed that before. No sweat - guess again!\n")
        continue

    # Check if guessed letter in mystery word, and update game board accordingly
    for i, c in enumerate(mystery_word):
        if user_guess_letter == c:
            game_board[i] = user_guess_letter

    # Update user lives
    if user_guess_letter not in mystery_word:
        user_lives -= 1
        print(f"The letter {user_guess_letter} is not in the word. You lose a life.")
        print(lives_art_dict[user_lives])

    # Display current game state
    print(' '.join(game_board) + '\n')

    # Update previous guesses and check end-of-game conditions
    previous_guesses.add(user_guess_letter)

    if user_lives == 0:
        end_of_game = True
        print(f"Too bad, the word was '{mystery_word}'. You lose!")

    if "_" not in game_board:
        end_of_game = True
        print(f"That's right, the word was '{mystery_word}'. You win!")
