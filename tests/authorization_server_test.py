import unittest
from unittest.mock import patch
import authorization_server
from flask import Flask
from unittest.mock import patch, Mock

class TestAuthorizationServer(unittest.TestCase):
    @patch('authorization_server.generate_random_token', return_value='test-token')
    @patch('authorization_server.jsonify')  # Mock the jsonify function
    def test_get_token(self, mock_jsonify, mock_generate_token):
        with authorization_server.app.test_request_context():
            mock_jsonify.return_value = {'token': 'test-token'}
            response = authorization_server.get_token()
            expected_response = {'token': 'test-token'}
            self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()

