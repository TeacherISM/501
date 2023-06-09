import pytest
from lambda_handler import handler  # Assuming the lambda function is in a file named my_lambda.py

def test_handler():
    # Create a mock event
    event = {"numbers": [1, 2, 3, 4, 5]}
    context = {}  # Context can usually be an empty dictionary for testing purposes

    # Call the lambda function with the mock event and context
    result = handler(event, context)

    # Assert that the sum is correct
    assert result == {"sum": 15}