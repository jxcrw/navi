#!/usr/bin/env python3
"""While loops with Reeborg's World"""

# Solution to Reeborg's World Hurdle 2
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

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

while not at_goal():
    hurdle()
