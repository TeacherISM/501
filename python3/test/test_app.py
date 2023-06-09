from src import app
from unittest import TestCase
import sys
sys.path.append('..')


class AppTest(TestCase):
    def test_sum_numbers(self):
        event = {'numbers': [1, 2, 3, 4, 5]}
        expected_result = 15

        response = app.lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], expected_result)

