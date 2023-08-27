import unittest
from unittest.mock import patch
import resource_api
from flask import Flask
from unittest.mock import patch, Mock


class TestResourceAPI(unittest.TestCase):
    @patch('resource_api.validate_token', return_value=False)
    def test_get_resource_access_denied(self, mock_validate_token):
        with resource_api.app.test_request_context():
            response = resource_api.get_resource()
            expected_response = ('{"message": "Access denied"}', 401)  # Correct expected format
            self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()

