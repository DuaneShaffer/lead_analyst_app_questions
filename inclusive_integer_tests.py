import unittest
from inclusive_integer import is_inclusive_integer

class InclusiveIntTests(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(is_inclusive_integer((10, 20), 15), True)


if __name__ == '__main__':
    unittest.main()