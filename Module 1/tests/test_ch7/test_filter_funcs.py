from unittest import TestCase  # 1
from unittest.mock import patch, call  # 2
from nose.tools import assert_equal, assert_list_equal  # 3

from ch7.filter_funcs import filter_ints  # 4


class FilterIntsTestCase(TestCase):  # 5

    @patch('ch7.filter_funcs.is_positive')  # 6
    def test_filter_ints(self, is_positive_mock):  # 7
        # preparation
        v = [3, -4, 0, 5, 8]

        # execution
        filter_ints(v)  # 8

        # verification
        assert_equal(
            [call(3), call(-4), call(0), call(5), call(8)],
            is_positive_mock.call_args_list
        )  # 9

    def test_filter_ints_return_value(self):
        v = [3, -4, 0, -2, 5, 0, 8, -1]

        result = filter_ints(v)

        assert_list_equal([3, 5, 8], result)
