import io

import pytest
from mypy_boto3_s3.service_resource import Bucket

from boto3_utils.s3 import download_s3_file
from boto3_utils.s3 import get_bucket_name_and_key_from_uri
from boto3_utils.s3 import get_s3_bucket
from boto3_utils.s3 import upload_s3_file
from tests.conftest import BUCKET_NAME
from tests.conftest import KEY


class TestGetBucketNameAndKeyFromUri:
    def test_get_bucket_name_and_key_from_uri(self):
        uri = "s3://my-bucket/test_doc_001.pdf"
        bucket, key = get_bucket_name_and_key_from_uri(uri)

        assert bucket == "my-bucket"
        assert key == "test_doc_001.pdf"

    def test_get_bucket_and_key_name_from_uri_invalid(self):
        uri = "neurotek/test_doc_001.pdf"

        with pytest.raises(ValueError) as e:
            get_bucket_name_and_key_from_uri(uri)

        assert f"Invalid S3 URI: {uri}" in str(e.value)


class TestGetBucket:
    def test_get_s3_bucket_success(self, mock_bucket):
        bucket = get_s3_bucket(BUCKET_NAME)

        assert bucket is not None


class TestDownloadS3File:
    def test_download_s3_file(self, mock_bucket: Bucket, sample_file: bytes):
        uri = f"s3://{BUCKET_NAME}/{KEY}"

        with io.BytesIO() as downloaded_data:
            download_s3_file(mock_bucket, uri, downloaded_data)

            assert downloaded_data.getvalue() == sample_file

    def test_download_s3_file_not_found(self, mock_bucket: Bucket):
        uri = f"s3://{BUCKET_NAME}/non-existent-key"

        with (
            pytest.raises(FileNotFoundError) as exc_info,
            io.BytesIO() as downloaded_data,
        ):
            download_s3_file(mock_bucket, uri, downloaded_data)

        assert exc_info.value.args[0] == "Not Found"


class TestUploadS3File:
    def test_upload_s3_file(self, mock_bucket: Bucket, sample_file: bytes):
        uri = f"s3://{BUCKET_NAME}/second-{KEY}"
        key = upload_s3_file(mock_bucket, uri, sample_file)
        assert key == uri
