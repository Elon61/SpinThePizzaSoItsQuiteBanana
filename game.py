import table, spinner
class Game(object):
    def __init__(self, players, bank=1000000):
        self._bets2players = {}
        self._players = players
        self._bank = bank
        self._spin_It = spinner.Spinner()
        self._table = table.Table()

    def _notify_players(self, won_bet, lost_bet):
        for bet in won_bet:
            self._bets2players[bet].won_bet(bet)
        for bet in lost_bet:
            self._bets2players[bet].lost_bet(bet)

    def play_round(self):
        curr_round = game_round(self._players, self._spin_It)

class game_round(object):
    def __init__(self, players, spin_It):
        self._table = table.Table()
        self._bets2players = {}
        self._players = players
        self._spin_It = spin_It

    def _fetch_bets(self):
        for player in self._players:
            bet = player.new_bet()
            self._bets2players[bet] = player

    def _put_bets_on_table(self):
        for bet in self._bets2players:
            self._table.add_bet(bet)

    def play(self):
        self._fetch_bets()
        self._put_bets_on_table()
        wowtcome = self._spin_It.spin()
        winning_bets = self._table.get_winning_bets(wowtcome)
        losing_bets = self._table.get_losing_bets(wowtcome)
