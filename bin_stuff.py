import outcome
import spinner
class Bin(set):
    pass

class BinBuilder(object):
    def __init__(self):
        pass

    def straight(self, spin):
        for num in xrange(0, 37):
            spin.addOutcome(num, outcome.Outcome(str(num), 35))
        spin.addOutcome(37, outcome.Outcome("00", 35))

    def split(self, spin):
        for num in xrange(1, 37):
            if num % 3 == 0:
                #all the right row
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num, num + 1), 17))

            if (num - 1) % 3 == 0:
                #all the left row
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num, num - 1), 17))

            if num > 3:
                #all but 1, 2 and 3
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num, num - 3), 17))

            if num < 34:
                #all but 34, 35, 36
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num, num + 3), 17))

    def street(self):
        pass

    def corner(self):
        pass

    def line(self):
        pass