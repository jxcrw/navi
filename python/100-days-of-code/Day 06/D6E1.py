#!/usr/bin/env python3
"""Introduction to functions with Reeborg's World"""

# Solution to Reeborg's World Hurdle 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    [turn_left() for _ in range(3)]

def move_left():
    turn_left()
    move()

def move_right():
    turn_right()
    move()

def hurdle():
    move()
    move_left()
    move_right()
    move_right()
    turn_left()

[hurdle() for _ in range(6)]
