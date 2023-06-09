from src.app import aws_Lambda as handler
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_handler(caplog):
    caplog.set_level(logging.INFO)  # Set the log level to capture INFO and above

    ret = handler(None, None)

    assert ret['statusCode'] == 200
    assert ret['body'] == 3

    # Retrieve the captured logs
    logs = [record.getMessage() for record in caplog.records]

    # Assert that the expected log message is present
    assert '3' in logs
