#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# AWS CLI version check
if ! aws --version >/dev/null 2>&1; then
    echo "AWS CLI not found. Please install it before running this script."
    exit 1
fi

# AWS credentials check
if ! aws sts get-caller-identity >/dev/null 2>&1; then
    echo "AWS credentials not found. Please configure your AWS CLI before running this script."
    exit 1
fi

# AWS region check
if [ -z "$AWS_DEFAULT_REGION" ]; then
    echo "AWS region not set. Please set your AWS_DEFAULT_REGION environment variable before running this script."
    exit 1
fi

# Create S3 bucket for storing reports and logs
echo "Creating S3 bucket..."
aws s3api create-bucket --bucket cspm-reports --region $AWS_DEFAULT_REGION --create-bucket-configuration LocationConstraint=$AWS_DEFAULT_REGION

# Create DynamoDB table for storing metadata and configurations
echo "Creating DynamoDB table..."
aws dynamodb create-table --cli-input-json file://templates/dynamodb_schema.json

# Create the CloudFormation stack
echo "Creating CloudFormation stack..."
aws cloudformation create-stack --stack-name cspm-mvp --template-body file://templates/cloudformation.yml --capabilities CAPABILITY_NAMED_IAM

# Wait for the CloudFormation stack to be created
echo "Waiting for CloudFormation stack to be created..."
aws cloudformation wait stack-create-complete --stack-name cspm-mvp

echo "Setup completed successfully."
