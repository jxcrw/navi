#!/usr/bin/env python3
"""For loops - add even numbers from 1 to 100"""

total = 0
for i in range(101):
    if i % 2 == 0:
        total += i
print(total)

numbers = [_ for _ in range(101) if _ % 2 == 0]
total = sum(numbers)
print(total)


total = 0
for i in range(2, 101, 2):
    total += i
print(total)

numbers = [_ for _ in range(2, 101, 2)]
total = sum(numbers)
print(total)
