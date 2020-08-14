import unittest

from src.division import div

class Divisiontest(unittest.TestCase):
    def testdivision(self):
        result=div(8,2)
        self.assertEqual(4,result)
    def testdivision_by_zero(self):
        result=div(8,0)
        self.assertEqual("Infinity",result)
    def testdivision_by_float(self):
        result=div(9.8596,3.14)
        self.assertEqual(3.14,result)
    def testdivision_by_negative_numbers(self):
        result=div(8,-2)
        self.assertEqual(-4,result)

