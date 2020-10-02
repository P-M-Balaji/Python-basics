import unittest

from src.list_of_n_elements_of_fibonacci_series import fibonacci_series

class MyTestCase(unittest.TestCase):
    def test1(self):
        result = fibonacci_series(7)
        self.assertEqual([0, 1, 1, 2, 3, 5, 8], result)

    def test2(self):
        result = fibonacci_series(10)
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], result)