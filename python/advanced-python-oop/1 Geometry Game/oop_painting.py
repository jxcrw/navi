#!/usr/bin/env python3
"""Scratchpad for exercises in course section 3"""

class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        num_buckets = self.wall_area * 2.5
        return num_buckets


class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        if self.color == 'white':
            price = self.buckets * 1.99
        else:
            price = self.buckets * 2.19
        return price

class PaintDiscounted(Paint):

    def discounted_price(self, discount_percentage):
        price = self.total_price() * (1 - discount_percentage/100)
        return price
