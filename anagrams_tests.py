import unittest
from anagrams import are_anagrams

class InclusiveIntTests(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(are_anagrams('dormitory', 'dirty room'), True)
        self.assertEqual(are_anagrams('agile', 'development'), False)

if __name__ == '__main__':
    unittest.main()