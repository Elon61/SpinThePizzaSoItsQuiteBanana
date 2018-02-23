class Bet(object):
    def __init__(self, outcome, gold):
        self._outcome = outcome
        self._gold = gold

    def get_outcome(self):
        return self._outcome

    def getGold(self):
        return self._gold