# CSPM System Setup Guide

This document provides a step-by-step guide to setting up the Cloud Security Posture Management (CSPM) system on your AWS environment.

## Prerequisites

- AWS Account with necessary permissions to create and manage resources.
- AWS CLI installed and configured with your AWS credentials.
- Python 3.6 or later installed.
- Git installed.

## Steps

1. **Clone the Repository**

   Clone the `aws-cspm-mvp` repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/aws-cspm-mvp.git
   cd aws-cspm-mvp
   ```

2. **Install Python Dependencies**

   Install the required Python dependencies listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Setup Script**

   Run the `setup.sh` script located in the `scripts/` directory. This script will create the necessary AWS resources such as the S3 bucket, DynamoDB table, and Lambda function.

   ```bash
   chmod +x scripts/setup.sh
   ./scripts/setup.sh
   ```

   The script will prompt you to enter your AWS region and the name for the S3 bucket and DynamoDB table. Make sure to choose unique names for your resources.

4. **Deploy the Application**

   Run the `deploy.sh` script located in the `scripts/` directory. This script will package your Lambda function code, upload it to S3, and update the Lambda function code.

   ```bash
   chmod +x scripts/deploy.sh
   ./scripts/deploy.sh
   ```

   The script will prompt you to enter the name of the S3 bucket where the Lambda function code will be uploaded.

5. **Verify the Setup**

   At this point, your CSPM system should be up and running. You can verify the setup by invoking the Lambda function manually or through the API Gateway.

   To invoke the Lambda function manually, use the following AWS CLI command:

   ```bash
   aws lambda invoke --function-name cspm_function --payload '{}' response.json
   ```

   This will trigger a CSPM scan and the results will be stored in the specified S3 bucket.

## Next Steps

After the setup, you can start using the CSPM system. Refer to the `USAGE.md` document for instructions on how to use the system and the `API.md` document for details on the API endpoints.

## Troubleshooting

If you encounter any issues during the setup, refer to the AWS CloudFormation events and the Lambda function logs in CloudWatch for debugging information.

## Cleanup

To delete the CSPM system and all associated resources, you can delete the CloudFormation stack that was created during the setup.

```bash
aws cloudformation delete-stack --stack-name cspm-stack
```