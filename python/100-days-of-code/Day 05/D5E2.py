#!/usr/bin/env python3
"""For loops - max of list without built-ins"""

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

running_max = 0
for score in student_scores:
    if score > running_max:
        running_max = score

max_convenient = max(student_scores)

print(f"The highest score in the class is: {running_max}")
print(f"The highest score in the class is: {max_convenient}")
