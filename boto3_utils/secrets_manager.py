import json
import os
from typing import Any
from typing import Optional

import boto3.session
from mypy_boto3_secretsmanager import SecretsManagerClient


def get_secret(
    secret_id: str, region_name: Optional[str] = None
) -> str | dict[str, Any]:
    """
    Returns a secret from AWS Secrets Manager.

    Args:
        secret_id: The ID of the secret.
        region_name: (Optional) The name of the AWS region. If not provided, it\
            will be read from the `REGION_NAME` environment variable, or default\
            to `us-east-1`.

    Environment variables:
        REGION_NAME: (Optional) The name of the AWS region.

    Returns:
        The secret as a string or a dictionary.
    """

    if region_name is None:
        region_name = os.environ.get("REGION_NAME", "us-east-1")

    session = boto3.session.Session()
    client: SecretsManagerClient = session.client(
        service_name="secretsmanager", region_name=region_name
    )
    response = client.get_secret_value(SecretId=secret_id)
    if response is not None:
        parsed_secret: str | dict[str, Any] = json.loads(response["SecretString"])
        return parsed_secret
    else:
        raise ValueError(f"Secret '{secret_id}' not found")
