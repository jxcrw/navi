#!/usr/bin/env python3
"""Python list deep dive."""

import numpy as np

# Creation
integers = [1, 2, 3, 4]
strings = ['milk', 'cheese', 'butter']
mixed = integers + strings
nested = [integers, strings]
empty = []

# Access/Traversal
print("\nAccess/Traversal")
my_element = strings[0]
print(3 in integers) # in operator
for _ in integers:
    print(_)

# Update/Insert
my_list = [1, 2, 3, 4, 5, 6, 7]
my_list[2] = 33

my_list.insert(0, 11)
my_list.insert(5, 123456789)

my_list.append(44)

your_list = [11, 12, 13, 14]
my_list.extend(your_list)

# Slice/Delete
print("\nSlice/Delete")
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(my_list[0:2])
print(my_list[:2])
print(my_list[2:])

my_list[0:2] = ['x', 'y']

my_list.pop(1)
print(my_list)

del my_list[0]
print(my_list)

my_list.remove('e')
print(my_list)

# Searching
print("\nSearching")
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(20 in my_list)

def linear_search(search_list, target_value):
    for i, element in enumerate(search_list):
        if element == target_value:
            return i
    return 'Value not found :( !'

print(linear_search(my_list, 80))

# List Operations/Functions
print("\nList Operations/Functions")
my_list = [1, 2, 3]
your_list = [4, 5, 6]
print(my_list + your_list)

print(my_list * 4)

print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sum(my_list) / len(my_list))

# Lists and Strings
print("\nLists and Strings")
my_string = 'Test test test this is only a test.'
print(list(my_string))
print(my_string.split())
print(' '.join(my_string.split()))

# Lists versus Arrays
print("\nLists versus Arrays")
my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_array / 2) # Arrays optimized for arithmetic operations.

my_list = [1, 2, 3, 4, 5, 'a'] # Lists can contain elements of different data types.
my_array = np.array([1, 2, 3, 4, 5, 'a'])
print(my_list)
print(my_array)
