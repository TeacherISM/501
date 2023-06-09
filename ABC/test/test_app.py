import json
from src import lambda_handler


def test_lambda_handler():
    # Define the test input
    event = {
        'number1': 3,
        'number2': 5
    }

    # Invoke the lambda_handler
    result = lambda_handler(event, None)

    # Extract the response body
    response_body = json.loads(result['body'])

    # Assert the expected values
    assert result['statusCode'] == 200
    assert response_body['sum'] == 8
