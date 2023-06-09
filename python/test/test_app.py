import lambda_function
from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

def test_sum_numbers():
    assert lambda_function.sum_numbers(2, 3) == 5

def test_lambda_handler():
    event = {'num1': 2, 'num2': 3}
    result = lambda_function.lambda_handler(event, None)
    assert result == 5
