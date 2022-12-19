#!/usr/bin/env python3
"""Main Blackjack game file"""

from time import sleep

from dealer import Dealer
from deck import Deck
from hand import Hand

LOGO = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|J /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ J|                            _/ |                
      `------'                           |__/           
"""

PAUSE_SHORT = 1 # seconds
PAUSE_LONG = PAUSE_SHORT * 3

def display_hands(hand_dealer, hand_player):
    print(f"\nDealer hand: {hand_dealer}")
    print(f"Player hand: {hand_player}\n")

def ask_keep_playing():
    """Ask if the player wants to keep playing."""
    play_again = input("\nPlay again ('y' or 'n')? ").lower().strip()
    return play_again == 'y'

# ─────────────────────────────────────────────────────────────────────────────

print(LOGO)
print("Welcome to Blackjack!")
sleep(0.75)

keep_playing = True
while keep_playing:
    # Initialization
    deck = Deck()
    deck.shuffle()
    hand_player = Hand([])
    hand_dealer = Hand([])

    print("\n##### Dealing cards... #####")
    sleep(PAUSE_SHORT)
    for _ in range(2):
        hand_player.add_card(deck.next())
        hand_dealer.add_card(deck.next())

    # Player turn
    hand_dealer.cards[0].visible = False # Hide dealer hole card during player turn
    hit_or_stand = ''
    while (hit_or_stand != 'stand') and (not hand_player.is_bust()):
        display_hands(hand_dealer, hand_player)
        hit_or_stand = input("Hit or stand? ").lower().strip()
        if hit_or_stand == 'hit':
            hand_player.add_card(deck.next())
            sleep(PAUSE_SHORT)

    # Dealer turn
    sleep(PAUSE_SHORT)
    print("\nDealer reveals hole card...")
    hand_dealer.cards[0].visible = True
    display_hands(hand_dealer, hand_player)
    sleep(PAUSE_LONG)
    dealer = Dealer(hand_dealer)
    while dealer.wants_hit() and (not hand_dealer.is_bust()):
        print("Dealer hits...")
        hand_dealer.add_card(deck.next())
        display_hands(hand_dealer, hand_player)
        sleep(PAUSE_LONG)

    # Showdown
    max_player = hand_player.max_value()
    max_dealer = hand_dealer.max_value()
    print(f"Dealer stands at: {max_dealer}\n")
    sleep(PAUSE_SHORT)
    if hand_player.is_bust() and hand_dealer.is_bust():
        print("##### Push! You both busted! #####")
    elif hand_player.is_bust():
        print("##### Bust! You lose! #####")
    elif hand_dealer.is_bust():
        print("##### Dealer busts! You win! #####")
    elif max_player == max_dealer:
        print("##### Push! #####")
    elif max_player > max_dealer:
        print("##### You win! #####")
    elif max_player < max_dealer:
        print("##### You lose! #####")

    keep_playing = ask_keep_playing()
