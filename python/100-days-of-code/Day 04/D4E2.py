#!/usr/bin/env python3
"""Randomization + lists - bill Russian roulette"""

import random

names_input = input("Give me everybody's names, separated by a comma. ")
names_list = names_input.split(", ")

random_index = random.randint(0, len(names_list) - 1)
unlucky_person = names_list[random_index]

unlucky_person_pythonic = random.choice(names_list)

print(f"{unlucky_person} is going to buy the meal today!")
print(f"{unlucky_person_pythonic} is going to buy the meal today!")
