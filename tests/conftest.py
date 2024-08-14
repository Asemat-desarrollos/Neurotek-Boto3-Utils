import json
from datetime import datetime
from os import path
from typing import Generator
from unittest.mock import patch

import boto3
import moto
from _pytest.monkeypatch import MonkeyPatch
from mypy_boto3_s3 import S3ServiceResource
from mypy_boto3_s3.service_resource import Bucket
from pytest import fixture

REGION_NAME = "us-east-1"

# S3 data
KEY = "Client/Project/test_doc.pdf"
BUCKET_NAME = "my-bucket"

# Secrets Manager data
SECRET_NAME = "my-secret"
SECRET_DATA = {"username": "admin", "password": "password123"}

# Step Functions data
STATE_MACHINE_ARN = (
    "arn:aws:states:us-east-1:123456789012:execution:HelloWorld-StateMachine"
)
STATE_MACHINE_EXECUTION_DATA = {
    "executionArn": f"{STATE_MACHINE_ARN}:1234567890",
    "startDate": datetime(2021, 1, 1),
    "ResponseMetadata": {
        "RequestId": "12345678-1234-1234-1234-123456789012",
        "HTTPStatusCode": 200,
    },
}


with open(path.join(path.dirname(__file__), "data/test_doc.pdf"), "rb") as f:
    MOCK_FILE = f.read()


@fixture(autouse=True)
def mock_env(monkeypatch: MonkeyPatch):
    monkeypatch.setenv("S3_BUCKET", BUCKET_NAME)


@fixture
def mock_s3_resource() -> Generator[S3ServiceResource, None, None]:
    with moto.mock_aws():
        yield boto3.resource("s3", region_name=REGION_NAME)


@fixture
def mock_bucket(mock_s3_resource: S3ServiceResource) -> Bucket:
    mock_s3_resource.create_bucket(Bucket=BUCKET_NAME)
    return mock_s3_resource.Bucket(BUCKET_NAME)


@fixture
def sample_file(mock_bucket: Bucket) -> Generator[bytes, None, None]:
    mock_bucket.put_object(Key=KEY, Body=MOCK_FILE)
    yield MOCK_FILE


@fixture
def mock_secrets_manager() -> Generator[None, None, None]:
    def side_effect_func(**kwargs):  # noqa :N803
        if kwargs["SecretId"] == SECRET_NAME:
            return {"SecretString": json.dumps(SECRET_DATA)}

        return None

    # Mock the return value of get_secret_value
    with patch("boto3.session.Session.client") as mock_client:
        mock_client.return_value.get_secret_value.side_effect = side_effect_func
        yield


@fixture
def mock_step_functions() -> Generator[None, None, None]:
    def side_effect_func(**kwargs):
        if kwargs["stateMachineArn"] == STATE_MACHINE_ARN:
            return STATE_MACHINE_EXECUTION_DATA

    # Mock the return value of start_execution
    with patch("boto3.client") as mock_client:
        mock_client.return_value.start_execution.side_effect = side_effect_func
        yield
