import table, spinner
class Game(object):
    def __init__(self, players, bank=1000000):
        self._bets2players = {}
        self._players = players
        self._bank = bank
        self._spin_It = spinner.Spinner()
        self._table = table.Table()

    def _fetch_bets(self):
        for p in self._players:
            bet = p.new_bet()
            self._bets2players[bet] = p

    def _put_bets_on_table(self):
        for t in self._bets2players:
            self._table.add_bet(t)

    def play_round(self):
        self.table
        wowtcome = self._spin_It.spin()
        winning_bets = self._table.get_winning_bets(wowtcome)
        losing_bets = self._table.get_losing_bets(wowtcome)