#!/usr/bin/env python3
"""Reeborg's World Maze"""

def turn_right():
    [turn_left() for _ in range(3)]

def move_left():
    turn_left()
    move()

def move_right():
    turn_right()
    move()

while not at_goal():
    if right_is_clear():
        move_right()
    elif front_is_clear():
        move()
    else:
        turn_left()
