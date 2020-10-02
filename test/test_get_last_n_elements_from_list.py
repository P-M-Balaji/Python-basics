import  unittest

from src.get_last_n_elements_from_list import get_last_n_list_items
from src.appending_list import append_list

class MyTestCase(unittest.TestCase):
    def test_1(self):
        list_ = [1, 'xy', 'z', 4]
        result = get_last_n_list_items(list_, 2)
        self.assertEqual(['z', 4], result)

    def test_2(self):
        list_ = [1, [1, 2, 'z'], 'xyz', ('x', 'y', 3)]
        result = get_last_n_list_items(list_, 1)
        self.assertEqual([('x', 'y', 3)], result)

    def test_3(self):
        list_ = [1.5, -18, 'xyz', 'a', 'b', 'c', {1, 2, 'x'}]
        result = get_last_n_list_items(list_, 4)
        self.assertEqual(['a', 'b', 'c', {1, 2, 'x'}], result)

