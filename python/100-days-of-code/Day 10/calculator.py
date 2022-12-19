#!/usr/bin/env python3
"""Simple calculator program"""

LOGO = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

OPERATIONS_DICT = {'+': add, '-': subtract, '*': multiply, '/': divide}
MESSAGE_OPERATION_SYMBOL = f"Enter the desired operation ({' '.join([k for k in OPERATIONS_DICT])}): "

def calculate():
    n1 = float(input("What's the first number? "))
    while True:
        operation_symbol = input(MESSAGE_OPERATION_SYMBOL).strip()
        n2 = float(input("What's the next number? "))
        operation_function = OPERATIONS_DICT[operation_symbol]
        answer = operation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}\n")

        should_continue = input(f"Enter 'y' to continue with {answer}, or 'n' to start fresh: ").strip()
        if should_continue == 'y':
            n1 = answer
        else:
            calculate()

calculate()
