#!/usr/bin/env python3
"""Find missing number in integer array of 1 to 100."""

import timeit

# Setup
input_array = list(range(1, 101))
input_array.remove(51)

# Solution 1 - Naive Loop
# Complexity: O(n)
def solution1():
    missing_values = []
    for i in range(1, 101):
        if i not in input_array:
            missing_values.append(i)
    return missing_values

print(solution1())

# Solution 2 - Sets
# Complexity: Unknown
def solution2():
    input_set = set(input_array)
    ref_set = set(list(range(1, 101)))
    diff = ref_set.difference(input_set)
    return diff

print(solution2())

# Solution 3 - Sum of Series
# Complexity: O(1)
# Weakness: Only works if exactly one number missing
def solution3():
    sum_complete = 100 * (100 + 1) / 2
    sum_missing = sum(input_array)
    missing = sum_complete - sum_missing
    return missing

print(solution3())

# Benchmarking
print(timeit.timeit(solution1, number=10000))
print(timeit.timeit(solution2, number=10000)) # ≈10x faster than solution1
print(timeit.timeit(solution3, number=10000)) # ≈5.6x faster than solution2
