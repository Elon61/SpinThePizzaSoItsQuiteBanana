import outcome
import spinner
class Bin(set):
    pass

class BinBuilder(object):
    def __init__(self):
        pass

    def allthestuffgoesherebutnotreally(self, spin):
        self.straight(spin)
        self.split(spin)
        self.street(spin)
        self.corner(spin)
        self.line(spin)
        self.twelve(spin)


    def straight(self, spin):
        for num in xrange(0, 37):
            spin.add_outcome(num, outcome.Outcome(str(num), 35))
        spin.add_outcome(37, outcome.Outcome("00", 35))

    def split(self, spin):
        for num in xrange(1, 37):
            if num % 3 != 0:
                #all but the right column
                spin.add_outcome(num, outcome.Outcome("{}-{}".format(num, num + 1), 17))

            if (num - 1) % 3 != 0:
                #all but the left column
                spin.add_outcome(num, outcome.Outcome("{}-{}".format(num - 1, num), 17))

            if num > 3:
                #all but 1, 2 and 3
                spin.add_outcome(num, outcome.Outcome("{}-{}".format(num - 3, num), 17))

            if num < 34:
                #all but 34, 35, 36
                spin.add_outcome(num, outcome.Outcome("{}-{}".format(num, num + 3), 17))

    def street(self, spin):
        for num in xrange(1, 37):
            if num % 3 == 0:
                #all the right column
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}".format(num - 2, num - 1, num), 11))

            if (num - 1) % 3 == 0:
                #all the left column
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}".format(num, num + 1, num + 2), 11))

            if (num - 2) % 3 == 0:
                #all the middle column
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}".format(num - 1, num, num + 1), 11))


    def corner(self, spin):
        for num in xrange(1, 37):
            if num % 3 != 0 and num < 34:
                #all but right column and <34.
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}-{}".format(num, num + 1, num + 3, num + 4), 8))

            if (num - 1) % 3 != 0 and num < 34:
                # all but left column and  <34.
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}-{}".format(num - 1, num, num + 2, num + 3), 8))

            if num % 3 != 0 and num > 3:
                #all but right column.
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}-{}".format(num - 3, num - 2, num, num + 1), 8))

            if (num - 1) % 3 != 0 and num > 3:
                # all but left column.
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}-{}".format(num - 4, num - 3, num - 1, num), 8))


    def line(self, spin):
        for num in xrange(1, 37):
            x = num - ((num + 2) % 3)
            if num > 3:
                y = x - 3
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}-{}-{}-{}".format(*[y + i for i in xrange(6)]), 5))
            if num < 34:
                spin.add_outcome(num, outcome.Outcome("{}-{}-{}-{}-{}-{}".format(*[x + i for i in xrange(6)]), 5))

    def twelve(self, spin):
        for num in xrange(1, 37):
            x = num - ((num - 1) % 12)
            spin.add_outcome(num, outcome.Outcome("{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(*[x + i for i in xrange(12)]), 2))

def print_bin(bin):
    for i in xrange(0, 38):
        print "bin {}: ".format(i), [x for x in bin[i]]