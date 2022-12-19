#!/usr/bin/env python3
"""Password generator"""

import random

tokens = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
          '!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
length = int(input("How long would you like the password to be? "))

password_list = random.choices(tokens, k=length)
random.shuffle(password_list)

password_final = ''.join(password_list)
print(f"Your password is: {password_final}")
