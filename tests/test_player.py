import player
import unittest
import strategy

class TestPlayerBanana(unittest.TestCase):
    def test_win_thrice_validate_gold(self):
        gold = 10000
        p1 = player.Player(strategy.Strategyt1326(), gold)
        bet = p1.new_bet()
        gold += bet.get_win_amount()
        p1.won_bet(bet)
        bet = p1.new_bet()
        gold += bet.get_win_amount()
        p1.won_bet(bet)
        bet = p1.new_bet()
        gold += bet.get_win_amount()
        p1.won_bet(bet)
        self.assertEquals(gold, p1.get_gold())

