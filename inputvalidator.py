
def isValidInput(player_list, move_list, inp):
    if(len(inp) < 3):
        return False

    if(len(inp) == 3):
        if(inp[0] not in player_list):
            return False
        if(inp[1] not in player_list):
            return False
    else:
        if(inp[0] not in player_list):
            return False
        if(inp[1] not in ["S+", "S-", "C+", "C-", "H+", "H-", "D+", "D-", "J8"]):
            return False

    return True
