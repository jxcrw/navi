#!/usr/bin/env python3
"""Split a bill between multiple people"""

print("Welcome to Bill Calculator!\n")

total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15?" ))
num_people = int(input("How many people will be splitting the bill? "))

total_with_tip = total_bill * (1 + tip_percent / 100)
amount_per_person = total_with_tip / num_people

print(f"Each person should pay: ${amount_per_person:.2f}")
