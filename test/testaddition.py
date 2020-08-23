import unittest

from src.addition import add


class AdditionTest(unittest.TestCase):
    def testadd(self):
        result=add(1,1)
        self.assertEqual(2,result)

    def teststrinadd(self):
        result = add("bal","aji")
        self.assertEqual("balaji", result)

    def testaddnegativenumbers(self):
        result=add(-1,-1)
        self.assertEqual(-2,result)

    def testaddtwotypes(self):
        result=add("balaji",-1)
        self.assertEqual("Invalid action",result)