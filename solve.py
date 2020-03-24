from CardCall import *
from HSCall import *

def process_move(player_list, move_list):
    # fuck what do i do
    for move in move_list:
        if(isinstance(move, CardCall)):
            print("Processing CardCall")


        elif(isinstance(move, HSCall)):
            print("Processing HSCall")

        else:
            print("what")

