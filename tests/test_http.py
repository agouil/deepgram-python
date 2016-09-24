import unittest

from deepgram.http import Http
from requests import Response, HTTPError
from test_data import response_success, response_invalid, response_xml


class TestHttp(unittest.TestCase):

    def setUp(self):
        self.http = Http("http://example.com")

    def tearDown(self):
        self.http = None

    def test_get_request_url(self):
        result = "http://example.com/test"
        self.assertEqual(
            self.http._get_request_url('/test'), result)

    def test_parse_response_success(self):
        response = Response()
        response._content = response_success
        response.status_code = 200

        result = {
            "foo": "bar"
        }
        self.assertEqual(
            self.http._parse_response(response), result)

    def test_parse_response_invalid(self):
        response = Response()
        response._content = response_invalid
        response.status_code = 200

        with self.assertRaises(ValueError):
            self.http._parse_response(response)

    def test_parse_response_other_format(self):
        response = Response()
        response._content = response_xml
        response.status_code = 200

        result = response_xml
        self.assertEqual(
            self.http._parse_response(response, format="xml"), result)

    def test_parse_response_invalid_return_code(self):
        response = Response()
        response.status_code = 500

        with self.assertRaises(HTTPError):
            self.http._parse_response(response)
