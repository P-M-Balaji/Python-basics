import unittest

from src.reverse_a_string import string_reverse


class MyTestcase(unittest.TestCase):
    def test_string1(self):
        result = string_reverse("cafe")
        self.assertEqual("efac", result)

    def test_string2(self):
        result = string_reverse("race car")
        self.assertEqual("rac ecar", result)

    def test_string3(self):
        result = string_reverse("1234")
        self.assertEqual("4321", result)
