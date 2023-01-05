#!/usr/bin/python
"""Normalize all the text in a text file."""
# Jak Crow 2014/02/06

import ftfy
import os

cwd = os.getcwd()
print(cwd)
input('press any key to continue')

with open('test_forwide2narrow.txt', 'r', encoding='utf-8') as file:
    # drug_data = [line.rstrip() for line in file]
    my_data = file.readlines()

#Now fix the text. Convert half-width chars to full-width and full-width nums to half-width.
my_data = [ftfy.fix_text(line) for line in my_data]

with open('test_forwide2narrow_normalized.txt', 'w+', encoding='utf-8') as file:
        file.writelines(my_data)

