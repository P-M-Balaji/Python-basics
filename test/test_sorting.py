import unittest

from src.sorting import sort


class TestSorting(unittest.TestCase):

    def test_1(self):
        result = sort([5, 2, 3, 6, 4, 0, 1])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], result)

    def test_2(self):
        result = sort([-5, -2, -3, -6, -4, -1])
        self.assertEqual([-6, -5, -4, -3, -2, -1], result)

    def test_3(self):
        result = sort([-5.123, -5.312, 3.5, 22/7, 3.51, 0])
        self.assertEqual([-5.312, -5.123, 0, 3.142857142857143, 3.5, 3.51], result)
