class Outcome(object):
    def __init__(self, name, odds):
        self._name = name
        self._odds = int(odds)

    def __eq__(self, other):
        return self._name == other.__name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return "{} ({}:1)".format(self._name, self._odds)

    def __repr__(self):
        return "Outcome({} {})".format(self._name, self._odds)

class Bin(frozenset):
    pass

class Wheel(object):
    def __init__(self):
        pass
    def bins(self):
        return tuple(Bin() for i in range(38))

    def rng(self):
        pass

    pass

class BinBuilder(object):
    def straight(self):
        for num in xrange(1, 37):
            Wheel().bins()[num] = Outcome(num, 35)