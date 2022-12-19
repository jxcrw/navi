#!/usr/bin/env python3
"""Caesar cipher"""

TOKENS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '?']
LOGO = '''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88'''

def caesar_cipher(string, shift, mode):
    if mode == 'decode':
        shift *= -1
    shift_modulo = shift % len(TOKENS)
    tokens_shifted = TOKENS[shift_modulo:] + TOKENS[:shift_modulo]

    string_processed = ''
    for c in string:
        if c in TOKENS:
            index = TOKENS.index(c)
            string_processed += tokens_shifted[index]
        else:
            string_processed += c
    return string_processed

# ─────────────────────────────────────────────────────────────────────────────

print(LOGO)
while(True):
    mode = input("\nType 'encode' to encode, or 'decode' to decode: ").lower().strip()
    text = input("Enter your message: ").lower()
    shift = int(input("Enter the desired shift: "))

    text_processed = caesar_cipher(text, shift, mode)
    print(f"The {mode}d message is: {text_processed}\n")

    keep_going = input("Would you like to continue? 'y' or 'n': ").lower().strip()
    if keep_going != 'y':
        break
