#!/usr/bin/env python3
"""Conditionals + string operations - silly love calculator"""

def count_freq_score(test_string, input_string):
    """Count the number of times each char in `test_string` occurs in `input_string`."""
    count = 0
    for c in test_string:
        count += input_string.count(c)
    return count

# ─────────────────────────────────────────────────────────────────────────────

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name_combined = name1.lower() + name2.lower()

count_true = count_freq_score("true", name_combined)
count_love = count_freq_score("love", name_combined)
love_score = int(str(count_true) + str(count_love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
