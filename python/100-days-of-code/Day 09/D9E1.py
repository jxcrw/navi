#!/usr/bin/env python3
"""Simple intro to dictionaries"""

def grade(score):
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    return grade

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {k: grade(v) for (k, v) in student_scores.items()}
print(student_grades)
