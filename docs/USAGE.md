# Usage Guide for the Cloud Security Posture Management (CSPM) System

This document provides a comprehensive guide on how to use the CSPM system. The system is designed to assess and report the security posture of AWS resources.

## Prerequisites

Before you can use the CSPM system, ensure that you have:

- An AWS account with necessary permissions to create and manage resources.
- The AWS CLI installed and configured on your local machine.
- Python 3.6 or later installed on your local machine.
- The CSPM system deployed on your AWS account. Refer to the [SETUP.md](SETUP.md) guide for instructions on how to set up the system.

## Using the CSPM System

### Initiating a Security Scan

The CSPM system exposes a RESTful API endpoint for initiating a security scan. You can trigger a scan by making a POST request to the `/scan` endpoint.

Here is an example using `curl`:

```bash
curl -X POST https://<api-gateway-url>/scan -H 'x-api-key: <your-api-key>'
```

Replace `<api-gateway-url>` with the URL of your deployed API Gateway and `<your-api-key>` with your API key.

The system will return a response with a `scanId`, which you can use to retrieve the scan results later.

### Retrieving Scan Results

To retrieve the results of a security scan, make a GET request to the `/results` endpoint with the `scanId` as a query parameter.

Here is an example using `curl`:

```bash
curl -X GET 'https://<api-gateway-url>/results?scanId=<your-scan-id>' -H 'x-api-key: <your-api-key>'
```

Replace `<api-gateway-url>` with the URL of your deployed API Gateway, `<your-api-key>` with your API key, and `<your-scan-id>` with the `scanId` you received when initiating the scan.

The system will return a response with the scan results, including details of any identified security misconfigurations.

### Viewing Logs and Reports

The CSPM system stores detailed logs and reports in an Amazon S3 bucket. You can access these files directly from the S3 bucket.

To list all files in the S3 bucket, use the following AWS CLI command:

```bash
aws s3 ls s3://<your-bucket-name> --recursive
```

Replace `<your-bucket-name>` with the name of your S3 bucket.

To download a specific file, use the following AWS CLI command:

```bash
aws s3 cp s3://<your-bucket-name>/<file-path> .
```

Replace `<your-bucket-name>` with the name of your S3 bucket and `<file-path>` with the path of the file you want to download.

## Troubleshooting

If you encounter any issues while using the CSPM system, refer to the logs stored in the S3 bucket. These logs provide detailed information about the system's operations and can help you identify and resolve any problems.

For further assistance, please refer to the [API.md](API.md) for detailed API documentation and the [SETUP.md](SETUP.md) for setup instructions.
