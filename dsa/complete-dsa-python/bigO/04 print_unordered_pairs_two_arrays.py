#!/usr/bin/env python3

def print_unordered_pairs(arrayA, arrayB):
    for i in range(len(arrayA)): # O(n), where n = len(arrayA)
        for j in range(len(arrayB)): # O(m), where m = len(arrayB)
            if arrayA[i] < arrayB[j]: # O(1)
                print(f"{i}, {j}") # O(1)

# ⇒ O(n * m)
