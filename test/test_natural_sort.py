import unittest


from src.natural_sort import natural_sort_


class TestNaturalSort(unittest.TestCase):
    def test_1(self):
        result = natural_sort_(['a3', 'a5', 'a2', 'a1', 'a4'])
        self.assertEqual(['a1', 'a2', 'a3', 'a4', 'a5'], result)

    def test_2(self):
        result = natural_sort_(['a3', 'a5', 'a2', 'a1', 'a4', 'A3', 'A5', 'A2', 'A4', 'A5'])
        self.assertEqual(['a1', 'a2', 'A2', 'a3', 'A3', 'a4', 'A4', 'a5', 'A5', 'A5'], result)

    def test_3(self):
        result = natural_sort_(['b3', 'a3', 'B3', 'A3'])
        self.assertEqual(['a3', 'A3', 'b3', 'B3'], result)
