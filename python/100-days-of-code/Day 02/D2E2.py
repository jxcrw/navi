#!/usr/bin/env python3
"""Mathematical operations - BMI calculator"""

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2
print(int(bmi))