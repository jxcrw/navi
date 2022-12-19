#!/usr/bin/env python3

def power_of_2(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * power_of_2(n // 2)

# ⇒ O(log n)
