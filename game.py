import table, spinner
class Game(object):
    def __init__(self, players, bank=1000000):
        self._bets2players = {}
        self._players = players
        self._bank = bank
        self._spin_It = spinner.Spinner
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
        wowtcome = self._spin_It.spin()
        win_bet = self._curr_table.get_winning_bet(wowtcome)
        lose_bet = self._curr_table.get_losing_bets(wowtcome)