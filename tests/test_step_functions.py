from boto3_utils.step_functions import start_step_function
from tests.conftest import STATE_MACHINE_ARN
from tests.conftest import STATE_MACHINE_EXECUTION_DATA


class TestStepFunctions:
    def test_start_step_function_success(self, mock_step_functions):
        result = start_step_function(
            state_machine_arn=STATE_MACHINE_ARN,
            payload='{"key": "value"}',
        )

        assert result == STATE_MACHINE_EXECUTION_DATA

    def test_start_step_function_success_payload_not_string(self, mock_step_functions):
        result = start_step_function(
            state_machine_arn=STATE_MACHINE_ARN,
            payload={"key": "value"},
        )

        assert result == STATE_MACHINE_EXECUTION_DATA
