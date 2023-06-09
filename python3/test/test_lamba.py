#from src import app
from app import lambda_handler
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_sum_numbers(self):
        event = {'numbers': [1, 2, 3, 4, 5]}
        expected_result = 15

        response = lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], expected_result)

