import bin_stuff
import outcome
import random

class Spinner(object):
    def __init__(self):
        self._bins = self.bins()
        buildCats = bin_stuff.BinBuilder()
        buildCats.allthestuffgoesherebutnotreally(self)
        pass

    def bins(self):
        return [bin_stuff.Bin([]) for i in range(38)]

    def rng(self):
        pass

    def spin(self):
        return random.choice(self._bins)

    def addOutcome(self, numDex, outcomed):
        """
        takes index in the tuple of bins. take bin at that place. add 'outcome' to that bin
        changes __bins
        """
        bns = self._bins[numDex]
        bns.add(outcomed)
        self._bins[numDex] = bns
    pass
