import unittest

from src.reverse_list import reverse_list
from src.appending_list import append_list


class MyTestCase(unittest.TestCase):
    def test1(self):
        result = reverse_list([-1, 'yx', 'xy', -4.4])
        self.assertEqual([-4.4, 'xy', 'yx', -1], result)

    def test2(self):
        result = reverse_list([[1, 2, 3], {1, 2}, (1, 'x', 3.3)])
        self.assertEqual([(1, 'x', 3.3), {1, 2}, [1, 2, 3]], result)