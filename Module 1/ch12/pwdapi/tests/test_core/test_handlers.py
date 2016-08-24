# -*- coding: utf-8 -*-
import json
from unittest.mock import patch

from nose.tools import assert_dict_equal, assert_equal

import falcon
import falcon.testing as testing

from core.handlers import (
    PasswordValidatorHandler, PasswordGeneratorHandler)


class PGHTest(PasswordGeneratorHandler):
    def process_request(self, req, resp):
        self.req, self.resp = req, resp
        return super(PGHTest, self).process_request(req, resp)


class PVHTest(PasswordValidatorHandler):
    def process_request(self, req, resp):
        self.req, self.resp = req, resp
        return super(PVHTest, self).process_request(req, resp)


class TestPasswordValidatorHandler(testing.TestBase):

    def before(self):
        self.resource = PVHTest()
        self.api.add_route('/password/validate/', self.resource)

    def test_post(self):
        self.simulate_request(
            '/password/validate/',
            body=json.dumps({'password': 'abcABC0123#&'}),
            method='POST')
        resp = self.resource.resp

        assert_equal('200 OK', resp.status)
        assert_dict_equal(
            {'password': 'abcABC0123#&',
             'score': {'case': 3, 'length': 5, 'numbers': 2,
                'special': 4, 'ratio': 2, 'total': 16},
             'valid': True},
             json.loads(resp.body))

    def test_post_empty_body(self):
        self.simulate_request(
            '/password/validate/',
            method='POST')
        assert_equal('400 Bad Request', self.srmock.status)

    def test_post_malformed_json(self):
        self.simulate_request(
            '/password/validate/',
            body='a',
            method='POST')
        assert_equal('753 Syntax Error', self.srmock.status)


class TestPasswordGeneratorHandler(testing.TestBase):

    def before(self):
        self.resource = PGHTest()
        self.api.add_route('/password/generate/', self.resource)

    @patch('core.handlers.PasswordGenerator')
    def test_get(self, PasswordGenerator):
        PasswordGenerator.generate.return_value = (7, 'abc123')
        self.simulate_request(
            '/password/generate/',
            query_string='length=7',
            method='GET')
        resp = self.resource.resp

        assert_equal('200 OK', resp.status)
        assert_equal([7, 'abc123'], json.loads(resp.body))

    def test_get_no_length(self):
        self.simulate_request(
            '/password/generate/', method='GET')
        resp = self.resource.resp

        assert_equal('200 OK', resp.status)
        # default length when not provided
        assert_equal(16, len(json.loads(resp.body)[1]))

    def test_get_length(self):
        self.simulate_request(
            '/password/generate/',
            query_string='length=42',
            method='GET')
        resp = self.resource.resp

        assert_equal('200 OK', resp.status)
        assert_equal(42, len(json.loads(resp.body)[1]))

    def test_get_length_not_int(self):
        self.simulate_request(
            '/password/generate/',
            query_string='length=not-an-int',
            method='GET')
        resp = self.resource.resp

        assert_equal('400 Bad Request', resp.status)

    def test_get_length_integer_not_positive(self):
        self.simulate_request(
            '/password/generate/',
            query_string='length=-42',
            method='GET')
        resp = self.resource.resp

        assert_equal('400 Bad Request', resp.status)
