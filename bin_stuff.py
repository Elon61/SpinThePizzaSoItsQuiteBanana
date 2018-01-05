import outcome
import spinner
class Bin(set):
    pass

class BinBuilder(object):
    def __init__(self):
        pass

    def straight(self, spin):
        for num in xrange(1, 37):
            spin.addOutcome(num, outcome.Outcome(num, 35))
        spin.addOutcome(37, outcome.Outcome("00", 35))
        spin.addOutcome(0, outcome.Outcome("0", 35))

    def split(self):
        pass

    def street(self):
        pass

    def corner(self):
        pass

    def line(self):
        pass