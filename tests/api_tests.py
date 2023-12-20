# tests/api_tests.py

import json
import unittest
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from unittest.mock import patch, MagicMock

# Import the lambda_handler from api_handler.py
from src.api.api_handler import lambda_handler

class TestAPIHandler(unittest.TestCase):
    """
    This class represents the test suite for the API handler and contains setup, teardown, and test case methods.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """
        self.event = {
            "httpMethod": "POST",
            "body": json.dumps({"test": "test"})
        }
        self.context = {}

    def tearDown(self):
        """
        Tear down method.
        """
        pass

    @patch('src.api.api_handler.lambda_client')
    def test_lambda_handler(self, mock_lambda_client):
        """
        Test the lambda_handler function.
        """
        # Mock the invoke method of the lambda client
        mock_lambda_client.invoke.return_value = {
            'StatusCode': 200,
            'Payload': json.dumps({"message": "success"})
        }

        # Call the lambda_handler function with the test event and context
        response = lambda_handler(self.event, self.context)

        # Assert that the lambda client's invoke method was called with the correct arguments
        mock_lambda_client.invoke.assert_called_with(
            FunctionName='cspm_function',
            InvocationType='RequestResponse',
            Payload=json.dumps(self.event)
        )

        # Assert that the response is as expected
        self.assertEqual(response, {"message": "success"})

    @patch('src.api.api_handler.lambda_client')
    def test_lambda_handler_error(self, mock_lambda_client):
        """
        Test the lambda_handler function when an error occurs.
        """
        # Mock the invoke method of the lambda client to raise an error
        mock_lambda_client.invoke.side_effect = ClientError(
            error_response = {'Error': {'Code': 'TestException', 'Message': 'Test exception'}},
            operation_name = 'Invoke'
        )

        # Call the lambda_handler function with the test event and context
        response = lambda_handler(self.event, self.context)

        # Assert that the response is as expected
        self.assertEqual(response, {"error": "Test exception"})

if __name__ == '__main__':
    unittest.main()
