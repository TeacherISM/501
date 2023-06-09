from src import app
import sys
sys.path.append('../src')


def test_sum_numbers():
    assert app.sum_numbers(2, 3) == 5


def test_lambda_handler():
    event = {'num1': 2, 'num2': 3}
    result = app.lambda_handler(event, None)
    assert result == 5
