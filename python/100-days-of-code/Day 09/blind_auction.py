#!/usr/bin/env python3
"""Blind auction program"""

import os

LOGO = '''
   ___________
   \         /
    )_______(
    |"""""""|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )"""""""(
   /_________\\
 .-------------.
/_______________\\
'''

print(f"{LOGO}\nWelcome to Blind Auction!\n")

bids_dict = {}

while(True):
    name = input("What is your name? ").strip()
    bid = int(input("What is your bid? $"))
    bids_dict[name] = bid

    should_continue = input("Are there any other bidders? 'y' or 'n' ")
    if should_continue == 'y':
        os.system('cls') # Clear console
    else:
        break

bid_winning = max(bids_dict.values())
winners = [k for k, v in bids_dict.items() if v == bid_winning]

print(f"\nThe winner is {winners} with a bid of ${bid_winning}.")
