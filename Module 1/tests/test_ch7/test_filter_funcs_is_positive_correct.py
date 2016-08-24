from unittest import TestCase
from nose.tools import assert_equal, assert_list_equal

from ch7.filter_funcs import (
    filter_ints, is_positive
)


class FilterIntsTestCase(TestCase):

    def test_filter_ints_return_value(self):
        v1 = [3, -4, 0, -2, 5, 0, 8, -1]
        v2 = [7, -3, 0, 0, 9, 1]

        assert_list_equal([3, 5, 8], filter_ints(v1))
        assert_list_equal([7, 9, 1], filter_ints(v2))

    def test_is_positive(self):
        assert_equal(False, is_positive(-1))
        assert_equal(False, is_positive(0))
        assert_equal(True, is_positive(1))
