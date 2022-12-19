#!/usr/bin/env python3

def print_unordered_pairs(arrayA, arrayB):
    for i in range(len(arrayA)): # O(n), where n = len(arrayA)
        for j in range(len(arrayB)): # O(m), where m = len(arrayB)
            for k in range(100_000): # O(100000) = O(1)
                print(f"{arrayA[i]}, {arrayB[j]}") # O(1)

# ⇒ O(n * m) again
