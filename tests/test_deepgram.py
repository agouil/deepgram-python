import unittest

from deepgram import Deepgram
from mock import patch
from test_data import response_dict_success, response_dict_invalid


class TestDeepgram(unittest.TestCase):

    def setUp(self):
        self.dg = Deepgram('test_api_key')
        self.request_data = {
            "action": "get_balance",
            "userID": "123-abc-456-def"
        }

    def tearDown(self):
        self.dg = None
        self.request_data = None

    @patch('deepgram.http.Http.post')
    def test_make_request_success(self, mock_post):
        mock_post.return_value = response_dict_success

        result = {
            "balance": 123,
            "userID": "123-abc-456-def"
        }
        self.assertEqual(
            self.dg._make_request(self.request_data), result)

    @patch('deepgram.http.Http.post')
    def test_make_request_invalid_response(self, mock_post):
        mock_post.return_value = response_dict_invalid

        result = {
            "error": "invalid contentID / userID"
        }
        self.assertEqual(
            self.dg._make_request(self.request_data), result)

    @patch('deepgram.http.Http.post')
    def test_makek_request_error(self, mock_post):
        mock_post.side_effect = ValueError('No JSON object could be decoded')

        with self.assertRaises(ValueError):
            self.dg._make_request(self.request_data)
