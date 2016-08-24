# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import patch

from nose_parameterized import parameterized, param
from nose.tools import (
    assert_equal, assert_dict_equal, assert_true)

from core.passwords import PasswordValidator, PasswordGenerator


class PasswordValidatorTestCase(TestCase):

    @parameterized.expand([
        (False, ''),
        (False, '  '),
        (True, 'abcdefghijklmnopqrstuvwxyz'),
        (True, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        (True, '0123456789'),
        (True, '!#$%&()*+-?@_|'),
    ])
    def test_is_valid(self, valid, password):
        validator = PasswordValidator(password)
        assert_equal(valid, validator.is_valid())

    @parameterized.expand(
        param.explicit(char) for char in '>]{<`\\;,[^/"\'~:}=.'
    )
    def test_is_valid_invalid_chars(self, password):
        validator = PasswordValidator(password)
        assert_equal(False, validator.is_valid())

    @parameterized.expand([
        (0, ''),  # 0-3: score 0
        (0, 'a'),  # 0-3: score 0
        (0, 'aa'),  # 0-3: score 0
        (0, 'aaa'),  # 0-3: score 0
        (1, 'aaab'),  # 4-7: score 1
        (1, 'aaabb'),  # 4-7: score 1
        (1, 'aaabbb'),  # 4-7: score 1
        (1, 'aaabbbb'),  # 4-7: score 1
        (3, 'aaabbbbc'),  # 8-11: score 3
        (3, 'aaabbbbcc'),  # 8-11: score 3
        (3, 'aaabbbbccc'),  # 8-11: score 3
        (3, 'aaabbbbcccc'),  # 8-11: score 3
        (5, 'aaabbbbccccd'),  # 12-15: score 5
        (5, 'aaabbbbccccdd'),  # 12-15: score 5
        (5, 'aaabbbbccccddd'),  # 12-15: score 5
        (5, 'aaabbbbccccdddd'),  # 12-15: score 5
    ])
    def test__score_length(self, score, password):
        validator = PasswordValidator(password)
        assert_equal(score, validator._score_length())

    def test__score_length_sixteen_plus(self):
        # all password whose length is 16+ score 7 points
        password = 'x' * 255
        for length in range(16, len(password)):
            validator = PasswordValidator(password[:length])
            assert_equal(7, validator._score_length())

    @parameterized.expand([
        (0, '0123456789!#$%&()*+-?@_|'),
        (1, 'abc'),
        (1, 'ABC'),
        (3, 'aA'),
    ])
    def test__score_case(self, score, password):
        validator = PasswordValidator(password)
        assert_equal(score, validator._score_case())

    @parameterized.expand(
        param.explicit(char) for char in '0123456789'
    )
    def test__score_numbers(self, password):
        validator = PasswordValidator(password)
        assert_equal(2, validator._score_numbers())

    @parameterized.expand([
        ('abcdefghijklmnopqrstuvwxyz'),
        ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        ('!#$%&()*+-?@_|'),
    ])
    def test__score_numbers_no_numbers(self, password):
        validator = PasswordValidator(password)
        assert_equal(0, validator._score_numbers())

    @parameterized.expand(
        param.explicit(char) for char in '!#$%&()*+-?@_|'
    )
    def test__score_special(self, password):
        validator = PasswordValidator(password)
        assert_equal(4, validator._score_special())

    @parameterized.expand([
        ('abcdefghijklmnopqrstuvwxyz'),
        ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        ('0123456789'),
    ])
    def test__score_special_no_special(self, password):
        validator = PasswordValidator(password)
        assert_equal(0, validator._score_special())

    @parameterized.expand([
        (0, 'abcdef'),  # 6:0 = 0 (6 chars, 0 digits)
        (1, 'a0'),  # 1:1 = 1
        (3, 'abc1'),  # 3:1 = 3
        (1, 'a123'),  # 1:3 = 1
        (7, 'abcdefg1'),  # 7:1 = 7
        (7, 'aaaaaaa1'),  # 7:1 = 7 (repeated characters)
        (7, 'abcdefgh1'),  # 8:1 = 7 (limitation)
    ])
    def test__score_ratio(self, score, password):
        validator = PasswordValidator(password)
        assert_equal(score, validator._score_ratio())

    @patch.object(PasswordValidator, '_score_length')
    @patch.object(PasswordValidator, '_score_case')
    @patch.object(PasswordValidator, '_score_numbers')
    @patch.object(PasswordValidator, '_score_special')
    @patch.object(PasswordValidator, '_score_ratio')
    def test_score(
            self,
            _score_ratio_mock,
            _score_special_mock,
            _score_numbers_mock,
            _score_case_mock,
            _score_length_mock):

        _score_ratio_mock.return_value = 2
        _score_special_mock.return_value = 3
        _score_numbers_mock.return_value = 5
        _score_case_mock.return_value = 7
        _score_length_mock.return_value = 11

        expected_result = {
            'length': 11,
            'case': 7,
            'numbers': 5,
            'special': 3,
            'ratio': 2,
            'total': 28,
        }

        validator = PasswordValidator('')

        assert_dict_equal(expected_result, validator.score())


class PasswordGeneratorTestCase(TestCase):

    def test__generate_password_length(self):
        for length in range(300):
            assert_equal(
                length,
                len(PasswordGenerator._generate_password(length))
            )

    def test__generate_password_validity(self):
        for length in range(1, 300):
            password = PasswordGenerator._generate_password(
                length)
            assert_true(PasswordValidator(password).is_valid())

    def test__generate_candidate(self):
        score, password = (
            PasswordGenerator._generate_candidate(42))
        expected_score = PasswordValidator(password).score()
        assert_equal(expected_score['total'], score)

    @patch.object(PasswordGenerator, '_generate_candidate')
    def test__generate(self, _generate_candidate_mock):
        # checks `generate` returns the highest score candidate
        _generate_candidate_mock.side_effect = [
            (16, '&a69Ly+0H4jZ'),
            (17, 'UXaF4stRfdlh'),
            (21, 'aB4Ge_KdTgwR'),  # the winner
            (12, 'IRLT*XEfcglm'),
            (16, '$P92-WZ5+DnG'),
            (18, 'Xi#36jcKA_qQ'),
            (19, '?p9avQzRMIK0'),
            (17, '4@sY&bQ9*H!+'),
            (12, 'Cx-QAYXG_Ejq'),
            (18, 'C)RAV(HP7j9n'),
        ]
        assert_equal(
            (21, 'aB4Ge_KdTgwR'), PasswordGenerator.generate(12))
