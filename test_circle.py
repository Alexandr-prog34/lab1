import unittest as t
from circle import area
from circle import perimeter
from math import pi


class CircleTestCase(t.TestCase):
    def test_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negativeR(self):
        res = area(-3)
        self.assertEqual(res, ValueError)

    def test_negativeR_error(self):
        with self.assertRaises(ValueError):
            area(-3)

    def test_floatPi(self):
        res = area(1/pi)
        self.assertAlmostEqual(res, 0.32, 2)

    def test_negative(self):
        res = perimeter(-pi)
        self.assertEqual(res, ValueError)

    def test_negative_error(self):
        with self.assertRaises(ValueError):
            area(-pi)

    def test_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_float(self):
        res = perimeter(9.5)
        self.assertAlmostEqual(res, 59.69, 2)
