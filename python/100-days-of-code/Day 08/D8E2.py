#!/usr/bin/env python3
"""Functions - prime number checker"""

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Check this number: "))
print("It's a prime number." if is_prime(number) else "It's not a prime number.")
