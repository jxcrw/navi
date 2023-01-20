#!/usr/bin/env python3
"""Various array operations"""

from array import *

my_array = array('i', [1, 2, 3, 4, 5]) # Creation

for i in my_array: # Traversal
    print(i)

my_element = my_array[0] # Access
my_array.append(6) # Append
my_array.insert(0, 0) # Insert
my_array.extend([7, 8, 9]) # Extend
my_array.fromlist([10, 11, 12]) # Alternate way of adding
my_array.remove(12) # Remove any element
my_array.pop() # Pop last item

my_index = my_array.index(4) # Find index
my_array.reverse() # Reverse

print(my_array.buffer_info()) # Get buffer info

my_count = my_array.count(10) # Count occurrences of element

my_bytes = my_array.tobytes() # Byte operations
original_array = array('i')
original_array.frombytes(my_bytes)

my_list = my_array.tolist() # Convert to list

print(my_array[0:5]) # Slicing
