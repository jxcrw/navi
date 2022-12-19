#!/usr/bin/env python3

def decimal_to_binary(n):
    """Convert specified n from decimal to binary."""
    assert n >= 0 and isinstance(n, int), 'n must be a positive integer!'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(n // 2)

print(decimal_to_binary(13))
