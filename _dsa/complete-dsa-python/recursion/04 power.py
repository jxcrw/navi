#!/usr/bin/env python3

def power(x, n):
    """Calculate x ** n."""
    assert isinstance(n, int), 'The exponent n must be an integer!'
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    else:
        return x * power(x, n - 1)

print(power(3, 0))
print(power(3, 2))
print(power(1.5, 3))
print(power(2, -5))
print(power(2, 1.2))
