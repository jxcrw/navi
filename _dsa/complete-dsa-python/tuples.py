#!/usr/bin/env python3
"""Tuple sandbox"""

# Creation
my_tuple = (1, 2, 3, 4, 5)
tuple_single = (1,)
tuple_empty = tuple()
tuple_empty = ()
tuple_from_string = tuple('kthxwtfbbq')

# Access
print(my_tuple[2])
print(my_tuple[2:4])

# Traversal
for _ in my_tuple: # O(n)
    print(_)

for i in range(len(my_tuple)):
    print(my_tuple[i])

# Search
print(2 in my_tuple)

def search_linear(a_tuple, target):
    for i, _ in enumerate(a_tuple):
        if _ == target:
            return i
    return 'Specified target value not found.'

print(search_linear(my_tuple, 4))
print(search_linear(my_tuple, 6))

# Tuple operations/functions
print(my_tuple + tuple_single)
print(tuple_single * 4)

print(my_tuple.count(1))
print(my_tuple.index(3))

print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))

tuple_from_list = tuple([1, 2, 3])
