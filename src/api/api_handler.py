import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from routes import route

# Initialize AWS services
lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    """
    This function handles the incoming requests from the API Gateway and routes them to the appropriate Lambda function.
    """
    try:
        # Extract the HTTP method and path parameters from the event
        http_method = event['httpMethod']
        path = event['path']

        # Route the request to the appropriate function
        function_name, payload = route(http_method, path, event)

        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )

        # Parse the response from the Lambda function
        response_payload = json.loads(response['Payload'].read().decode('utf-8'))

        # Return the response to the API Gateway
        return {
            'statusCode': 200,
            'body': json.dumps(response_payload),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    except (BotoCoreError, ClientError) as error:
        # Log the error and return an error response
        print(f"An error occurred: {error}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
