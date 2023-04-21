import unittest

myTuple = ("apple", "banana", "cherry")
noTuple = ("apple")
oneTuple = ("apple", )
mixedTuple = ("abc", 34, True, 40, "male")

"""
- Tuples are used to store multiple items in a single variable.
- Tuple items are ordered, unchangeable, and allow duplicate values.
"""

class testAboutTuple(unittest.TestCase):
    def test1(self):
        length = len(myTuple)
        self.assertEqual(length, 3, "Has three Items")

    def test2(self):
        elType = type(noTuple)
        self.assertEqual(elType, str, "Missing Comma - No Tuple")

    def test3(self):
        elType = type(oneTuple)
        self.assertEqual(elType, tuple, "Comma present - Tuple")

    def test4(self):
        elType = type(mixedTuple)
        self.assertEqual(elType, tuple, "Tuple")



if __name__ == '__main__':
    unittest.main()