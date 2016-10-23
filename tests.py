import unittest
from kata import (
    diamond_letters,
    diamond_lines,
    erease,
    erease_other_letters,
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


class EreaseTests(unittest.TestCase):

    def test_it_replace_single_letter_by_space(self):
        result = erease('b', 'abc')
        self.assertEqual(result, 'a c')

    def test_it_replace_multiple_letters_by_spaces(self):
        result = erease('bc', 'abc')
        self.assertEqual(result, 'a  ')

    def test_it_replace_multiple_separated_letters_by_spaces(self):
        result = erease('ac', 'abc')
        self.assertEqual(result, ' b ')


class DiamondLinesTests(unittest.TestCase):

    def test_a_diamond(self):
        result = diamond_lines('a')
        self.assertEqual(result, ['a'])

    def test_b_diamond(self):
        result = diamond_lines('b')
        self.assertEqual(result, [
            ' a ',
            'b b',
            ' a ',
        ])


class EreaseOtherLettersTests(unittest.TestCase):

    def test_it_replace_other_letters_by_spaces(self):
        result = erease_other_letters('b', 'abc')
        self.assertEqual(result, ' b ')
