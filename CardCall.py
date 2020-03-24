
class CardCall():
    def __init__(self, playerCaller, playerCalled, card):
        self.playerCaller = playerCaller
        self.playerCalled = playerCalled
        self.card = card

    def __repr__(self):
        return self.playerCaller + "\tasked for the\t" + str(self.card) + "\tfrom\t" + str(self.playerCalled)


