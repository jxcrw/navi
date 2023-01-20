#!/usr/bin/env python3

def sum_of_digits(n):
    """Calculate the sum of the digits of n."""
    assert n >= 0 and isinstance(n, int), 'n must be a non-negative integer!'
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(112))
print(sum_of_digits(3358))
print(sum_of_digits(8675309))
