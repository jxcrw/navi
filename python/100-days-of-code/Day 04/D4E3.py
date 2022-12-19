#!/usr/bin/env python3
"""Nested lists - treasure map game"""

row1 = ['⬜','⬜','⬜']
row2 = ['⬜','⬜','⬜']
row3 = ['⬜','⬜','⬜']
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

column_index = int(position[0]) - 1
row_index = int(position[1]) - 1
treasure_map[row_index][column_index] = 'X'

print(f"{row1}\n{row2}\n{row3}")
