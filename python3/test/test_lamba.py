from src import lambda_handler
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_handler(self):
        result = lambda_handler(None , None)
        self.assertEqual(result, 4)


from src import lambda_handler

def test_sum_numbers():
    event = {'numbers': [1, 2, 3, 4, 5]}
    expected_result = 15

    response = lambda_handler(event, None)

    assert response['statusCode'] == 200
    assert response['body'] == expected_result

