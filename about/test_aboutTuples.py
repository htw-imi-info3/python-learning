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

    def test_tuples_are_immutable(self):
        """ 'Adding' to a tuple creates a new one """
        t = ("a", "b")
        t_id = id(t)
        t += ("c", "d")
        self.assertTupleEqual(t, ("a", "b", "c", "d"))
        self.assertNotEqual(t_id, id(t))

    def test_tuples_cant_add_to_tuples(self):
        pass

if __name__ == '__main__':
    unittest.main()
