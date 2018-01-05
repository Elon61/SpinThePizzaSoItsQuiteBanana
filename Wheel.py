import Bin
import Outcome
class Wheel(object):
    def __init__(self):
        self.__bins = self.bins()
        pass

    def bins(self):
        return tuple(Bin([Outcome("TESTOUTCOME", 1)]) for i in range(38))

    def rng(self):
        pass

    def addOutcome(self, numDex, outcome):
        """
        takes index in the tuple of bins. take bin at that place. add 'outcome' to that bin
        changes __bins
        """
        bns = self.__bins[numDex]
        bn = Bin(bns | {outcome})
        pn = [x for x in self.__bins]
        pn[numDex] = bn
        print pn
    pass
