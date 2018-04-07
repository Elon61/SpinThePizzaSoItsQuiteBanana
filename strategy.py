import abc
import bet
import outcome


class PlayingStragtegy(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, gold):
        self._history = []
        self._base_gold = gold

    @abc.abstractmethod
    def new_bet(self):
        raise NotImplementedError

    def update_history(self, bet, won):
        self._history.append((bet, won))


class Strategyt1326(PlayingStragtegy):
    def __init__(self, base_gold=1948):
        PlayingStragtegy.__init__(self, base_gold)

    def new_bet(self):
        #new bet probably made from a selection from the main outcome builder.
        return bet.Bet(outcome.Outcome("10", 35), self._gold_multiplier1326() * self._base_gold)

    def _gold_multiplier1326(self):
        wins = 0
        for _, won in reversed(self._history[-4:]):
            if won:
                wins += 1
            else:
                return 1

        return self._gold_mult_switch(wins)

    def _gold_mult_switch(self, x):
        return {
            1: 3,
            2: 2,
            3: 6
        }.get(x, 1)


class StrategytMartin(PlayingStragtegy):
    def __init__(self, base_gold=1948):
        PlayingStragtegy.__init__(self, base_gold)

    def new_bet(self):
        return bet.Bet(outcome.Outcome("10", 35), self._losses() * self._base_gold)

    def _losses(self):
        losses = 0
        for i in xrange(len(self._history)):
            if not self._history[-i][1]:
                losses += 1
            else:
                return losses
            return losses