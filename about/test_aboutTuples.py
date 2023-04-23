import unittest

"""
- Tuples are used to store multiple items in a single variable.
- Tuple items are ordered, unchangeable, and allow duplicate values.
"""


class TestAboutTuple(unittest.TestCase):
    def test1(self):
        myTuple = ("apple", "banana", "cherry")
        length = len(myTuple)
        self.assertEqual(length, 3, "Has three Items")

    def test2(self):
        noTuple = ("apple")
        elType = type(noTuple)
        self.assertEqual(elType, str, "Missing Comma - No Tuple")

    def test3(self):
        oneTuple = ("apple",)
        elType = type(oneTuple)
        self.assertEqual(elType, tuple, "Comma present - Tuple")

    def test4(self):
        mixedTuple = ("abc", 34, True, 40, "male")
        elType = type(mixedTuple)
        self.assertEqual(elType, tuple, "Tuple")


if __name__ == '__main__':
    unittest.main()
