import unittest

from src.compare_strings import compare_strings


class MyTestCase(unittest.TestCase):
    def test_stringSet1(self):
        result = compare_strings("python", "python")
        self.assertEqual("same", result)

    def test_stringSet2(self):
        result = compare_strings("Python", "python")
        self.assertEqual("different", result)

    def test_stringSet3(self):
        result = compare_strings("10", "100")
        self.assertEqual("different", result)

    def test_stringSet4(self):
        result = compare_strings("-10", "-10")
        self.assertEqual("same", result)


if __name__ == '__main__':
    unittest.main()
