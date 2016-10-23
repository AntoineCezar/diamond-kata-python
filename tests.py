import unittest
from kata import simetrize


class SymetrizeTests(unittest.TestCase):

    def test_it_return_simetrized_string_with_last_char_as_pivot(self):
        simetrized = simetrize('  a')
        self.assertEqual(simetrized, '  a  ')
