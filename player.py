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
        self._betHistory = []

    def won_bet(self, bet):
        """
        :return: Next time you won't get so lucky.
        """
        self._wins += 1
        self._mood += 1
        self._gold += bet.get_outcome().winAmount(bet.getGold)
        self._betHistory.append((bet, True))

    def lost_bet(self, bet):
        """
        :return: Sadness.
        """
        self._losses -= 1
        self._mood -= 1
        self._gold -= bet.get_outcome().loseAmount(bet.getGold)
        self._betHistory.append((bet, False))

    def new_bet(self):
        """
        :return: a new bet
        """
        return Bet(Outcome("10", 35), random.randint(0, self._gold))
