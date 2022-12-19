#!/usr/bin/env python3
"""Mathematical operations and f-strings"""

HUMAN_LIFESPAN_YEARS = 90

age_years = int(input("What is your current age? "))

remaining_years = HUMAN_LIFESPAN_YEARS - age_years
remaining_days = remaining_years * 365
remaining_weeks = remaining_years * 52
remaining_months = remaining_years * 12

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
