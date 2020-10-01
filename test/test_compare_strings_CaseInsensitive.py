import unittest

from src.compare_Strings_CaseInsensitive import compare_strings

class MyTestCase(unittest.TestCase):
    def test1(self):
        result = compare_strings("Python", "python")
        self.assertEqual("same", result)

    def test2(self):
        result = compare_strings("PYTHON", "python")
        self.assertEqual("same", result)

