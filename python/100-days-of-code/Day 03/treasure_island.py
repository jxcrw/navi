#!/usr/bin/env python3
"""Simple text-based choose your own adventure game"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice_1 = input("Every journey starts at a fork in the road. Go left or right? ").lower()
if choice_1 != 'left':
    print("You fell into a hole and died. Game over.")
    quit()

choice_2 = input("As you go down the road, you find a lake. Swim or wait?").lower()
if choice_2 != 'wait':
    print("You were eaten by trout and died. Game over.")
    quit()

choice_3 = input("A boat arrives and takes you to the island. There you find a building with three doors. Go through "
                 "the red, blue, or yellow door?").lower()
if choice_3 == 'red':
    print("You were burned by a fire and died. Game over.")
    quit()
elif choice_3 == 'blue':
    print("You were eaten by beasts and died. Game over.")
    quit()
elif choice_3 == 'yellow':
    print("You found the treasure and win. Congratulations!")
else:
    print("You didn't go through any of the doors and died. Game over.")
    quit()
