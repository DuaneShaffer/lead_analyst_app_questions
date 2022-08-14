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

    def test_impossible_range(self):
        with self.assertRaises(ValueError):
            is_inclusive_integer((20, 10), 15),

    def test_impossible_range_2(self):
        with self.assertRaises(ValueError):
            is_inclusive_integer((20, 10), 20)

if __name__ == '__main__':
    unittest.main()