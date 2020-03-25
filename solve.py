from CardCall import *
from HSCall import *


# take in player_list and move_list and return the probabilities from each
# player's perspective from player 0's perspective. (this means that the
# starting hand for player 0 is public to santiago)
def process_move(player_list, move_list):
    # fuck what do i do

    probabilities = [[[[] for _ in range(52)] for _ in range(len(player_list))] for _ in range(len(player_list))]

    # all the probabilities start at 1/5 except for the ones currently held in
    # your hand

    # each player has a different persepective so the probabilities can only be
    # calcualated from one person, let player 0 be the person calculating the
    # probabilities: the optimal moves change depending on the information that
    # each player has

    # i will keep the exact cards in player 0's hand in the information file
    # that the move data comes from, but for realtime game, this cannot actually
    # be accurately calculated without knowing the starting hands.

    for move in move_list:
        if(isinstance(move, CardCall)):
            print("Processing CardCall")


        elif(isinstance(move, HSCall)):
            print("Processing HSCall")

        else:
            print("what")

