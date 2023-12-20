# AWS Cloud Security Posture Management (CSPM) MVP

This repository contains the source code for a Minimum Viable Product (MVP) of a Cloud Security Posture Management (CSPM) system. The system is built using AWS microservices, focusing on rapid deployment and core functionality. The architecture is serverless, utilizing AWS Lambda for the execution of CSPM logic, Amazon S3 for immutable storage of logs and reports, and Amazon DynamoDB for efficient metadata and configuration management. The system exposes its functionality through a RESTful API interface, orchestrated via AWS API Gateway.

## Repository Structure

```
aws-cspm-mvp/
│
├── src/
│   ├── lambda/
│   │   ├── cspm_function.py     # Main Lambda function for CSPM logic.
│   │   └── utils.py             # Utility functions used by the CSPM function.
│   │
│   └── api/
│       ├── api_handler.py       # Handles API Gateway requests and responses.
│       └── routes.py            # Defines the API routes and their handlers.
│
├── templates/
│   ├── cloudformation.yml       # AWS CloudFormation template for resource setup.
│   └── dynamodb_schema.json     # Schema definition for the DynamoDB table.
│
├── tests/
│   ├── lambda_tests.py          # Unit tests for Lambda functions.
│   └── api_tests.py             # Unit tests for API handlers.
│
├── scripts/
│   ├── deploy.sh                # Script for deploying the application.
│   └── setup.sh                 # Script for initial setup of AWS resources.
│
├── docs/
│   ├── API.md                   # Documentation for the API endpoints.
│   ├── SETUP.md                 # Setup guide for the CSPM system.
│   └── USAGE.md                 # User guide for using the CSPM system.
│
├── .github/
│   ├── workflows/
│   │   └── ci_cd.yml            # GitHub Actions workflow for CI/CD.
│   │
│
├── README.md                    # Overview and instructions for the repository.
└── requirements.txt             # Lists dependencies for the Python application.
```

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/aws-cspm-mvp.git
   cd aws-cspm-mvp
   ```

2. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the setup script to initialize AWS resources:
   ```
   ./scripts/setup.sh
   ```

4. Deploy the application:
   ```
   ./scripts/deploy.sh
   ```

## Documentation

For more detailed information on the API endpoints, system setup, and usage, please refer to the `docs/` directory.

- [API Documentation](docs/API.md)
- [Setup Guide](docs/SETUP.md)
- [Usage Guide](docs/USAGE.md)

## Testing

Unit tests are located in the `tests/` directory. To run the tests, use the following command:

```
python -m unittest discover tests
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
