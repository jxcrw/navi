#!/usr/bin/env python3

def foo(array):
    sum = 0 # O(1)
    product = 1 # O(1)

    for i in array: # O(n)
        sum += 1 # O(1)
    for i in array: # O(n)
        product *= i # O(1)
    print(f"Sum = {sum}, Product = {product}") # O(1)

# ⇒ O(n)
