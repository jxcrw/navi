#!/usr/bin/env python3

import numpy as np

# Creation
my_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(my_array)

# Insertion
new_array = np.insert(my_array, 0, [[1, 2, 3, 4]], axis=1)
print(new_array)

# Appending
new_array2 = np.append(my_array, [[1], [2], [3], [4]], axis=1)
print(new_array2)

# Access
my_element = my_array[1][2]

# Traversal
for i in range(len(my_array)):
    for j in range(len(my_array[0])):
        print(my_array[i][j])

# Search
def search(array_2D, element):
    """Linear search through 2D array."""
    for i in range(len(array_2D)):
        for j in range(len(array_2D[0])):
            if my_array[i][j] == element:
                return f"The value is located at index [i][j] = [{i}][{j}]"
    return "The element was not found."

print(search(my_array, 20))

# Deletion
new_array3 = np.delete(my_array, 0, axis=1)
print(new_array3)
