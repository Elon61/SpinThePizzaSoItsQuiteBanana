import table
class Game(object):
    def __init__(self, players, bank=1000000):
        self._bets2players = {}
        self._players = players
        self._bank = bank
        self._curr_table = table.Table()
        self._outcomes = 0 # outcome list?

    def _fetch_bets(self):
        for p in self._players:
            bet = p.new_bet()
            self._bets2players[bet] = p

    def _put_bets_on_table(self):
        for t in self._bets2players:
            self._curr_table.add_bet(t)

    def play_round(self):
        pass

    def _spin_wheel(self):
        pass