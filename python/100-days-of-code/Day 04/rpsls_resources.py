#!/usr/bin/env python3
"""Resources for RPSLS game"""

# Game results
result_win = "You win!"
result_loss = "You lose!"
result_tie = "Tie!"

# Signal names
name_rock = 'Rock'
name_paper = 'Paper'
name_scissors = 'Scissors'
name_lizard = 'Lizard'
name_spock = 'Spock'

# Signal combination messages
message_scissors_paper = "Scissors cuts Paper. "
message_paper_rock = "Paper covers Rock. "
message_rock_lizard = "Rock crushes Lizard. "
message_lizard_spock = "Lizard poisons Spock. "
message_spock_scissors = "Spock smashes Scissors. "
message_scissors_lizard = "Scissors decapitates Lizard. "
message_lizard_paper = "Lizard eats Paper. "
message_paper_spock = "Paper disproves Spock. "
message_spock_rock = "Spock vaporizes Rock. "
message_rock_scissors = "Rock crushes Scissors. "

# ASCII art for game signals
ascii_rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

ascii_paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

ascii_scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_lizard = '''     _
   _| |
 _| | |
| | | | __
| | | |/  \\
|       /\ \\
|      /  \/
|      \  /\\
|       \/ /
 \        /
  |     /
  |    |
'''

ascii_spock = ''' __      __
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === |
'''

# VLT Dictionaries (VLT = Victory, Loss, Tie)
vlt_dict_rock = {name_rock: result_tie,
                 name_paper: message_paper_rock + result_loss,
                 name_scissors: message_rock_scissors + result_win,
                 name_lizard: message_rock_lizard + result_win,
                 name_spock: message_spock_rock + result_loss}

vlt_dict_paper = {name_rock: message_paper_rock + result_win,
                  name_paper: result_tie,
                  name_scissors: message_scissors_paper + result_loss,
                  name_lizard: message_lizard_paper + result_loss,
                  name_spock: message_paper_spock + result_win}

vlt_dict_scissors = {name_rock: message_rock_scissors + result_loss,
                     name_paper: message_scissors_paper + result_win,
                     name_scissors: result_tie,
                     name_lizard: message_scissors_lizard + result_win,
                     name_spock: message_spock_scissors + result_loss}

vlt_dict_lizard = {name_rock: message_rock_lizard + result_loss,
                   name_paper: message_lizard_paper + result_win,
                   name_scissors: message_scissors_lizard + result_loss,
                   name_lizard: result_tie,
                   name_spock: message_lizard_spock + result_win}

vlt_dict_spock = {name_rock: message_spock_rock + result_win,
                  name_paper: message_paper_spock + result_loss,
                  name_scissors: message_spock_scissors + result_win,
                  name_lizard: message_lizard_spock + result_loss,
                  name_spock: result_tie}
