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
            if num % 3 != 0:
                #all but the right column
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num, num + 1), 17))

            if (num - 1) % 3 != 0:
                #all but the left column
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num - 1, num), 17))

            if num > 3:
                #all but 1, 2 and 3
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num - 3, num), 17))

            if num < 34:
                #all but 34, 35, 36
                spin.addOutcome(num, outcome.Outcome("{}-{}".format(num, num + 3), 17))

    def street(self, spin):
        for num in xrange(1, 37):
            if num % 3 == 0:
                #all the right column
                spin.addOutcome(num, outcome.Outcome("{}-{}-{}".format(num - 2, num - 1, num), 11))

            if (num - 1) % 3 == 0:
                #all the left column
                spin.addOutcome(num, outcome.Outcome("{}-{}-{}".format(num, num + 1, num + 2), 11))

            if (num - 2) % 3 == 0:
                #all the middle column
                spin.addOutcome(num, outcome.Outcome("{}-{}-{}".format(num - 1, num, num + 1), 11))


    def corner(self, spin):
        for num in xrange(1, 37):
            if num % 3 != 0 and num < 34:
                #all but right column and <34.
                spin.addOutcome(num, outcome.Outcome("{}-{}-{}-{}".format(num, num + 1, num + 3, num + 4), 8))

            if (num - 1) % 3 != 0 and num < 34:
                # all but left column and  <34.
                spin.addOutcome(num, outcome.Outcome("{}-{}-{}-{}".format(num - 1, num, num + 2, num + 3), 8))

            if num % 3 != 0 and num > 3:
                #all but right column.
                spin.addOutcome(num, outcome.Outcome("{}-{}-{}-{}".format(num - 3, num - 2, num, num + 1), 8))

            if (num - 1) % 3 != 0 and num > 3:
                # all but left column.
                spin.addOutcome(num, outcome.Outcome("{}-{}-{}-{}".format(num - 4, num - 3, num - 1, num), 8))


    def line(self):

        pass

def print_bin(bin):
    for i in xrange(0, 38):
        print "bin {}: ".format(i), [x for x in bin[i]]