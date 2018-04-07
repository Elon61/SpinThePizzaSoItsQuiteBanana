import strategy

class Player(object):
    def __init__(self, strategy_1, gold=0, mood=1337, swim_skills=False):
        assert isinstance(strategy_1, strategy.PlayingStragtegy)
        self._gold = gold
        self._mood = mood
        self._can_swim = swim_skills
        self._strategy = strategy_1

    def won_bet(self, bet):
        """
        :return: Next time you won't get so lucky.
        """
        self._mood += 10
        self._gold += bet.get_win_amount()
        self._strategy.update_history(bet, True)

    def lost_bet(self, bet):
        """
        :return: Sadness.
        """
        self._mood -= 1
        self._gold -= bet.get_lose_amount()
        self._strategy.update_history(bet, False)

    def new_bet(self):
        """
        :return: a new bet
        """
        return self._strategy.new_bet()
        #return Bet(Outcome("10", 35), random.randint(0, self._gold))

    def get_mood(self):
        return self._mood

    def get_gold(self):
        return self._gold
