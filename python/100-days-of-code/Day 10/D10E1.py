#!/usr/bin/env python3
"""Functions with outputs - days in specified month"""

MONTH_DAYS = {1: 31,
              2: 28,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31}

def is_leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if is_leap(year) and month == 2:
        days = 29 # 29 days in February in leap year
    else:
        days = MONTH_DAYS[month]
    return days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
