#!/usr/bin/env python3
"""Geometry game"""

from random import randint
from classes import *

point_random_1 = Point(randint(0, 400), randint(0, 400))
point_random_2 = Point(randint(10, 400), randint(10, 400))
rectangle_random = RectangleGUI(point_random_1, point_random_2)

point_user = PointGUI(int(input("Guess X: ")), int(input("Guess Y: ")))
area_user = int(input("Guess rectangle area: "))

in_rectangle = rectangle_random.contains_point(point_user)
area_difference = abs(area_user - rectangle_random.calculate_area())
print(f"Point was inside rectangle: {in_rectangle}")
print(f"Your area guess was off by: {area_difference}")

canvas = turtle.Turtle()
rectangle_random.draw(canvas)
point_user.draw(canvas)
turtle.done()
