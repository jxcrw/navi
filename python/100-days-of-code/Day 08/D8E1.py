#!/usr/bin/env python3
"""Functions with parameters - paint area calculator"""

import math

def calc_paint_cans(wall_height, wall_width, coverage):
    cans_float = wall_height * wall_width / coverage
    cans_whole = math.ceil(cans_float) # Not possible to buy partial cans of paint
    return int(cans_whole)

wall_height = int(input("Height of wall: "))
wall_width = int(input("Width of wall: "))
coverage = 5

cans_required = calc_paint_cans(wall_height, wall_width, coverage)

print(f"You'll need {cans_required} cans of paint.")
