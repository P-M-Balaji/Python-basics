import unittest

from src.addition import add


class AdditionTest(unittest.TestCase):

    def test_add(self):
        result = add(1, 1)
        self.assertEqual(2, result)

    def test_string_add(self):
        result = add("bal", "aji")
        self.assertEqual("balaji", result)

    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(-2, result)

    def test_add_two_types(self):
        result = add("balaji", -1)
        self.assertEqual("Invalid action", result)
