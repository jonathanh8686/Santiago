
class HSCall():

    VALUES = list(map(str, [1,2,3,4,5,6,7,8,9,10,11,12,13]))
    SUITS = ["S", "H", "D", "C"]
    CARDS = []

    claim = {}
    for i in range(len(VALUES)):
        for j in range(len(SUITS)):
            CARDS.append(VALUES[i] + SUITS[j])


    def __init__(self, player_caller, hs, call_string):
        # initalize cards
        self.player_caller = player_caller
        self.hs = hs
        self.call_string = call_string

        csarr = call_string.split(" ")
        curr_player = ""
        for i in csarr:
            if i not in self.CARDS:
                curr_player = i
                self.claim[i] = []
                # this is the name of a player
            else:
                self.claim[curr_player].append(i)

    def  __repr__(self):
        repr_str = ""
        repr_str += self.player_caller + "\tcalled for the\t" + self.hs + "\twith\n"

        for key, val in self.claim.items():
            repr_str += str(key) + str(val) + "\n"
        return repr_str


