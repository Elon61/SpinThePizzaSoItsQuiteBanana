import outcome
import spinner
class Bin(set):
    pass

class BinBuilder(object):
    def __init__(self, spin):
        _spin = spin
    def straight(self):
        for num in xrange(1, 37):
            self._spin.addOutcome(num, outcome.Outcome(num, 35))

    def split(self):
        pass

    def street(self):
        pass

    def corner(self):
        pass

    def line(self):
        pass