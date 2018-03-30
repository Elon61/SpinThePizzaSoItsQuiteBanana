import bin_stuff
import random


class Spinner(object):
    SPINNER_SIZE = 38

    def __init__(self, builder=bin_stuff.BinBuilder()):
        self._bin = self._bin()
        builder.allthestuffgoesherebutnotreally(self)
        pass

    def _bins(self):
        return [bin_stuff.Bin([]) for _ in xrange(Spinner.SPINNER_SIZE)]

    def spin(self):
        return random.choice(self._bin)

    def add_outcome(self, numDex, outcomed):
        """
        takes index in the tuple of bins. take bin at that place. add 'outcome' to that bin
        changes __bins
        """
        bns = self._bin[numDex]
        bns.add(outcomed)
        self._bin[numDex] = bns
    pass
3