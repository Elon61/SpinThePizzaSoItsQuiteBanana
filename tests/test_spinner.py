import spinner
import unittest


class BuilderMock(object):
    def allthestuffgoesherebutnotreally(self, wheel):
        assert isinstance(wheel, spinner.Spinner)
        wheel.add_outcome(0, "outcome0")
        wheel.add_outcome(0, "outcome1")
        wheel.add_outcome(0, "outcome2")


class TestSpinner(unittest.TestCase):
    def test_add_outcome(self):
        wheel = spinner.Spinner(BuilderMock())
        for _ in xrange(spinner.Spinner.SPINNER_SIZE * 10):
            outcomes = wheel.spin()
            if outcomes:
                self.assertSetEqual(outcomes, {"outcome0", "outcome1", "outcome2"})
