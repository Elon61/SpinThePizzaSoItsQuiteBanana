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
        return self._name == other._name

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
        :rtype: str
        """
        return "{} ({}:1)".format(self._name, self._odds)

    def __repr__(self):
        """
        :return: Name and odds of the outcome
        :rtype: str
        """
        return "Outcome({!r} {})".format(self._name, self._odds)

    def winAmount(self, amount):
        """
        :return: Multiply this Outcome's odds by the given amount. The product is returned.
        :rtype: int
        """
        return amount * self._odds

    def loseAmount(self, amount):
        """
        :return: Multiply this Outcome's odds by the given amount. The product is returned.
        :rtype: int
        """
        return amount
