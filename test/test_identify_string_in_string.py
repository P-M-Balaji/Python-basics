import unittest

from src.identify_string_in_string import find_string

class MyTestCase(unittest.TestCase):
    def test1(self):
        result = find_string("Hell", "Hello world")
        self.assertEqual("Exact match found", result)

    def test2(self):
        result = find_string("hell", "Hello world")
        self.assertEqual("similar match found", result)

    def test3(self):
        result = find_string("helloworld", "Hello world")
        self.assertEqual("match not found", result)

    def test4(self):
        result = find_string("llo wo", "Hello world")
        self.assertEqual("Exact match found", result)