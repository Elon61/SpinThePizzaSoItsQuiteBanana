import table, spinner
class Game(object):
    def __init__(self, players, bank=1000000):
        self._bets2players = {}
        self._players = players
        self._bank = bank
        self._spin_It = spinner.Spinner()
        self._table = table.Table()

    def _fetch_bets(self):
        for players in self._players:
            bet = players.new_bet()
            self._bets2players[bet] = players

    def _put_bets_on_table(self):
        for bet in self._bets2players:
            self._table.add_bet(bet)

    def _notify_players(self, wb, lb):
        for bet in wb:
            self._bets2players[bet].won_bet(bet)
        for bet in lb:
            self._bets2players[bet].lost_bet(bet)

    def play_round(self):
        self._table.reset()
        self._bets2players = {}
        self._fetch_bets()
        self._put_bets_on_table()
        wowtcome = self._spin_It.spin()
        winning_bets = self._table.get_winning_bets(wowtcome)
        losing_bets = self._table.get_losing_bets(wowtcome)