#!/usr/bin/env python3

def factorial(n):
    """Calculate n! (factorial)."""
    assert n >= 0 and isinstance(n, int), 'n must be a non-negative integer!'
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(4)
print(f'result: {result}')
