#!/usr/bin/env python3
"""Simple variable manipulation"""

# Get user input
a = input("a: ")
b = input("b: ")

# Switch values of a and b (just because)
c = b
b = a
a = c

# Output new values
print("a: " + a)
print("b: " + b)
