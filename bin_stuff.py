import outcome
import spinner
class Bin(frozenset):
    pass

class BinBuilder(object):
    def straight(self):
        for num in xrange(1, 37):
            spinner.Spinner().bins()[num] = outcome.Outcome(num, 35)
