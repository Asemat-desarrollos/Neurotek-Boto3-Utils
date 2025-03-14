import os
import re
from typing import IO
from typing import Any
from typing import Optional

import boto3
from botocore.exceptions import ClientError
from mypy_boto3_s3.service_resource import Bucket


def get_bucket_name_and_key_from_uri(uri: str) -> tuple[str, str]:
    """
    Extracts the bucket name and the key from an S3 URI.

    Args:
        uri: An S3 URI.

    Returns:
        A tuple with the bucket name and the key.
    """
    match = re.match(r"s3://(?P<bucket_name>[^/]+)/(?P<key>.+)", uri)

    if match is None:
        raise ValueError(f"Invalid S3 URI: {uri}")

    return match.group("bucket_name"), match.group("key")


def get_s3_bucket(bucket_name: str, region_name: Optional[str] = None) -> Bucket:
    """
    Returns an S3 bucket.

    Args:
        bucket_name: The name of the bucket.
        region_name: (Optional) The name of the AWS region. If not provided, it\
            will be read from the `AWS_DEFAULT_REGION` environment variable, or\
            default to `us-east-1`.

    Environment variables:
        AWS_DEFAULT_REGION: (Optional) The name of the AWS region.

    Returns:
        An S3 bucket resource.
    """
    if region_name is None:
        region_name = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")

    s3 = boto3.resource("s3", region_name=region_name)
    bucket: Bucket = s3.Bucket(bucket_name)

    return bucket


def download_s3_file(bucket: Bucket, key: str, target: IO[Any]) -> None:
    """
    Downloads a file from S3 to a buffer (file or in-memory buffer).

    Args:
        bucket: The S3 bucket resource.
        key: The key of the file to download.
        target: The buffer where the file will be written.
    """
    m = re.match(r"(?:s3://[^/]+)?/?(.+)", key)
    assert m is not None, f"Invalid S3 key: {key}"
    key = m.group(1)

    try:
        bucket.download_fileobj(key, target)
        target.seek(0)
    except ClientError as e:
        error_message = e.response.get("Error", {}).get(
            "Message", f"URI '{key}' not found."
        )
        raise FileNotFoundError(error_message)


def upload_s3_file(bucket: Bucket, key: str, data: bytes, **kwargs) -> str:
    """
    Uploads a file to an S3 bucket.

    Args:
        bucket: The S3 bucket resource.
        key: The key of the blob to be uploaded.
        data: The bytes to be uploaded.
        **kwargs: Additional arguments to be passed to the `put` method.

    Returns:
        The Key of the uploaded image.
    """
    s3_object = bucket.Object(key)
    s3_object.put(Body=data, **kwargs)

    return s3_object.key
