import unittest

class TestMyModule(unittest.TestCase):
    def test_import(self):
        self.assertIsNotNone(unittest)     

if __name__ == '__main__':
    unittest.main()