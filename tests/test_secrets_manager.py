import pytest

from boto3_utils.secrets_manager import get_secret

from .conftest import SECRET_DATA
from .conftest import SECRET_NAME


class TestSecretsManager:
    def test_get_secret_success(self, mock_secrets_manager):
        result = get_secret(SECRET_NAME)

        assert result == SECRET_DATA

    def test_get_secret_not_found(self, mock_secrets_manager):
        with pytest.raises(ValueError) as exc_info:
            get_secret("non-existent-secret")

        assert exc_info.value.args[0] == "Secret 'non-existent-secret' not found"
