import unittest

from src.appending_list import append_list


class TestAppending(unittest.TestCase):

    def test1(self):
        result = append_list()
        self.assertEqual([1, -2, 3, -4], result)

    def test2(self):
        result = append_list()
        self.assertEqual(['ab', 'cd', 'ef', 'gh'], result)

    def test3(self):
        result = append_list()
        self.assertEqual([5.5, 1, 'xyz'], result)
