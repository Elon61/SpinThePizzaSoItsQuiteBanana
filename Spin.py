class Outcome(object):
    """
    is an outcome
    """
    def __init__(self, name, odds):
        self._name = name
        self._odds = int(odds)

    def __eq__(self, other):
        """
        :param other: other object to compare
        :type other: Outcome
        :return: True if the objects are equal, else False.
        :rtype: bool
        """
        return self._name == other.__name

    def __ne__(self, other):
        """
        :param other: other object to compare
        :type other: Outcome
        :return: False if the objects are equal, else True.
        :rtype: bool
        """
        return not self.__eq__(other)

    def __hash__(self):
        """
        :return: Hash of this outcome
        :rtype: int
        """
        return hash(self._name)

    def __str__(self):
        """
        :return: Name and odds of the outcome
        :rtype: string
        """
        return "{} ({}:1)".format(self._name, self._odds)

    def __repr__(self):
        """
        :return: Name and odds of the outcome
        :rtype: string
        """
        return "Outcome({} {})".format(self._name, self._odds)

    def winAmount(self, amount):
        """
        :return: Multiply this Outcome's odds by the given amount. The product is returned.
        :rtype: int
        """
        return amount * self._odds

class Bin(frozenset):
    pass

class Wheel(object):
    def __init__(self):
        pass

    def bins(self):
        return tuple(Bin() for i in range(38))

    def rng(self):
        pass

    pass

class BinBuilder(object):
    def straight(self):
        for num in xrange(1, 37):
            Wheel().bins()[num] = Outcome(num, 35)