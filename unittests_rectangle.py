import unittest
class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_area_mul(self):
       res = area(10, 20)
       self.assertEqual(res, 200)

   def test_perimeter(self):
       res = area(30, 5)
       self.assertEqual(res, 70)
