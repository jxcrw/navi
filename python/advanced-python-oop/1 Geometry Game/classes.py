#!/usr/bin/env python3
"""Class definitions"""

import turtle
from math import sqrt


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_to(self, point: 'Point'):
        """Calculate the distance from self to the specified `point`."""
        a_squared = (point.x - self.x) ** 2
        b_squared = (point.y - self.y) ** 2
        c = sqrt(a_squared + b_squared)
        return c


class Rectangle:

    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.width = abs(self.calculate_width())
        self.height = abs(self.calculate_height())

    def contains_point(self, point: Point):
        """Determine if the specified `point` falls within the rectangle."""
        if (self.point_1.x < point.x < self.point_2.x) and (self.point_1.y < point.y < self.point_2.y):
            return True
        else:
            return False

    def calculate_width(self):
        """Calculate the width of the rectangle."""
        width = self.point_2.x - self.point_1.x
        return width

    def calculate_height(self):
        """Calculate the height of the rectangle."""
        height = self.point_2.x - self.point_1.y
        return height

    def calculate_area(self):
        """Calculate the area of the rectangle."""
        area = abs(self.width * self.height)
        return area


class RectangleGUI(Rectangle):

    def draw(self, canvas: turtle.Turtle):
        canvas.penup()
        canvas.goto(self.point_1.x, self.point_1.y)
        canvas.pendown()
        canvas.forward(self.width)
        canvas.left(90)
        canvas.forward(self.height)
        canvas.left(90)
        canvas.forward(self.width)
        canvas.left(90)
        canvas.forward(self.height)

class PointGUI(Point):

    def draw(self, canvas: turtle.Turtle, size: int=5, color: str='blue'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


if __name__ == '__main__':
    pass
