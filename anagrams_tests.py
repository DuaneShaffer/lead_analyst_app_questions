import unittest
from anagrams import are_anagrams

class InclusiveIntTests(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(are_anagrams('inch', 'chin'), True)
        self.assertEqual(are_anagrams('brag', 'grab'), True)
        self.assertEqual(are_anagrams('agile', 'development'), False)

    def test_with_spaces(self):
        self.assertEqual(are_anagrams('dormitory', 'dirty room'), True)
        self.assertEqual(are_anagrams('a gentleman', 'elegant man'), True)

    def test_with_mixed_case(self):
        self.assertEqual(are_anagrams('Clint Eastwood', 'Old West action'), True)
        self.assertEqual(are_anagrams('Signature', 'A True Sign'), True)

    def test_null_string(self):
        self.assertEqual(are_anagrams('agile', ''), False)

    def test_null_strings(self):
        self.assertEqual(are_anagrams('', ''), True)

if __name__ == '__main__':
    unittest.main()