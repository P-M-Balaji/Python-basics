import unittest

from src.find_length_of_a_list import list_size

class GetListLenght(unittest.TestCase):
    def test1(self):
        result = list_size([123, 2, 3, 4])
        self.assertEqual(4, result)

    def test2(self):
        result = list_size(['xy', 'yz', 'xyz',1,12,123,[1,2,3],(1,2,3)])
        self.assertEqual(8, result)