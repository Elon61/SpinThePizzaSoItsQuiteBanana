import bin_stuff
import outcome

class Spinner(object):
    def __init__(self):
        self._bins = self.bins()
        pass

    def bins(self):
        return [bin_stuff.Bin(str(i)) for i in range(38)]

    def rng(self):
        pass

    def addOutcome(self, numDex, outcomed):
        """
        takes index in the tuple of bins. take bin at that place. add 'outcome' to that bin
        changes __bins
        """
        bns = self._bins[numDex]
        bns.add(outcomed)
        print bns
    pass
