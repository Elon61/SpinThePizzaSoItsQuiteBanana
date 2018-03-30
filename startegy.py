import abc
import bet
import outcome

class PlayingSAtragtegy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_bet(self, history):
        raise NotImplementedError


class Strategyt1326(PlayingSAtragtegy):
    def __init__(self, history, base_gold=1948):
        self._history = history
        self._base_gold = base_gold

    def new_bet(self, history): # new bet probably made from a selection from the main outcome builder.
        self._history = history

        return bet.Bet(outcome.Outcome("10", 35), self._gold_multiplier1326())

    def _gold_multiplier1326(self):
        wins = 0
        for i in xrange(1, 1 + max(min(4, len(self._history)), 0)):
            if self._history[-i][1]:
                wins += 1
            else:
                wins = 0
            return self._gold_mult_switch(wins)

    def _gold_mult_switch(self, x):
        return {
            1: 3,
            2: 2,
            3: 6
        }.get(x, 1)

    def _prev_gold(self):
        if len(self._history) == 0: prev_gold = self._base_gold
        else: prev_gold = self._history[-1]
        return prev_gold

class StrategytMartin(PlayingSAtragtegy):
    def __init__(self, history, base_gold=1948):
        self._history = history
        self._base_gold = base_gold

    def new_bet(self, history):
        self._history = history

        return bet.Bet(outcome.Outcome("10", 35), self._losses() * self._base_gold)

    def _losses(self):
        losses = 0
        for i in xrange(len(self._history)):
            if not self._history[-i][1]:
                losses += 1
            else:
                return losses
            return losses