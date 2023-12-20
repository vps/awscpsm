#!/bin/bash

# Define AWS profile
AWS_PROFILE="default"

# Define AWS region
AWS_REGION="us-east-1"

# Define S3 bucket for deployment
S3_BUCKET="cspm-deployment-bucket"

# Define CloudFormation stack name
STACK_NAME="cspm-stack"

# Define the AWS CLI command, including profile and region
AWS_CLI="aws --profile $AWS_PROFILE --region $AWS_REGION"

# Package the CloudFormation template
echo "Packaging the CloudFormation template..."
$AWS_CLI cloudformation package \
  --template-file templates/cloudformation.yml \
  --s3-bucket $S3_BUCKET \
  --output-template-file packaged-template.yml

# Deploy the CloudFormation stack
echo "Deploying the CloudFormation stack..."
$AWS_CLI cloudformation deploy \
  --template-file packaged-template.yml \
  --stack-name $STACK_NAME \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    S3BucketName=$S3_BUCKET

# Get the outputs from the CloudFormation stack
echo "Getting the outputs from the CloudFormation stack..."
STACK_OUTPUTS=$($AWS_CLI cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs")

# Extract the API Gateway URL from the stack outputs
API_GATEWAY_URL=$(echo $STACK_OUTPUTS | jq -r '.[] | select(.OutputKey=="ApiGatewayUrl") | .OutputValue')

# Print the API Gateway URL
echo "API Gateway URL: $API_GATEWAY_URL"

# Zip the Lambda function code
echo "Zipping the Lambda function code..."
zip -r lambda_code.zip src/lambda/

# Upload the Lambda function code to S3
echo "Uploading the Lambda function code to S3..."
$AWS_CLI s3 cp lambda_code.zip s3://$S3_BUCKET/

# Update the Lambda function code
echo "Updating the Lambda function code..."
$AWS_CLI lambda update-function-code \
  --function-name CSPMFunction \
  --s3-bucket $S3_BUCKET \
  --s3-key lambda_code.zip

# Delete the local Lambda function code zip file
echo "Deleting the local Lambda function code zip file..."
rm lambda_code.zip

# Delete the packaged CloudFormation template
echo "Deleting the packaged CloudFormation template..."
rm packaged-template.yml

echo "Deployment completed successfully!"
