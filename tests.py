import unittest
from kata import (
    diamond_letters,
    diamond_lines,
    erase_other_letters,
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
        result = erase_other_letters('b', 'abc')
        self.assertEqual(result, ' b ')
