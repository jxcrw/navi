#!/usr/bin/env python3
"""For loops - calculating average of list without convenience functions"""

from statistics import mean

student_heights = [180, 124, 165, 173, 189, 169, 146]

i = 0
running_sum = 0
for height in student_heights:
    running_sum += height
    i += 1

average_height = running_sum / i
average_height_convenient = sum(student_heights) / len(student_heights)
average_height_convenienter = mean(student_heights)

print(round(average_height))
print(round(average_height_convenient))
print(round(average_height_convenienter))
