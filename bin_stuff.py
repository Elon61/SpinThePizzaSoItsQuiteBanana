import outcome
import wheel
class Bin(frozenset):
    pass

class BinBuilder(object):
    def straight(self):
        for num in xrange(1, 37):
            wheel.Wheel().bins()[num] = outcome.Outcome(num, 35)
