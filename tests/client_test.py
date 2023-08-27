import unittest
from unittest.mock import patch, Mock, call
import client

class TestClient(unittest.TestCase):
    @patch('client.requests.get')
    def test_main(self, mock_get):
        mock_response_authorization = Mock()
        mock_response_authorization.json.return_value = {'token': 'test-token'}
        mock_response_authorization.status_code = 200

        mock_response_resource = Mock()
        mock_response_resource.status_code = 200
        mock_response_resource.text = '{"message": "Access granted to the resource"}'  # Set the response content

        mock_get.side_effect = [mock_response_authorization, mock_response_resource]

        with patch('builtins.print') as mock_print:
            client.main()

        mock_get.assert_has_calls([
            call(client.AUTHORIZATION_SERVER_URL),
            call(client.RESOURCE_API_URL, headers={'Authorization': 'Bearer test-token'})
        ])
        mock_print.assert_called_once_with('Resource API response:', mock_response_resource.text)

if __name__ == '__main__':
    unittest.main()


