#!/usr/bin/env python3
"""Conditional statements - BMI calculator 2.0"""

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2
if bmi <= 18.5:
    interpretation = "underweight"
elif bmi <= 25:
    interpretation = "normal weight"
elif bmi <= 30:
    interpretation = "slightly overweight"
elif bmi <= 35:
    interpretation = "obese"
else:
    interpretation = "clinically obese"

print(f"Your BMI is {round(bmi)}, you are {interpretation}.")
