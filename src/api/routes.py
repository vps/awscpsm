# src/api/routes.py

# Import necessary modules
from http import HTTPStatus
import json
import boto3

# Initialize AWS services
lambda_client = boto3.client('lambda')

# Define the routes dictionary
routes = {
    'GET': {
        '/cspm/scan': 'CSPMFunction',
        '/cspm/report': 'CSPMReportFunction'
    },
    'POST': {
        '/cspm/scan': 'CSPMFunction'
    }
}

def route(http_method, path, event):
    """
    This function routes the incoming requests to the appropriate Lambda function.
    """
    try:
        # Check if the route exists
        if http_method in routes and path in routes[http_method]:
            # Get the function name
            function_name = routes[http_method][path]

            # Invoke the Lambda function
            response = lambda_client.invoke(
                FunctionName=function_name,
                InvocationType='RequestResponse',
                Payload=json.dumps(event)
            )

            # Parse the response from the Lambda function
            response_payload = json.loads(response['Payload'].read().decode('utf-8'))

            # Return the response
            return {
                'statusCode': HTTPStatus.OK,
                'body': json.dumps(response_payload)
            }
        else:
            # Return a 404 Not Found response if the route does not exist
            return {
                'statusCode': HTTPStatus.NOT_FOUND,
                'body': json.dumps({'error': 'Route not found'})
            }
    except Exception as e:
        # Return a 500 Internal Server Error response if an error occurs
        return {
            'statusCode': HTTPStatus.INTERNAL_SERVER_ERROR,
            'body': json.dumps({'error': str(e)})
        }
