import bin_stuff
import spinner
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

    def win_amount(self, amount):
        """
        :return: Multiply this Outcome's odds by the given amount. The product is returned.
        :rtype: int
        """
        return amount * self._odds

    def lose_amount(self, amount):
        """
        :return: Multiply this Outcome's odds by the given amount. The product is returned.
        :rtype: int
        """
        return amount

    def builder(self, outcome_value): #makes an outcome out of the representative string of the outcome, checks for validity on my unfinished generator; is there any way not to recreate a generator every time?
        """
        :param outcome_value:
        :type outcome_value: str
        :return:
        """
        t_outcome = Outcome(outcome_value, 35 / (len(outcome_value.split("-"))))
        spin = spinner.Spinner() # less cool
        if t_outcome in spin._bin():
            return t_outcome
        return Outcome("10", 35)
