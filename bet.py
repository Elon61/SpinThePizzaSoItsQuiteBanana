class Bet(object):
    def __init__(self, outcome, gold):
        self._outcome = outcome
        self._gold = gold

    def get_outcome(self):
        return self._outcome

    def get_win_amount(self):
        return self.outcome().win_amount(self._gold)

    def get_lose_amount(self):
        return self.outcome().lose_amount(self._gold)