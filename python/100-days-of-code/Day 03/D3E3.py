#!/usr/bin/env python3
"""Conditional statements - leap year determination"""

import calendar

MESSAGE_LEAP_YEAR = "Leap year."
MESSAGE_NOT_LEAP_YEAR = "Not leap year."

year = int(input("Which year do you want to check? "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    message = MESSAGE_LEAP_YEAR
else:
    message = MESSAGE_NOT_LEAP_YEAR

print(message)
print(calendar.isleap(year))
