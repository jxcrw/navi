#!/usr/bin/env python3

def print_pairs(array):
    for i in array: # O(n)
        for j in array: # O(n)
            print(f"{i}, {j}") # O(1)

# ⇒ O(n^2)
