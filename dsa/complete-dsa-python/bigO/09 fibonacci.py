#!/usr/bin/env python3

def all_fibonacci(n):
    for i in range(n): # O(n)
        print(f"{i}: {fibonacci(i)}") # O(2^n)

def fibonacci(n):
    assert n >= 0 and isinstance(n, int), 'n must be a non-negative integer!'
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # O(2^n)

# ⇒ O(2^n)
