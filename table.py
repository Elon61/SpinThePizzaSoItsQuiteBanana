class Table(object):
    def __init__(self):
        self._bets = []

    def add_bet(self, bet):
        self._bets.append(bet)

    def get_winning_bet(self, winning_outcomes):
        return [b for b in self._bets if b.get_outcome() in winning_outcomes]


    def get_losing_bets(self, winning_outcomes):
        return [b for b in self._bets if b.get_outcome() not in winning_outcomes]