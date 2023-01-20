#!/usr/bin/env python3

def greatest_common_divisor(a, b):
    """Find the GCD of a and b using Euclidean algorithm."""
    assert (isinstance(a, int) and isinstance(b, int)), 'a and b must be integers!'
    a = a if a > 0 else -a
    b = b if b > 0 else -b
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(-12, -9))
