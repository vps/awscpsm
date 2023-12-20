import unittest
import boto3
import json
from unittest.mock import patch, MagicMock
from botocore.exceptions import BotoCoreError, ClientError

# Import the lambda function
from src.lambda.cspm_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def setUp(self):
        self.event = {
            "detail": {
                "requestParameters": {
                    "bucketName": "test-bucket"
                }
            }
        }
        self.context = {}

    @patch('boto3.client')
    def test_lambda_handler_success(self, mock_client):
        # Mock the boto3 client
        mock_s3 = MagicMock()
        mock_ec2 = MagicMock()
        mock_iam = MagicMock()

        # Set the return value for the boto3 client
        mock_client.return_value = mock_s3
        mock_client.return_value = mock_ec2
        mock_client.return_value = mock_iam

        # Call the lambda handler
        response = lambda_handler(self.event, self.context)

        # Assert the response
        self.assertEqual(response, {
            'statusCode': 200,
            'body': json.dumps('CSPM scan completed successfully.')
        })

    @patch('boto3.client')
    def test_lambda_handler_failure(self, mock_client):
        # Mock the boto3 client
        mock_s3 = MagicMock()
        mock_ec2 = MagicMock()
        mock_iam = MagicMock()

        # Set the return value for the boto3 client
        mock_client.return_value = mock_s3
        mock_client.return_value = mock_ec2
        mock_client.return_value = mock_iam

        # Set the side effect for the boto3 client
        mock_s3.get_bucket_acl.side_effect = BotoCoreError
        mock_ec2.describe_instances.side_effect = BotoCoreError
        mock_iam.list_policies.side_effect = BotoCoreError

        # Call the lambda handler
        response = lambda_handler(self.event, self.context)

        # Assert the response
        self.assertEqual(response, {
            'statusCode': 500,
            'body': json.dumps('An error occurred during the CSPM scan.')
        })

if __name__ == '__main__':
    unittest.main()

