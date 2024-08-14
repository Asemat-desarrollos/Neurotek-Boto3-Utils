import json
import os
from typing import Any
from typing import Optional

import boto3
from mypy_boto3_stepfunctions import SFNClient
from mypy_boto3_stepfunctions.type_defs import StartExecutionOutputTypeDef


def start_step_function(
    state_machine_arn: str,
    payload: str | dict[str, Any],
    region_name: Optional[str] = None,
) -> StartExecutionOutputTypeDef:
    """
    Starts a Step Function execution.

    Args:
        state_machine_arn: The ARN of the Step Function state machine.
        payload: The input to the execution.
        region_name: (Optional) The name of the AWS region. If not provided, it\
            will be read from the `AWS_DEFAULT_REGION` environment variable, or\
            default to `us-east-1`.

    Environment variables:
        AWS_DEFAULT_REGION: (Optional) The name of the AWS region.

    Returns:
        The response from the `start_execution` call.
    """
    if region_name is None:
        region_name = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")

    stepfunctions_client: SFNClient = boto3.client(
        "stepfunctions", region_name=region_name
    )

    if not isinstance(payload, str):
        payload = json.dumps(payload)

    response = stepfunctions_client.start_execution(
        stateMachineArn=state_machine_arn,
        input=payload,
    )

    return response
