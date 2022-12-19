#!/usr/bin/env python3

def print_unordered_pairs(array):
    for i in range(0, len(array)): # O(n)
        for j in range(i + 1, len(array)): # ≈O(n/2) by average work
            print(f"{array[i]}, {array[j]}") # O(1)

# ⇒ O(n^2)
