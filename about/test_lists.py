import unittest

my_shoppinglist = []

def add_to_shoppingList(addition):
    my_shoppinglist.append(addition)


class TestList(unittest.TestCase):

    def test1(self):
        add_to_shoppingList("Pineapple")
        self.assertEqual(my_shoppinglist, ['Pineapple'], "ERROR")


if __name__ == '__main__':
    unittest.main()