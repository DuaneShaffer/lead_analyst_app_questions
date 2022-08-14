import unittest
from inclusive_integer import is_inclusive_integer

class InclusiveIntTests(unittest.TestCase):

    def test_basic_true(self):
        self.assertEqual(is_inclusive_integer((10, 20), 15), True)

    def test_edge_case_lower(self):
        self.assertEqual(is_inclusive_integer((10, 20), 10), True)

    def test_edge_case_upper(self):
        self.assertEqual(is_inclusive_integer((10, 20), 20), True)

    def test_basic_false(self):
        self.assertEqual(is_inclusive_integer((10, 20), 0), False)

if __name__ == '__main__':
    unittest.main()