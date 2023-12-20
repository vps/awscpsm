# API Documentation

This document provides detailed information about the RESTful API endpoints exposed by the Cloud Security Posture Management (CSPM) system. The API is orchestrated via AWS API Gateway and allows users to interact with the system, initiate scans, and retrieve results.

## Base URL

The base URL for all API requests is:

```
https://<api-id>.execute-api.<region>.amazonaws.com/prod
```

Replace `<api-id>` with your API Gateway ID and `<region>` with the AWS region where your API is deployed.

## Endpoints

### 1. Initiate Scan

- **URL**: `/scan`
- **Method**: `POST`
- **Description**: Initiates a CSPM scan on the specified AWS resources.
- **Request Body**:

```json
{
    "resources": ["ec2", "s3", "iam"]
}
```

- **Response**:

```json
{
    "message": "Scan initiated successfully.",
    "scan_id": "<scan_id>"
}
```

### 2. Get Scan Results

- **URL**: `/scan/<scan_id>`
- **Method**: `GET`
- **Description**: Retrieves the results of a completed CSPM scan.
- **Response**:

```json
{
    "scan_id": "<scan_id>",
    "status": "completed",
    "results": {
        "ec2": {
            "total": 10,
            "issues": 2
        },
        "s3": {
            "total": 5,
            "issues": 1
        },
        "iam": {
            "total": 3,
            "issues": 0
        }
    }
}
```

## Error Handling

In case of an error, the API will return a response with an HTTP status code of 400 or above, along with a JSON object containing an error message. For example:

```json
{
    "error": "Invalid scan_id provided."
}
```

## Rate Limiting

To prevent abuse, the API implements rate limiting. If you exceed the limit, you will receive a response with an HTTP status code of 429 (Too Many Requests).

## Security

All API requests must include an API key in the header. The key should be included in the `x-api-key` field. Unauthorized requests will receive a 403 (Forbidden) response.

## Support

For any issues or queries related to the API, please refer to the [USAGE.md](USAGE.md) guide or contact our support team.
