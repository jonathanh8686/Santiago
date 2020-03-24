from Card import Card
from inputvalidator import isValidInput
from CardCall import *

print("Initalizing Deck")
NUM_PLAYERS = 6
VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
SUITS = ["S", "H", "D", "C"]

DECK = []
for i in range(len(VALUES)):
    for j in range(len(SUITS)):
        DECK.append(Card(VALUES[i], SUITS[j]))
DECK.append(Card("J", "+")) # big joker
DECK.append(Card("J", "-")) # smol joker

print("Deck Initalized")

move_list, player_list = [], []
print("Game Started!")

print("Enter Player Information:")
# sitting in a circle, go around
for i in range(NUM_PLAYERS):
    print(f"Player {i}:", end="\t")
    player_list.append(input().strip())

while(True):
    print("Enter Move:")
    move_dat = input().strip().split(" ")
    if(isValidInput(player_list, move_list, move_dat) == False):
        print("Invalid Input!")
        continue

    if(len(move_dat) == 3):
        # p1 p2 card
        # cardcall

        called_card = Card(move_dat[2][:-1], move_dat[2][-1])
        print(called_card)
        move = CardCall(move_dat[0], move_dat[1], called_card)
        print(move)
        move_list.append(move)

    else:
        # p1 hs callstring (min length 7)
        # hscall
        pass


