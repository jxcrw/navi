#!/usr/bin/env python3

def fibonacci(n):
    """Calculate the nth fibonacci number."""
    assert n >= 0 and isinstance(n, int), 'n must be a non-negative integer!'
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)
print(f'result: {result}')
