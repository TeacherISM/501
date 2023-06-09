from src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_handler(self):
        result = app.lambda_handler(None , None)
        self.assertEqual(result, 4)

class AppTest(TestCase): 
    def test_sum_numbers():
    event = {'numbers': [1, 2, 3, 4, 5]}
    expected_result = 15

    response = app.ambda_handler(event, None)

    assert response['statusCode'] == 200
    assert response['body'] == expected_result

