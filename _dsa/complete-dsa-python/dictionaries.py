#!/usr/bin/env python3
"""Simple dictionary sandbox"""

# Creation
my_dictionary = dict()
my_dictionary = {}
my_dictionary = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# Access
one_spanish = my_dictionary['one']

# Insert/Update
my_dictionary['four'] = 'cuatro' # O(1)
my_dictionary['one'] = 'ichi' # O(1)

# Traverse
for k in my_dictionary: # O(n)
    print(k)

for k, v in my_dictionary.items(): # O(n)
    print(k, v)

# Search (linear) (O(n))
def search_linear(dictionary, value):
    for k in dictionary:
        if dictionary[k] == value:
            return k, value
    return 'The specified value does not exist!'

print(search_linear(my_dictionary, "dos"))

# Delete/remove (O(1); amortized O(n))
popped = my_dictionary.pop('one')
popped_item = my_dictionary.popitem()
print(popped, popped_item)

del my_dictionary['two']
my_dictionary.clear()
# del my_dictionary

# Method Summary
my_dictionary = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
your_dictionary = my_dictionary.copy()
our_dictionary = {}.fromkeys([1, 2, 3], 0)

print(my_dictionary.get('one', 'unknown'))
print(my_dictionary.get('five', 'unknown'))

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

print(my_dictionary.setdefault('five', 'unknown'))

another_dictionary = {'one': 'ichi', 'two': 'ni', 'three': 'san', 'four': 'yon'}
my_dictionary.update(another_dictionary)
print(my_dictionary)

# Dictionary Operations and Built-ins
print('one' in my_dictionary) # O(1) (!)
print(all(my_dictionary))
print(any(my_dictionary))
print(len(my_dictionary))
print(sorted(my_dictionary, reverse=False, key=len))
