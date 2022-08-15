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

    def test_large_text(self):
        lorem_ipsum_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        lorem_ip_tweaked = 'ipsum Lorem dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        self.assertEqual(are_anagrams(lorem_ipsum_text, lorem_ip_tweaked), True)
        self.assertEqual(are_anagrams(lorem_ipsum_text, lorem_ipsum_text[:-1]), False)
if __name__ == '__main__':
    unittest.main()