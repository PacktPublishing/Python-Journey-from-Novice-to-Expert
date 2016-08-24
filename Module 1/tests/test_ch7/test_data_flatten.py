from unittest import TestCase
from nose.tools import assert_equal

from ch7.data_flatten import flatten


class FlattenTestCase(TestCase):

    def test_flatten(self):
        test_cases = [
            ({'A': {'B': 'C', 'D': [1, 2, 3], 'E': {'F': 'G'}},
              'H': 3.14,
              'J': ['K', 'L'],
              'M': 'N'},
             {'A.B': 'C',
              'A.D': [1, 2, 3],
              'A.E.F': 'G',
              'H': 3.14,
              'J': ['K', 'L'],
              'M': 'N'}),
            (0, 0),
            ('Hello', 'Hello'),
            ({'A': None}, {'A': None}),
        ]
        for (nested, flat) in test_cases:
            assert_equal(flat, flatten(nested))

    def test_flatten_custom_separator(self):
        nested = {'A': {'B': {'C': 'D'}}}

        assert_equal(
            {'A#B#C': 'D'}, flatten(nested, separator='#'))
