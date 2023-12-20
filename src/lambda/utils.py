import boto3
import json
import time

# Initialize AWS services
s3 = boto3.client('s3')

def log_event(event):
    """
    Logs the received event for debugging and auditing purposes.
    """
    print(f"Received event: {json.dumps(event, indent=2)}")

def generate_report(results):
    """
    Generates a JSON report from the scan results.
    """
    report = {
        "timestamp": time.time(),
        "results": results
    }
    return json.dumps(report, indent=2)

def store_report_s3(bucket_name, report_name, report):
    """
    Stores the generated report in the specified S3 bucket.
    """
    try:
        response = s3.put_object(
            Bucket=bucket_name,
            Key=report_name,
            Body=report,
            ContentType='application/json'
        )
        print(f"Report stored successfully in {bucket_name}/{report_name}")
    except Exception as e:
        print(f"Failed to store report in S3: {e}")

def get_ec2_instances(ec2):
    """
    Retrieves a list of all EC2 instances.
    """
    try:
        instances = ec2.describe_instances()
        return instances
    except Exception as e:
        print(f"Failed to retrieve EC2 instances: {e}")

def get_s3_buckets(s3):
    """
    Retrieves a list of all S3 buckets.
    """
    try:
        buckets = s3.list_buckets()
        return buckets
    except Exception as e:
        print(f"Failed to retrieve S3 buckets: {e}")

def get_iam_policies(iam):
    """
    Retrieves a list of all IAM policies.
    """
    try:
        policies = iam.list_policies(Scope='Local')
        return policies
    except Exception as e:
        print(f"Failed to retrieve IAM policies: {e}")
