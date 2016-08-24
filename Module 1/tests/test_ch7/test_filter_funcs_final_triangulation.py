from unittest import TestCase, expectedFailure
from nose.tools import assert_list_equal

from ch7.filter_funcs_triangulation import filter_ints


class FilterIntsTestCase(TestCase):

    @expectedFailure
    def test_filter_ints_return_value(self):
        v1 = [3, -4, 0, -2, 5, 0, 8, -1]
        v2 = [7, -3, 0, 0, 9, 1]

        assert_list_equal([3, 5, 8], filter_ints(v1))
        assert_list_equal([7, 9, 1], filter_ints(v2))
