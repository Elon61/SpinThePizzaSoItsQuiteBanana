from bet import *
from outcome import *
import random
class Player(object):
    def __init__(self, gold=0, mood='tired', swim_skills=False):
        self._gold = gold
        self._wins = 0
        self._losses = 0
        self._mood = mood
        self._can_swim = swim_skills
        self._bet_history = []

    def won_bet(self, bet):
        """
        :return: Next time you won't get so lucky.
        """
        self._wins += 1
        self._mood += 10
        self._gold += bet.get_win_amount()
        self._bet_history.append((bet, True))

    def lost_bet(self, bet):
        """
        :return: Sadness.
        """
        self._losses -= 1
        self._mood -= 1
        self._gold -= bet.get_lose_amount()
        self._bet_history.append((bet, False))

    def new_bet(self):
        """
        :return: a new bet
        """
        return Bet(Outcome("10", 35), random.randint(0, self._gold))

    def get_mood(self):
        return self._losses + 10 * self._wins
