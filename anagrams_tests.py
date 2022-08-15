import unittest
from anagrams import are_anagrams

class InclusiveIntTests(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(are_anagrams('inch', 'chin'), True)
        self.assertEqual(are_anagrams('brag', 'grab'), True)
        self.assertEqual(are_anagrams('agile', 'development'), False)

    def test_with_spaces(self):
        self.assertEqual(are_anagrams('dormitory', 'dirty room'), True)

if __name__ == '__main__':
    unittest.main()