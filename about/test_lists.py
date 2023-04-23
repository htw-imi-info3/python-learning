import unittest

my_shoppinglist = []


def add_to_shoppinglist(addition):
    my_shoppinglist.append(addition)


class TestList(unittest.TestCase):

    def setUp(self):
        my_shoppinglist.clear()

    def test_append(self):
        add_to_shoppinglist('Pineapple')
        self.assertEqual(my_shoppinglist, ['Pineapple'], 'ERROR')


if __name__ == '__main__':
    unittest.main()
