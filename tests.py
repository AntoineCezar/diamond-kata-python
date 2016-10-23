import unittest
from kata import (
    diamond_letters,
    erease,
    mirror,
)


class MirrorTests(unittest.TestCase):

    def test_it_return_mirrored_string_with_last_char_as_pivot(self):
        mirrored = mirror('  a')
        self.assertEqual(mirrored, '  a  ')


class DiamondLettersTests(unittest.TestCase):

    def test_a_gives_a(self):
        result = diamond_letters('a')
        self.assertEqual(result, 'a')

    def test_c_gives_abc(self):
        result = diamond_letters('c')
        self.assertEqual(result, 'abc')


class EreaseTest(unittest.TestCase):

    def test_it_replace_single_letter_by_space(self):
        result = erease('b', 'abc')
        self.assertEqual(result, 'a c')

    def test_it_replace_multiple_letters_by_spaces(self):
        result = erease('bc', 'abc')
        self.assertEqual(result, 'a  ')

    def test_it_replace_multiple_separated_letters_by_spaces(self):
        result = erease('ac', 'abc')
        self.assertEqual(result, ' b ')
