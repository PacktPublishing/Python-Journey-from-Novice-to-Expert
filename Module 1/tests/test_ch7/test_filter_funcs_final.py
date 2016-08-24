from unittest import TestCase
from nose.tools import assert_list_equal

from ch7.filter_funcs import filter_ints


class FilterIntsTestCase(TestCase):

    def test_filter_ints_return_value(self):
        v = [3, -4, 0, -2, 5, 0, 8, -1]
        result = filter_ints(v)
        assert_list_equal([3, 5, 8], result)
