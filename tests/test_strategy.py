import unittest
import strategy

class TestStrategy(unittest.TestCase):

    def test_strategy1326(self):
        gold = 310964
        betgold = 29
        strat = strategy.Strategyt1326(betgold)
        bet = strat.new_bet()
        strat.update_history(bet, True)

        bet = strat.new_bet()
        strat.update_history(bet, True)

        bet = strat.new_bet()
        strat.update_history(bet, True)

        bet = strat.new_bet()
        self.assertEquals(bet.get_lose_amount(), 6 * betgold)

    def test_strategy1326_2(self):
        gold = 310964
        betgold = 29
        strat = strategy.Strategyt1326(betgold)
        bet = strat.new_bet()
        strat.update_history(bet, True)

        bet = strat.new_bet()
        strat.update_history(bet, True)

        bet = strat.new_bet()
        strat.update_history(bet, False)


        bet = strat.new_bet()
        self.assertEquals(bet.get_lose_amount(), 1 * betgold)
