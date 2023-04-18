import unittest

class AboutInterning(unittest.TestCase):
    """
    Python interns values for optimization.
    I could not find an example where numbers were not interned;
    switched to show interning with lists (mutable) and tuples (immutable)
    instead and indeed, tuples seem to be interned.
    Note that this is implementation dependent.
    """
    def test_small_number(self):
        n1 = 3 + 4
        n2 = 4 + 3
        self.assertEqual(True, n1 == n2)
        self.assertEqual(True, n1 is n2)

    def test_larger_number(self):
        n1 = 982345892738958973245789235789789235789278934987234 + 42
        n2 = 42 + 982345892738958973245789235789789235789278934987234
        self.assertEqual(True, n1 == n2, "equal")
        self.assertEqual(True, n1 is n2, "still interned - but implementation dependent!")
        self.assertEqual(True, id(n1) == id(n2), "object ids are the same")

    def test_list(self):
        n1 = [1, 2, 3]
        n2 = [1, 2, 3]
        self.assertEqual(True, n1 == n2, "equal")
        self.assertEqual(False, n1 is n2, "Lists are mutable and thus cannot be interned!")
        print(id(n1))
        print(id(n2))
    def create_tuple(self):
        return (1, 2, 3)
    def test_tuple(self):
        n1 = (1, 2, 3)
        n2 = self.create_tuple()

        self.assertEqual(True, n1 == n2, "equal")
        self.assertEqual(True, n1 is n2, "identity - tuples with same literal")

        n3 = tuple([1, 2, 3])
        self.assertEqual(True, n1 == n3, "equal")
        self.assertEqual(False, n1 is n3, "identity - no interning if one is created from a list.")

    def test_tuple_is_immutable(self):
        n1 = (1, 2, 3)
        n2 = (4, 5, 6)
        # as tuples are immutable, they don't have mutator methods.
        # found a private __add__ method:
        n3 = n1.__add__(n2)
        self.assertEqual((1, 2, 3), n1)
        self.assertEqual((1, 2, 3, 4, 5, 6), n3)


if __name__ == '__main__':
    unittest.main()
