#!/usr/bin/env python3
"""Conditionals - pizza bill calculator"""

print("Welcome to Python Pizza Deliveries!")

# Gather user input
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ") == "Y"
extra_cheese = input("Do you want extra cheese? Y or N ") == "Y"

# Determine cost for size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

# Determine cost for toppings
if add_pepperoni:
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese:
    bill += 1

# Output final bill
print(f"Your final bill is: ${bill}.")
