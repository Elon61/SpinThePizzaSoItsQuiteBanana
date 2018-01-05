import Outcome
import Wheel
class Bin(frozenset):
    pass

class BinBuilder(object):
    def straight(self):
        for num in xrange(1, 37):
            Wheel().bins()[num] = Outcome(num, 35)
