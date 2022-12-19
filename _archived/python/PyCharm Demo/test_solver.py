from unittest import TestCase
from Solver import  Solver


class TestSolver(TestCase):
    def test_negative_discr(self):
        s = Solver
        self.assertRaises(Exception, s.calc_discr, 2, 1, 2)

    def test_calc_discr(self):
        self.fail()
