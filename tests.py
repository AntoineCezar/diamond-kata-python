import unittest
from kata import mirror


class MirrorTests(unittest.TestCase):

    def test_it_return_mirrored_string_with_last_char_as_pivot(self):
        mirrored = mirror('  a')
        self.assertEqual(mirrored, '  a  ')
