import unittest

from src.get_first_n_elements_from_a_list import get_first_n_list_items


class MyTestCase(unittest.TestCase):
    def test_1(self):
        list_ = [1, 'xy', 'z', 4]
        result = get_first_n_list_items(list_, 2)
        self.assertEqual([1, 'xy'], result)
    
    def test_2(self):
        list_ = [1, [1, 2, 'z'], 'xyz', ('x', 'y', 3)]
        result = get_first_n_list_items(list_, 1)
        self.assertEqual([1], result)

    def test_3(self):
        list_ = [1.5, -18, 'xyz', 'a', 'b', 'c', {1, 2, 'x'}]
        result = get_first_n_list_items(list_, 4)
        self.assertEqual([1.5, -18, 'xyz', 'a'], result)
